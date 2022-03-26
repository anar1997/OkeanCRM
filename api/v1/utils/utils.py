import logging, logging.config
import sys
import  jwt
from django.conf import settings
import numpy as np


def jwt_decode_handler(token):
    """
    JWT token create eden funksiya
    """
    secret_key = settings.SECRET_KEY
    
    return jwt.decode(
        token,
        secret_key,
        audience=settings.SIMPLE_JWT.get("AUDIENCE"),
        issuer=settings.SIMPLE_JWT.get("ISSUER"),
        algorithms=[settings.SIMPLE_JWT.get("ALGORITHM")]
    )

def work_day_creater(start_date: str, expiration_date: str):
    """
    İşçilərin iş və tətil günlərini create edən funksiya
    """

    return np.arange(start_date, expiration_date, dtype='datetime64[D]')