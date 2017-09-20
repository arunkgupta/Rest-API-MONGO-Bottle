import json
from bottle import route, run, request, abort
from pymongo import MongoClient

connection = MongoClient('10.5.3.178', 27017)
db = connection.mydatabase


@route('/documents', method='PUT')
def put_document():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except Exception as e:
        abort(400, str(e))


@route('/documents/:id', method='GET')
def get_document(id):
    entity = db['documents'].find_one({'_id': id})
    if not entity:
        abort(400, 'No document with id %s' % id)
    return entity


run(host='localhost', port=8080)

