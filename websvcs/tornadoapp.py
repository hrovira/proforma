#!/usr/bin/env python
"""
Start server:
python tornadoapp.py
(Default port is 8000)
python tornadoapp.py --port=8001

"""

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, HTTPError, Application, StaticFileHandler
from tornado.options import define, options, logging
from tornado.options import parse_command_line, parse_config_file

from uuid import uuid4

import random
import string

from dao import MongoDbHandler

char_set = string.ascii_uppercase + string.digits

define("port", default=8000, help="run on the given port", type=int)
define("config_file", help="Path to config file")
define("client_secret", help="client_secret")
define("mongo_uri", default="http://localhost:8080", help="options.mongo_uri")

settings = {
    "debug": True,
    "cookie_secret": uuid4()
}

server_settings = {
    "xheaders" : True,
    "address" : "0.0.0.0"
}

class RootHandler(RequestHandler):
    def get(self):
        with open("_public/index.html", "rb") as file:
            self.write(file.read())
            self.set_status(200)

class AuthWhoAmiHandler(RequestHandler):
    def get(self):
        logging.info("AuthWhoAmiHandler.get")

        whoami = {
            "user": "hrovira",
            "label": "Hector Rovira"
        }
        self.write(whoami)
        self.set_status(200)

class AuthSignoutHandler(RequestHandler):
    def post(self):
        logging.info("AuthSignoutHandler.post")
        self.set_status(200)

def main():
    parse_command_line()
    if not options.config_file is None:
        parse_config_file(options.config_file)
        parse_command_line()

    if not options.client_secret is None:
        settings["cookie_secret"] = options.client_secret

    logging.info("Starting tornadoweb on http://localhost:%s" % options.port)
    if not options.config_file is None:
        logging.info("--config_file=%s" % options.config_file)

    application = Application([
        (r"/auth/whoami", AuthWhoAmiHandler),
        (r"/auth/signout", AuthSignoutHandler),
        (r"/dao/?(.*)", MongoDbHandler),
        (r"/", RootHandler),
        (r"/(.*)", StaticFileHandler, {"path": "_public"})
    ], **settings)
    application.listen(options.port, **server_settings)

    IOLoop.instance().start()

if __name__ == "__main__":
    main()