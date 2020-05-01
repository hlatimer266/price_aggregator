FROM node:10
MAINTAINER Harrison Latimer <latimerh@oregonstate.edu>

WORKDIR /price_aggregator/price_agg_frontend

COPY /price_agg_frontend/package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["node", "index.js"]