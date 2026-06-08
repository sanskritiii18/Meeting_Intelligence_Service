import uuid

from flask import g
from flask import request


def register_trace_middleware(app):

    @app.before_request
    def generate_trace_id():

        trace_id = request.headers.get(
            "X-Trace-Id"
        )

        if not trace_id:

            trace_id = str(
                uuid.uuid4()
            )

        g.trace_id = trace_id

        