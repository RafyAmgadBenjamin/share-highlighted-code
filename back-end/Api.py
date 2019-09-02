from bottle import route, run, error, template, abort
from random import randint
import random
import redis
import json
from bottle import hook, request, response
from bottle import post, get, put, delete
import bottle
import base64

#  configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

# ####
# _allow_origin = '*'
# _allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
# _allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'


# @hook('after_request')
# def enable_cors():
#     '''Add headers to enable CORS'''

#     response.headers['Access-Control-Allow-Origin'] = _allow_origin
#     response.headers['Access-Control-Allow-Methods'] = _allow_methods
#     response.headers['Access-Control-Allow-Headers'] = _allow_headers
#     response.headers['content-type'] = 'application/json'
#     response.headers['Access-Control-Allow-Credentials'] = 'true'


# @route('/', method='OPTIONS')
# @route('/<path:path>', method='OPTIONS')
# #######################

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()

# the decorator
# app = bottle.app()
# def enable_cors(fn):
#     def _enable_cors(*args, **kwargs):
#         # set CORS headers
#         response.headers['Access-Control-Allow-Origin'] = '*'
#         response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
#         response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
#         if bottle.request.method != 'OPTIONS':
#             # actual request; reply with the actual response
#             return fn(*args, **kwargs)
#     return _enable_cors
# @post('/api/code/add-highlighted-code')
@app.route('/api/code/add-highlighted-code', method=['OPTIONS', 'GET', 'POST'])
@enable_cors
def add_Highlighted_code():
    """
    Add the highlighted code to the Redis database
    """
    if request.method == "POST":
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-type'] = 'application/json'
    # import ipdb; ipdb.set_trace()

    print("Data:")
    # data =  json.loads(request.json)
    print(request.json)
    data = request.json['code']
    print(data)
    encodedData = stringToBase64(data)
    print(encodedData)

    # print(data["code"])
    generatedVal = str(generate_random_no())
    # add to redis data base
    add_highlighted_code(radndomNo=generatedVal,
                         data=encodedData)
    # return generatedVal
    # print(generatedVal)
    # return generatedVal
    #response.headers['Content-Type'] = 'application/json'
    #response.headers['Cache-Control'] = 'no-cache'
    # return json.dumps({'tinyUrl': generatedVal})

# # API: used to get the original URL from the tiny URL and redirect to the original URL
# @route('/<tinyUrl>')
# def get_original_url(tinyUrl):
#     r = redis.StrictRedis(host=redis_host, port=redis_port,
#                           password=redis_password, decode_responses=True)
#     if r.get(tinyUrl) is not None:
#         response.status = 303
#         response.set_header('Location', r.get(tinyUrl))
#     else:
#         response.status = 404
#         abort(404, 'object already exists with that name')  # raise an 404 error

# # Handle the 404 error response
# @error(404)
# def error404(error):
#     return template('views/404.tpl', e=response.status_code)


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


def generate_random_no():

    random.seed(a=None)
    return randint(0, 1000000)  # randint is inclusive at both ends


def add_highlighted_code(radndomNo, data):
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port,
                              password=redis_password, decode_responses=True)

        # step 4: Set the data in Redis
        r.set(radndomNo, data)
        print("form redis" + r.get(radndomNo))

        # step 5: Retrieve the data message from Redis
    except Exception as e:
        print(e)


run(host='localhost', port=8080, debug=True)
