# STEP 1 BUILD QUASAR PROJECT
FROM python:3.8-alpine AS python-stage
WORKDIR /lam-rest-api
ADD . /lam-rest-api
RUN pip install -r REQUIREMENTS
EXPOSE 8390
CMD ["uwsgi", "run.ini"]

# STEP 2 CREATE NGINX SERVER
FROM nginx AS server-stage
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=server-stage nginx.conf /etc/nginx/conf.d/