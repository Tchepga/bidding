## To build this image
git clone https://github.com/billmetangmo/bidding.git

cd docker;docker build -t qopius/challenge:python-2.7-alpine-onbuild .

cd .. ; docker build -t qopius/challenge:python-2.7 .

## To run it
docker run --net host qopius/challenge:python-2.7

docker run --net host -e PORT xxxx qopius/challenge:python-2.7

docker run -e PORT xxxx:yyyy qopius/challenge:python-2.7

The ENV variables for the doker images are: RANDOMIZER_LOWER_VALUE; RANDOMIZER_LOWER_VALUE;IP; PORT


## To test the API
A service is deployed on GCP at IP/PORT 104.198.205.151/80

curl -X GET http://104.198.205.151/start?duration=xx
 
curl -X GET http://104.198.205.151/bid/<id>?amount=xx&name=yy
 
curl -X GET http://104.198.205.151/getactualprice/<id>
 
curl -X GET http://104.198.205.151/getwinner/<id>
 

