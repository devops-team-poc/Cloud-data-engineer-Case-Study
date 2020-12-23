FROM debian:buster-slim
WORKDIR /app 

RUN apt update && apt install -y gnupg
# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.3
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y  software-properties-common postgresql postgresql-client postgresql-contrib

# Installing python
RUN apt-get update
RUN apt-get install -y python3 python3-pip curl  net-tools
# RUN apt-get -y install python3.7-dev 
# RUN apt-get install -y postgresql-server-dev-12 gcc python3-dev musl-dev python-virtualenv
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

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``
 
# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
 
# Create a PostgreSQL role named ``postgresondocker`` with ``postgresondocker`` as the password and
# then create a database `postgresondocker` owned by the ``postgresondocker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.


# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
 
# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
#RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
 
# Expose the PostgreSQL port
EXPOSE 8000
 
# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# RUN /etc/init.d/postgresql start && python3 /app/json_import.py
# Set the default command to run when starting the container
CMD /etc/init.d/postgresql start && python3 /app/json_import.py && cd /app;python3 manage.py runserver 0:8000