

FROM python:3.11

WORKDIR /flaskines

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 80
COPY entrypoint.sh
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]


#ENTRYPOINT ["python3", "/flaskines/index.py"]