FROM node:22

WORKDIR /var/www/nestjs_test_app

RUN npm i -g @nestjs/cli
RUN git clone https://github.com/RomanFedyunin/nestjs-test-app.git .
RUN git pull
RUN npm install
