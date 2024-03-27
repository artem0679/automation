FROM ubuntu:20.04
ENV TZ=Europe/Moscow 
WORKDIR /app
COPY . .
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential 
RUN apt-get install -y python3-dev default-libmysqlclient-dev 
RUN apt-get install -y pkg-config 
RUN apt-get install -y gunicorn 
RUN pip3 install -r requirements.txt
WORKDIR /app/app
CMD /usr/bin/gunicorn -b 0.0.0.0:80 -w 4 app:app
