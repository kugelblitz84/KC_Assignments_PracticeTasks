import os

import jwt

from project.core.entities.entity_models import Session


def verify_token(session: Session):
    jwt_secret = os.environ.get("JWT_SECRET")
    if not jwt_secret or not session.username or not session.token:
        return False
    try:
        payload = jwt.decode(session.token, jwt_secret, algorithms=["HS256"], options={"require": ["sub", "iat", "exp"]})
    except jwt.InvalidTokenError:
        return False
    return payload.get("sub") == session.username
