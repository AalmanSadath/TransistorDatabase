# Use Node.js 22.1.0 as the base image
FROM node:22.11.0-bullseye-slim

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y git

# Clone the Git repository
RUN git clone https://github.com/AalmanSadath/TransistorDatabase.git .

# Install dependencies in the restapi folder
WORKDIR /app/restapi
RUN npm install

# Expose the application port
EXPOSE 8080

# Start the Node.js app
CMD ["node", "index.js"]

