FROM node:18.14.2-alpine as node
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build --prod

FROM nginx:alpine
COPY --from=node /app/dist/dns-service-frontend /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
