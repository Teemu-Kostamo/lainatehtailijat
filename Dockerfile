FROM python:latest
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . src
WORKDIR /src

EXPOSE 8000

RUN python lainatehtailijat/manage.py collectstatic

ENTRYPOINT [ "python", "lainatehtailijat/manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]