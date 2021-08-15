from pyforbes.exceptions import DataUnavailableError
from pandas import DataFrame
from pyforbes.utils.constants import ORG, PERSON
from pyforbes.exceptions import DataUnavailableError


def response_to_df(response, category):
    """Extract the data from API and load into Pandas DataFrame.

    Args:
        response (requests.response): Result response from API request
        category (str): 'org' or 'person'

    Raises:
        DataUnavailableError: Requested data is not available.

    Returns:
        pandas.DataFrame: Returns DataFrame loaded with the API data.
    """
    json = response_to_json(response)
    if category == ORG:
        orgList = json.get("organizationList")
        data = orgList.get("organizationsLists")
    else:
        personList = json.get("personList")
        data = personList.get("personsLists")
    if not data:
        raise DataUnavailableError
    return DataFrame(data)


def response_to_json(response):
    """Return API Response as json

    Args:
        response (requests.response): response from API request

    Returns:
        dict: Forbes List data as json
    """
    return response.json()
