FROM nginx
RUN echo '<h2>Hello, Docker!</h2>' > /usr/share/nginx/html/index.html
