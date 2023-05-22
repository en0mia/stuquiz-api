FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]