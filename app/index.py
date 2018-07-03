import logging
from tornado.web import authenticated
from app.base import BaseHandler

logger = logging.getLogger(__name__)

class MainHandler(BaseHandler):

    @authenticated
    def get(self):
        logger.info("main page get")
        self.render("index.html", messages="hello tornado !")