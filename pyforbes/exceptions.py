class PyForbesError(Exception):
    """Base class for PyForbes errors."""


class ListNotSupportedError(PyForbesError):
    def __init__(self, list_name, message=None):
        if not message:
            message = """{} List is currently not supported by PyForbes package.
                    Find available lists by executing lists.get_available_lists() method.
                    Try lists.get_list_from_uri() method"""
        super().__init__(message)


class DataUnavailableError(PyForbesError):
    def __init__(self):
        message = """Empty Dataset recieved. \
            Requested data is unavailable for the specified year."""
        super().__init__(message)
