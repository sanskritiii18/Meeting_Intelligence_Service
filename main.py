from flask import Flask
from config import Config
from database import db
from routes.auth_routes import auth_bp
from routes.meeting_routes import meeting_bp
from routes.action_items_routes import action_item_bp
from routes.health_routes import health_bp
from routes.evaluation_routes import evaluation_bp
from scheduler.scheduler import start_scheduler
from middleware.trace import register_trace_middleware
from flask import request
from flask import g
from flasgger import Swagger
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()


app = Flask(__name__)
CORS(app)
Swagger(app)
app.config.from_object(Config)


db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(meeting_bp)
app.register_blueprint(action_item_bp)
app.register_blueprint(health_bp)
app.register_blueprint(evaluation_bp)

register_trace_middleware(app)

@app.after_request
def log_response(response):

    app.logger.info({
        "traceId": g.trace_id,
        "method": request.method,
        "path": request.path,
        "status": response.status_code
    })

    return response

with app.app_context():
    db.create_all()

start_scheduler(app)


if __name__ == "__main__":
    app.run(debug=True)