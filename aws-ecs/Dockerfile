FROM amazonlinux:latest

# set environment varibles. Need to print to appear in cloudwatch
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /source
RUN mkdir -p /source/api 
RUN mkdir -p /source/db
RUN mkdir -p /source/static

COPY ./Main.sh /source
COPY ./Install_Python.sh /source
COPY ./requirements.txt /source
COPY ./Run_Flask_Server.py /source
COPY ./ValidateEnv.sh /source
COPY ./api/health.py /source/api
COPY ./api/mydata.py /source/api
COPY ./api/__init__.py /source/api
COPY ./db/__init__.py /source/db
COPY ./db/postgre_db.py /source/db
COPY ./static/swagger.json /source/static




RUN chmod +x Main.sh
RUN chmod +x Install_Python.sh
RUN chmod +x requirements.txt
RUN chmod +x Run_Flask_Server.py
RUN chmod +x ValidateEnv.sh
RUN chmod +x /source/api/health.py
RUN chmod +x /source/api/mydata.py
RUN chmod +x /source/api/__init__.py
RUN chmod +x /source/db/__init__.py
RUN chmod +x /source/db/postgre_db.py
RUN chmod +x /source/static/swagger.json


EXPOSE 80

ENTRYPOINT ["./Main.sh"]
