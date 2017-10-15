class Constant:

    def __init__(self):
        pass

    # hours
    TOKEN_EXPIRED_TIME = 24

    def get_token_expired_time(self):
        seconds = self.TOKEN_EXPIRED_TIME * 3600
        return seconds

