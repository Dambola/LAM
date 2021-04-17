# STEP 1 BUILD QUASAR PROJECT
FROM node:14.16.1-alpine3.10 AS quasar-stage
WORKDIR /lam-web-app
COPY package.json ./
RUN npm install -g @quasar/cli
RUN npm install
COPY . .
RUN quasar build

# STEP 2 CREATE NGINX SERVER
FROM nginx:1.19.0-alpine AS server-stage
COPY --from=quasar-stage /lam-web-app/dist/spa /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
