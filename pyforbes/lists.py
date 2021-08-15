from json import JSONDecodeError
from pyforbes.exceptions import ListNotSupportedError
from pyforbes.utils.lists_config import ALL_LISTS
from pyforbes.utils.constants import ORG_LIST_URL
from pyforbes.utils.constants import PERSON_LIST_URL
from pyforbes.utils.constants import ORG, CATEGORY

from datetime import date
from pyforbes.utils.requests import ForbesRequest
from pyforbes import utils


class ForbesList(object):
    def __init__(self):
        """
        Create ForbesList Object
        """
        self.request = ForbesRequest()

    def _resolve_and_request(self, list_name, category, year):
        """Resolves to appropriate API URL and fetches Forbes List data.

        Args:
            list_name (str): name of the list
            category (str): 'org' or 'person'
            year (int): Year to fetch the data for

        Returns:
            requests.response: returns the result after making api call.
        """
        if category == ORG:
            url = ORG_LIST_URL.format(list_name, year)
        else:
            url = PERSON_LIST_URL.format(list_name, year)
        response = self.request.get(url)
        return response

    def _get_category(self, list_name):
        """Helper method to get the category of the given list name

        Args:
            list_name (str): name of the Forbes List

        Returns:
            str: returns category of the list. 'org' or 'person'
        """
        list_info = ALL_LISTS.get(list_name)
        if not list_info:
            raise ListNotSupportedError(list_name)
        return list_info.get(CATEGORY)

    def get_response(self, list_name, year=date.today().year):
        """Get Forbes List for the specified year

        Args:
            list_name (str): name of the Forbes List
            year (int, optional): Year to fetch the list. Defaults to current year.

        Raises:
            ListNotSupportedError: Specified list is not supported by PyForbes package.

        Returns:
            requests.response: returns response object for the API call.
        """
        assert year <= date.today().year, "Year cannot be in the future"
        category = self._get_category(list_name)
        return self._resolve_and_request(list_name, category, year)

    def get_df(self, list_name, year=date.today().year):
        """Get Forbes List as a DataFrame

        Args:
            list_name (str): Name of the Forbes List
            year (int, optional): Specify the year to fetch the data for. Defaults to the current year.

        Returns:
            pandas.DataFrame: returns ForbesList data as pandas DataFrame.
        """
        category = self._get_category(list_name)
        response = self.get_response(list_name, year)

        return utils.response_to_df(response, category)

    def get_json(self, list_name, year=date.today().year):
        """Get Forbes List data as JSON

        Args:
            list_name (str): Name of the Forbes List
            year (int, optional): Specify the year to fetch the data. Defaults to date.today().year.

        Returns:
            json: returns ForbesList data as json object.
        """
        response = self.get_response(list_name, year)
        return utils.response_to_json(response)
