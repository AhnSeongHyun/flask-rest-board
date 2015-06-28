# -*- coding:utf-8 -*-
__author__ = 'sh84.ahn@gmail.com'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

import datetime
Base = declarative_base()


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)

    title = Column(Text, nullable=False)
    contents = Column(Text, nullable=True)
    ctime = Column(DateTime, nullable=False)
    mtime = Column(DateTime, nullable=True)
    user_id = Column(Integer, nullable=False)

    def __init__(self, title, contents, ctime, mtime, user_id):
        self.title = title
        self.contents = contents
        self.ctime = ctime 
        self.mtime = mtime
        self.user_id = user_id

    def __str__(self):
        return str(self.__dict__)

    @property
    def to_dict(self):


        if self.mtime:
            mtime_value = self.mtime.strftime("%Y/%m/%d %H:%M:%S")
        else:
            mtime_value = self.mtime

        return {'id': self.id,
                'title': self.title,
                'contents': self.contents,
                'ctime': self.ctime.strftime("%Y/%m/%d %H:%M:%S"),
                'mtime': mtime_value,
                'user_id': self.user_id}


class Reply(Base):
    __tablename__ = 'reply'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, nullable=False)
    contents = Column(Text, nullable=True)
    ctime = Column(DateTime, nullable=False)
    mtime = Column(DateTime, nullable=True)
    parent_reply_id = Column(Integer, nullable=True)

    def __init__(self, article_id, contents, ctime, mtime, parent_reply_id=None):
        self.article_id = article_id
        self.contents = contents
        self.ctime = ctime
        self.mtime = mtime
        self.parent_reply_id = parent_reply_id

    def __str__(self):
        return str(self.__dict__)


    @property
    def to_dict(self):
        # TODO : IMPLEMENT
        pass


class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False)
    name = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, user, password, name):
        self.user = user
        self.password = password
        self.name = name

    def __str__(self):
        return str(self.__dict__)


    @property
    def to_dict(self):
        return {'user':self.user, 'name':self.name}



def create_database():
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///db.sqlite')
    Base.metadata.create_all(engine)


#create_database()

