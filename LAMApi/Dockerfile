FROM python:3.8-alpine

WORKDIR /lam-rest-api

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-wsgi python-dev python-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip --no-cache-dir install -r requirements

RUN a2dissite default
RUN a2dissite default-ssl
RUN a2enmod wsgi

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

COPY lamapi /lam-rest-api/lamapi
COPY config/lam-api.conf /etc/apache2/sites-available

RUN chown -R www-data:www-data /lam-rest-api
RUN chown www-data:www-data /etc/apache2/sites-available/lam-api
RUN a2ensite lam-api

EXPOSE 8390
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]