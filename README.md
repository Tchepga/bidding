## To build this image
git clone git clone https://github.com/billmetangmo/bidding.git

cd docker;docker build -t qopius/challenge:python-2.7-alpine-onbuild .

cd ..; docker build -t qopius/challenge:python-2.7 .

## To run it
docker run --net host qopius/challenge:python-2.7

## To test the API
curl -X GET http://<IP>:<PORT>/start?duration=xx
 
curl -X GET http://<IP>:<PORT>/bid/<id>?amount=xx&name=yy
 
curl -X GET http://<IP>:<PORT>/getactualprice/<id>
 
curl -X GET http://<IP>:<PORT>/getwinner/<id>
 

