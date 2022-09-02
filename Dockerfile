FROM python:3.10.4-alpine3.15
ENV TZ "Europe/Moscow"
RUN mkdir /home/api
WORKDIR /home/api
ADD requirements.txt .
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN python -m pip install --upgrade pip
RUN pip install -U -r requirements.txt
ADD . .
CMD ["python3 bot.py"]