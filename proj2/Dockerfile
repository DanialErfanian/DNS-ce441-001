FROM node:13


# Create app directory
ADD code/yarn.lock /home/ce441/proj2/
ADD code/package.json /home/ce441/proj2/
WORKDIR /home/ce441/proj2/

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

RUN npm install
ADD code/ /home/ce441/proj2/

# Bundle app source
COPY . .

EXPOSE 3000
CMD [ "npm", "start" ]
