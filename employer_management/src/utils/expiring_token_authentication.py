from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from django.core import exceptions
from datetime import datetime, timedelta
import pytz

from ..infrastructures import ApiCustomException
from ..constant import ErrorDefine
from ..constant import Constant


class ExpiringTokenAuthentication(TokenAuthentication):
    constant = Constant()

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            raise ApiCustomException(ErrorDefine.INVALID_TOKEN)

        if not token.user.is_active:
            raise ApiCustomException(ErrorDefine.USER_INACTIVE)

        # This is required for the time comparison
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - timedelta(seconds=self.constant.get_token_expired_time()):
            raise ApiCustomException(ErrorDefine.TOKEN_EXPIRED)

        return token.user, token
