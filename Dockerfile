FROM python:3.10-alpine
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . src
WORKDIR /src

EXPOSE 8000

ENTRYPOINT [ "python", "lainatehtailijat/manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]