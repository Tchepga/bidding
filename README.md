
cd docker
docker build -t qopius/challenge:python-2.7-alpine-onbuild .

docker build -t qopius/challenge:python-2.7 .
docker run --net host qopius/challenge:python-2.7

curl -X GET http://localhost:8080/start?duration=60
curl -X GET "http://localhost:8080/bid/<id>?amount=100&name=blbla"
curl -X GET http://localhost:8080/getactualprice/<id>
curl -X GET http://localhost:8080/getwinner/<id>

