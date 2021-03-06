# JSON responses which are following JSend
# https://github.com/omniti-labs/jsend
from flask import jsonify, make_response
from .status import SUCCESS_OK, ERROR_BAD_REQUEST


def success(data, status=SUCCESS_OK):
    return make_response(
        jsonify({
            "status": "success",
            "data": data
        }), status)


def error(msg, status=ERROR_BAD_REQUEST):
    print (msg)
    return make_response(
        jsonify({
            "status": "error",
            "message": msg
        }), status)

"""
# might be deprecated
def fail(data):
    return jsonify({
        "status": "fail",
        "data": data
    })
"""
