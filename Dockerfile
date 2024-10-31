FROM node:22.11.0-bullseye-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/AalmanSadath/TransistorDatabase.git .

WORKDIR /app/restapi
RUN npm install

EXPOSE 8080

CMD ["node", "index.js"]

