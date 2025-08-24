FROM nginx:alpine

COPY ./web/dist/ /usr/share/nginx/html
RUN chown -R nginx:nginx /usr/share/nginx/html
COPY ./docker/web/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]