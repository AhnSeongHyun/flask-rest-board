# -*- coding:utf-8 -*-
__author__ = 'sh84.ahn@gmail.com'

from board_base import *
from db.dbmanager import OrmManager
from api_response_data import APIResponse


@app.route('/api/articles',  methods=[GET])
def get_article_list():

    try:
        start_index = request.args.get("start_index", 0)
        paging_size = request.args.get("paging_size", 30)
        keyword = request.args.get("keyword", None)

        db_manager = OrmManager()
        result = db_manager.select_articles(start_index=start_index,
                                            paging_size=paging_size,
                                            keyword=keyword)

        return APIResponse(code=200, data=result).json

    except Exception as e:
        return APIResponse(code=500, data=None, msg=e).json



@app.route('/api/articles',  methods=[POST])
def write_article():
    try:
        db_manager = OrmManager()
        article_id = db_manager.insert_article(request.form)
        return APIResponse(code=200, data={'article_id': article_id}).json

    except Exception as e:
        return APIResponse(code=500, data=None, msg=e).json


@app.route('/api/articles/<int:id>',  methods=[DELETE])
def delete_article(id):
    try:
        db_manager = OrmManager()
        db_manager.delete_article(id)
        return APIResponse(code=200, data=None).json
    except Exception as e:
        return APIResponse(code=500, data=None, msg=e).json


@app.route('/api/articles/<int:id>',  methods=[PUT])
def modify_article(id):

    try:
        db_manager = OrmManager()
        result = db_manager.update_article(id, request.form)
        return APIResponse(code=200, data=result).json
    except Exception as e:
        return APIResponse(code=500, data=None, msg=e).json


@app.route('/api/articles/<int:id>',  methods=[GET])
def get_article(id):

    try:
        db_manager = OrmManager()
        result = db_manager.select_by_id(id)
        return APIResponse(code=200, data=result).json
    except Exception as e:
        return APIResponse(code=500, data=None, msg=e).json



