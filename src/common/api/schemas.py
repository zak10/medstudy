from ninja import Schema


class BadRequestSchema(Schema):
    error_code: str
    error_message: str


class ErrorSchema(Schema):
    error_code: str
    error_message: str


class NotFoundSchema(Schema):
    error_code: str = "E_NOT_FOUND"
    error_message: str = "Not found."
