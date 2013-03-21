proforma
========
Prototype Data Entry Webapp

Initial Install
========
npm install - creates node_modules
brunch build - creates _public

Brunch - auto updates changes to _public
========
brunch w -c brunch.coffee

MongoDB - storage and lookup database
========
mongod --dbpath /local/path/to/mongoDB/ --port 3032

TornadoWeb - web services and authentication
========
websvcs/tornadoapp.py --config_file=/local/path/to/tornado.config