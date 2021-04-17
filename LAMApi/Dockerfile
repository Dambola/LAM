# STEP 1 BUILD QUASAR PROJECT
FROM python:3.8-alpine AS python-stage
WORKDIR /lam-rest-api
ADD lamapi /lam-rest-api
RUN pip install -r requirements
EXPOSE 8390
CMD ["uwsgi", "run.ini"]

# STEP 2 CREATE NGINX SERVER
FROM nginx AS server-stage
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=server-stage nginx.conf /etc/nginx/conf.d/