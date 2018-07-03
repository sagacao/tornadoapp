import logging
from tornado.gen import coroutine
from tornado.escape import json_decode, json_encode
from app.base import BaseHandler
import json

from service.user_service import UserService

logger = logging.getLogger(__name__)

class UserHandler(BaseHandler):

    @coroutine
    def get(self):
        useraccount = self.get_argument('useraccount')
        logger.info("role_get_handler {}".format(useraccount))
        res = {"useraccount": useraccount, "accountdata" : []}
        user = yield self.async_do(UserService.get_user, self.db, useraccount)
        if user is not None:
            userdict = self.filter_user(user)
            for k, u in userdict.items():
                # logger.info("--> {0} -- {1}".format(u.userid, u.level))
                res["accountdata"].append({"userid": u.userid, "serverid" : u.serverid, "level" : u.level, "prof" : u.prof, "sex" : u.sex})
                pass
            logger.info("res: {}".format(json.dumps(res)))
            self.write(json.dumps(res))
        else:
            self.write(json.dumps(res))

    @coroutine
    def post(self):
        user = json_decode(self.request.body)
        logger.info("role_set_handler {}".format(user))

        user_saved = yield self.async_do(UserService.save_user, self.db, user)
        if user_saved and user_saved.userid:
            self.write("success")
        else:
            self.write("error")

    def filter_user(self, userobj):
        userdict = {}
        for u in userobj:
            key = '{0}_{1}'.format(u.useraccount, u.serverid)
            uobj = userdict.get(key)
            if uobj is not None:
                if uobj.level < u.level:
                    uobj.userid = u.userid
                    uobj.level = u.level
                    uobj.prof = u.prof
                    uobj.sex = u.sex
            else:
                userdict[key] = u
        return userdict