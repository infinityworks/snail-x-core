FROM python:3

RUN mkdir -p snail-x-core

ADD * /snail-x-core/

RUN pip install -r /snail-x-core/requirements.txt

CMD [ "python", "/snail-x-core/app.py" ]

