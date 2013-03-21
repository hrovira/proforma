proforma
========
> Instructions for installing, compiling and deploying *Prototype Data Entry Web* application

## Support

#### Operating Systems
* Mac OS X
* Linux
* easy to port to other systems

#### Browsers
* HTML5 complaint
* tested on Google Chrome

## Installation

#### Required Libraries
> Download and Install these before proceeding

* Python 2.7 http://www.python.org/download/releases/2.7/
* MongoDB 2.x http://www.mongodb.org/downloads
* NodeJS NPM http://nodejs.org/download/

#### Web Application Initial Build
> All commands should be executed from the root of this project.  

```bash
   # installs brunch build system for developers
   $ [sudo] npm install -g brunch
   
   # creates node_modules directory containing downloaded dependencies (don't check-in)
   $ npm install
  
   # creates _public directory (don't check-in)
   # web app is compiled into single-page static HTML website with minified JavaScript
   # serve as static content from your web server, or use tornado as static content handler 
   $ brunch build
```

## Deployment

#### MongoDB
```bash
   # start MongoDB storage and lookup databases
   $ mongod --dbpath /local/path/to/mongoDB/ --port 3032
```

#### TornadoWeb
```bash
   # start tornado to provide web services and authentication
   # tornado.config (see below) specifies properties used by Python web services
   $ python websvcs/tornadoapp.py --config_file=/local/path/to/tornado.config

   # contents of tornado.config
   port=8000
   mongo_uri="mongodb://localhost:3032"
```
> Upon successful launch, the web application will be accessible at [http://localhost:8000](http://localhost:8000)

#### Development Mode Auto-update 
```bash
   # this process monitors changes in your web application and auto-compiles into _public
   $ brunch w -c brunch.coffee
```
