from pyforbes.tests.fixtures import (
    all_list_names,
    forbes_list,
    all_list_names_years,
)
from pyforbes.utils.constants import PERSON, ORG
import pytest
from datetime import date


@pytest.mark.parametrize("list_name", all_list_names)
def test_get_response(list_name):
    response = forbes_list.get_response(list_name)
    assert response.status_code == 200


@pytest.mark.parametrize("list_name, year", all_list_names_years)
def test_get_list_resposne_with_year(list_name, year):
    response = forbes_list.get_response(list_name, year)
    assert response.status_code == 200


# Test JSON
@pytest.mark.parametrize("list_name, year", all_list_names_years)
def test_get_json(list_name, year):
    category = forbes_list._get_category(list_name)
    json = forbes_list.get_json(list_name, year)
    if category == ORG:
        assert json.__contains__("organizationList")
    elif category == PERSON:
        assert json.__contains__("personList")


# Test DataFrame
@pytest.mark.parametrize("list_name, year", all_list_names_years)
def test_get_df(list_name, year):
    category = forbes_list._get_category(list_name)
    df = forbes_list.get_df(list_name, year)
    assert not df.empty


# Fail Test Case
@pytest.mark.xfail
@pytest.mark.parametrize(
    "list_name, year", [(all_list_names[0], date.today().year + 1)]
)
def test_get_list_with_year(list_name, year):
    response = forbes_list.get(list_name, year)
    assert response.status_code == 200
