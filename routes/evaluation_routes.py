from flask import Blueprint
from flask import jsonify

evaluation_bp = Blueprint(
    "evaluation",
    __name__,
    url_prefix="/api"
)

@evaluation_bp.route(
    "/evaluation",
    methods=["GET"]
)
def evaluation():

    return jsonify({
        "candidateName": "Sanskriti Verma",
        "email": "sanskritiverma.1807@gmail.com",
        "repositoryUrl": "https://github.com/sanskritiii18/Meeting_Intelligence_Service",
        "deployedUrl": "https://meeting-intelligence-service-pslx.onrender.com",
        "externalIntegration": "Discord Webhook",
        "features": [
            "Authentication",
            "Meeting CRUD",
            "AI Analysis",
            "Action Items",
            "Overdue Detection",
            "Reminder Scheduler"
        ]
    })