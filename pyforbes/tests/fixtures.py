import pytest
from pyforbes.utils.lists_config import ALL_LISTS, ORG_LISTS, PERSON_LISTS
from pyforbes import ForbesList
import random

short_test_limit = 10

forbes_list = ForbesList()
all_list_names = [key for key in ALL_LISTS.keys()]
person_list_names = [key for key in PERSON_LISTS.keys()]
org_list_names = [key for key in ORG_LISTS.keys()]

random.shuffle(person_list_names)
random.shuffle(person_list_names)
random.shuffle(org_list_names)

all_list_names_years = [(key, 2017) for key in ALL_LISTS.keys()][
    :short_test_limit
]
person_list_names_years = [(key, 2017) for key in PERSON_LISTS.keys()][
    :short_test_limit
]
org_list_names_years = [(key, 2017) for key in ORG_LISTS.keys()][
    :short_test_limit
]
