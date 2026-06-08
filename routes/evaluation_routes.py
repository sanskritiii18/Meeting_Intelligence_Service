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
        "email": "YOUR_EMAIL",
        "repositoryUrl": "YOUR_GITHUB_URL",
        "deployedUrl": "YOUR_DEPLOYED_URL",
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