class NoAuthException(Exception):
    """未登录"""
    pass

class AuthFailedException(Exception):
    """登录失败"""
    pass

class InvalidCredentialsException(Exception):
    """无效的登录凭据"""
    pass

class SystemBusyException(Exception):
    """系统繁忙"""
    pass