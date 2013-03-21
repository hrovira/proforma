proforma
========
> Instructions for installing, compiling and deploying this *Prototype Data Entry Web App*

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
> Download and install these libraries before proceeding

* Git http://git-scm.com/downloads
* Python 2.7 http://www.python.org/download/releases/2.7/
* MongoDB 2.x http://www.mongodb.org/downloads
    * MongoDB SQL cheat-sheet http://docs.mongodb.org/manual/reference/sql-comparison/
* NodeJS NPM http://nodejs.org/download/

#### Web Application Initial Build

```bash
   # check out project from github into a new 'proforma' directory (project root)
   $ git clone https://github.com/hrovira/proforma.git
```

> These commands should be executed from within project root

```bash
   # installs brunch build system for developers
   $ [sudo] npm install -g brunch
   
   # creates node_modules directory containing downloaded dependencies (don't check-in)
   $ npm install
  
   # creates _public directory (don't check-in)
   # web app is compiled into single-page static HTML website with minified JavaScript
   # serve as static content from your web server, or use tornado as static content handler 
   $ brunch build -c brunch.coffee 
```

## Deployment

#### MongoDB
```bash
   # start MongoDB storage and lookup databases
   $ mongod --dbpath /local/path/to/mongoDB/ --port 3032
```

#### TornadoWeb
> These commands should be executed from within project root

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
> These commands should be executed from within project root

```bash
   # this process monitors changes in your web application and auto-compiles into _public
   $ brunch w -c brunch.coffee
```
