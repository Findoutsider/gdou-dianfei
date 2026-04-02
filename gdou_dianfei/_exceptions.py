class NoAuthException(Exception):
    """未登录"""


class AuthFailedException(Exception):
    """登录失败"""


class InvalidCredentialsException(Exception):
    """无效的登录凭据"""


class SystemBusyException(Exception):
    """系统繁忙"""
