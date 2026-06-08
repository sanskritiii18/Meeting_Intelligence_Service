from flask import jsonify
from flask import g
from main import app


@app.errorhandler(Exception)
def handle_exception(error):

    return jsonify({
        "traceId": getattr(
            g,
            "trace_id",
            None
        ),
        "success": False,
        "error": {
            "code": "INTERNAL_SERVER_ERROR",
            "message": str(error)
        }
    }), 500
