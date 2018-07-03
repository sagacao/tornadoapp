# coding=utf-8
from model.models import User


class UserService(object):

    @staticmethod
    def get_user(db_session, useraccount):
        return db_session.query(User).filter(User.useraccount == useraccount).all()

    @staticmethod
    def update_user_info(db_session, username, user):
        current_user = UserService.get_user(db_session, username)
        if current_user:
            if "useraccount" in user:
                current_user.useraccount = user['useraccount']
            if "email" in user:
                current_user.email = user['email']
            db_session.commit()
            return current_user
        else:
            return None

    @staticmethod
    def get_count(db_session):
        return db_session.query(User).count()

    @staticmethod
    def save_user(db_session, user):
        user_to_save = User(
            userid=user['roleid'],
            useraccount=user['userid'],
            serverid=user['serverid'],
            level=user['lev'],
            prof=user['prof'],
            sex=user['sex'],
        )
        db_session.merge(user_to_save)
        db_session.commit()
        return user_to_save