# Base URLs
BASE_URL = "https://www.forbes.com/forbesapi/"
PERSON_BASE_URL = f"{BASE_URL}/person/"
ORG_BASE_URL = f"{BASE_URL}/org"

# List URLs
ORG_LIST_URL = ORG_BASE_URL + "/{}/{}/position/true.json"  # .format(uri, year)
PERSON_LIST_URL = (
    PERSON_BASE_URL + "/{}/{}/position/true.json"
)  # .format(category-uri, year)

# Individual Data endpoints URLs
PERSON_DATA_URL = PERSON_BASE_URL + "/{}.json"  # .format(person-uri)
ORG_DATA_URL = ORG_BASE_URL + "/{}.json"  # .format(org-uri)

# String Constants
ORG = "org"
PERSON = "person"
CATEGORY = "category"
