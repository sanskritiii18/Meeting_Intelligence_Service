from marshmallow import (
    Schema,
    fields,
    validate
)


class ActionItemSchema(Schema):

    meeting_id = fields.Int(
        required=True
    )

    task = fields.Str(
        required=True
    )

    assignee = fields.Str(
        required=True
    )

    status = fields.Str(
        validate=validate.OneOf([
            "PENDING",
            "IN_PROGRESS",
            "COMPLETED"
        ])
    )