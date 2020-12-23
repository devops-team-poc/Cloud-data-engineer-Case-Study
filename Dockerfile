FROM debian:buster-slim
WORKDIR /app 

RUN apt update && apt install -y gnupg

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Install ``software-properties-common`` and PostgreSQL

RUN apt-get update && apt-get install -y  software-properties-common postgresql postgresql-client postgresql-contrib

# Installing python
RUN apt-get update
RUN apt-get install -y python3 python3-pip curl  net-tools
RUN apt-get install -y  gcc python3-dev musl-dev python-virtualenv
RUN pip3 install --user --upgrade virtualenv==20.0.28


COPY . .
ENV DJANGO_SETTINGS_MODULE=najla.settings
RUN virtualenv venv -p python3
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER najla_user WITH SUPERUSER PASSWORD 'najlapass';" &&\
    createdb -O najla_user najla_db
RUN /bin/bash -c  "source venv/bin/activate" && pip3 install -r requirements.txt && /etc/init.d/postgresql start && cd /app;python3 manage.py makemigrations && cd /app;python3 manage.py migrate

 
# Expose the PostgreSQL port
EXPOSE 8000
 
# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# RUN /etc/init.d/postgresql start && python3 /app/json_import.py
# Set the default command to run when starting the container
CMD /etc/init.d/postgresql start && python3 /app/json_import.py && cd /app;python3 manage.py runserver 0:8000