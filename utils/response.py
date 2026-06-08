from flask import g


def success_response(
    data,
    status=200
):

    return {
        "traceId": g.trace_id,
        "success": True,
        "data": data
    }, status



def error_response(
    code,
    message,
    status
):

    return {
        "traceId": g.trace_id,
        "success": False,
        "error": {
            "code": code,
            "message": message
        }
    }, status