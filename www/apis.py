# -*- coding: utf-8 -*-


class APIError(Exception):
    """包含错误（必需），数据（可选）和消息（可选）的基本APIError。"""

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """指示输入值有错误或无效。数据指定输入表单的错误字段。"""

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    """指示资源未找到。数据指定资源名称。"""

    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    """表示api没有权限。"""

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
