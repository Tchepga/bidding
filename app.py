import os
import random
import datetime
import logging
import time
import model
import cron
import config

from flask import Flask,request,jsonify
from time import strftime
from threading import Thread
from model import Enchere,Enchere_Status
from cron import CronJobSeconds
from data import encheres
from utils import get_log_time

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def hello():
    return "Welcome to Qopius challenge!"

@app.route('/start')
def start():
    
    ## validation of args
    duration= request.args.get('duration')
    if request.args.get('duration') is None:
        return jsonify(message="", error="you must provide the duration of the bid(in seconds)")
        
    ## state mutation
    bid_begin_date = datetime.datetime.now()
    id = random.randint(os.getenv('RANDOMIZER_LOWER_VALUE', 0),os.getenv('RANDOMIZER_UPPER_VALUE', 100))
    enchere= Enchere(bid_begin_date,request.args.get('duration'))
    ts=get_log_time()
    encheres[id] = enchere
    app.logger.info('[INFO] %s %s start endpoint: A new bid with %s has begun with exact time=%s',ts,request.remote_addr,id,bid_begin_date)
    
    ## start the bid killer
    duration=int(duration)
    BidTerminator = CronJobSeconds(duration)
    BidTerminator.setName(id)
    BidTerminator.start()
    
    bid_duration = datetime.timedelta(seconds=duration)
    bid_end_date = bid_begin_date+bid_duration
    app.logger.info('[INFO] %s %s start endpoint: Create a CRON job to stop bid %s at  %s',ts,request.remote_addr,id,bid_end_date)
    
    return jsonify(message=id, error="")


@app.route('/bid/<int:id>')
def bid(id):
    
    ## validation of URI
    if id not in encheres:
        return jsonify(message="", error="the required bid doesn't exist")
    
    ## validation of args
    enchere = encheres[id]
    status = enchere.status
    if status == Enchere_Status.FINISHED:
        return jsonify(message="", error="The bid is already finished")
        
    amount= request.args.get('amount')
    if amount is None:
        return jsonify(message="", error="The amount of bid can not be null")
            
    client_name= request.args.get('name')
    if client_name is None:
        return jsonify(message="", error="The name of the client can not be null")
        
    
    ts = get_log_time()
    curr_price = str(enchere.price)
    curr_client = str(enchere.client)
    
    # for pretty log message: seller instead of ""
    if enchere.client =="" :
        curr_client="seller"
        
    if amount > curr_price:
        
        ## state mutation
        enchere.set_price(amount)
        enchere.set_client(client_name)
        
        amount =str(amount)
        client_name = str(client_name)
        app.logger.info('[INFO] %s %s bid endpoint: bid of client %s accepted because %s is superior to current price %s from %s',ts,request.remote_addr,client_name,amount,curr_price,curr_client)
        return jsonify(message="success", error="")
        
    else:
            
        client_name = str(client_name)
        amount =str(amount)
            
        app.logger.info('[INFO] %s %s bid endpoint: bid of client %s refused because %s is inferior to current price %s from  %s',ts,request.remote_addr,id,client_name,amount,curr_price,curr_client)
        return jsonify(message="", error="the proposed bid is lower than the current value. Use get Use /getactualprice to get the current price")
            
        
@app.route('/getactualprice/<int:id_enchere>')
@app.route('/getwinner/<int:id_enchere>')
## The endpoint is the same for 2 routes because the business logic is the same
## What's change is just the message depending of the status of the bid
## This helps avoid code duplication
def get_current_winner(id_enchere):
    
    if id_enchere not in encheres:
        return jsonify(message="", error="The required bid doesn't exist")
        
    enchere = encheres[id_enchere]
    price=str(enchere.price)
    name =str(enchere.client)
    status = enchere.status
        
    # for pretty return response to client "nobody" instead of ""
    if name=="":
        name="nobody"
        
    # This is a trick to get the current route
    # See more https://stackoverflow.com/questions/21498694/flask-get-current-route
    rule = request.url_rule
    if 'getactualprice' in rule.rule:
        if status == Enchere_Status.FINISHED:
            return jsonify(message="", error="The bid is already finished. Use /getwinner to get results")
            
        return jsonify(price=price,client=name, error="")
    
    elif 'getwinner' in rule.rule:
        if status != Enchere_Status.FINISHED:
            return jsonify(message="", error="The bid is not yet finished. Use /getactualprice to get the current price")
            
        return jsonify(price=price,client=name, error="")
            

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    
    
##http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
## avec base data: https://github.com/ErnstHaagsman/grouporder/blob/master/grouporder/server.py
    

   
    