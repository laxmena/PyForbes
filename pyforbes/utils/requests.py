import requests

__author__ = "laxmena"
__license__ = "MIT"


class ForbesRequest(object):
    """
    Private Class wrapper for Forbes API Requests.
    """

    def __init__(self, headers=None):
        if not headers:
            self.headers = {}

    def process_request(self, method, url, data=None):
        """Make requests to Forbes API by appending required headers.

        Args:
            method (str): supported methods - get, post, delete, put
            url (str): API URL
            data (dict, optional): additional data to be passed to request.
                Defaults to None.

        Returns:
            [type]: [description]
        """
        request_method = getattr(requests, method)
        return request_method(url, json=data, headers=self.headers)

    def get(self, url, data=None):
        """send GET request to Forbes API

        Args:
            url (str): API URL
            data (dict, optional): Parameters to be passed to API. Defaults to None.

        Returns:
            requests.Response: Returns response for the given API
        """
        return self.process_request("get", url, data)
