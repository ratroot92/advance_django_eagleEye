FROM ubuntu:18.04
WORKDIR /var/www/d_auth
COPY . .
CMD /bin/bash