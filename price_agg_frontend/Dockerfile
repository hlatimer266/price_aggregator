FROM node:10
MAINTAINER Harrison Latimer <latimerh@oregonstate.edu>

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]