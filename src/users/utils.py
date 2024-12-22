from ninja_jwt.tokens import RefreshToken


def token_creator(token_model, user, serializer):
    return RefreshToken.for_user(user)
