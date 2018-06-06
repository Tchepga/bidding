FROM python:2.7-alpine
MAINTAINER Bill Metangmo <bilmetangmo@yahoo.fr> 

ONBUILD ADD requirements.txt /app
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
ONBUILD COPY . /app

WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["python"]
CMD [ "application.py" ]
