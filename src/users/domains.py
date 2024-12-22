from ninja import ModelSchema, Schema
from users.models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ["password"]


class LoginWithEmailRequestSchema(Schema):
    email: str
    redirect: str | None = ""
