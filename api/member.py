# -*- coding:utf-8 -*-
__author__ = 'sh84.ahn@gmail.com'

from plate_base import *
from db.dbmanager import OrmManager
from .api_response_data import APIResponse


@app.route('/api/member/auth',  methods=[POST])
def auth():
    logger.debug(request)
    try:
        user = request.form['user'] if 'user' in request.form else None
        password = request.form['password'] if 'password' in request.form else None

        if user and password:
            db_manager = OrmManager()
            member = db_manager.select_member_by_user(user)
            if member.password == password:
                return APIResponse(code=200, data=None).json
            else:
                return APIResponse(code=401, data=None).json

        else:
            return APIResponse(code=401, data=None).json
    except Exception as e:
        logger.exception(e)
        return APIResponse(code=500, data=None, msg=str(e)).json

@app.route('/api/member',  methods=[POST])
def register_member():
    logger.debug(request)

    try:
        user = request.form['user'] if 'user' in request.form else None
        password = request.form['password'] if 'password' in request.form else None
        name = request.form['name'] if 'name' in request.form else None

        if user and password:
            db_manager = OrmManager()
            member = db_manager.insert_member(user=user, password=password, name=name)
            if member:
                return APIResponse(code=200, data=None).json
        else:
            return APIResponse(code=401, data=None).json
    except Exception as e:
        logger.exception(e)
        return APIResponse(code=500, data=None, msg=str(e)).json
