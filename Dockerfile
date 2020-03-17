FROM python:3.5.4

# Explicitly set user/group IDs
RUN groupadd -r uwsgi --gid=999 && useradd -r -g uwsgi --uid=999 uwsgi

# Folder structure
RUN mkdir -p /var/app/storage \
    && chown -R uwsgi:uwsgi /var/app

WORKDIR /var/app

# Uploads folder
VOLUME /var/app/storage

# Service port
EXPOSE 8081

# Configue timezone
ENV TIMEZONE "America/Mexico_City"
RUN echo "$TIMEZONE" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

# Install uWSGI and pipenv
RUN set -ex; \
    pip install pipenv uWSGI --no-cache-dir;

# Add project
COPY . /var/app

# Project dependencies
RUN set -xe \
    && pipenv install --deploy --system

CMD [ "uwsgi", "/var/app/challenge/uwsgi.ini" ]
