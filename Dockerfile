FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install -r requirements.txt

RUN pip install ipdb

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
