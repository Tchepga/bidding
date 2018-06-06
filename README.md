## To build this image
git clone https://github.com/billmetangmo/bidding.git

cd docker;docker build -t qopius/challenge:python-2.7-alpine-onbuild .

cd .. ; docker build -t qopius/challenge:python-2.7 .

## To run it
docker run --net host qopius/challenge:python-2.7

The ENV variables for the doker images are: RANDOMIZER_LOWER_VALUE; RANDOMIZER_LOWER_VALUE;IP; PORT


## To test the API
curl -X GET http://<IP>:<PORT>/start?duration=xx
 
curl -X GET http://<IP>:<PORT>/bid/<id>?amount=xx&name=yy
 
curl -X GET http://<IP>:<PORT>/getactualprice/<id>
 
curl -X GET http://<IP>:<PORT>/getwinner/<id>
 

