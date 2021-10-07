import requests
BASE_URL = "https://www.bungie.net/Platform"
HEADERS = {"X-API-Key": 'X-API-Key here'}


def get_information(endpint, base_url=BASE_URL, headers=HEADERS):
    r = requests.get(
        base_url + endpint, headers=headers)
    return r.json()

# /Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/
# inventoryItem = get_information(
#     f"/Destiny/{2}/Account/{destinyMembershipId}/Character/{37744}/Inventory/")


print(get_information(
    f"/Destiny/2/Stats/GetMembershipIdByDisplayName//"))

# print(inventoryItem['Response']['data']['inventoryItem']['itemName'])
# Gjallarhorn
# waiting to change by bungie name)))))))))))))))))))))))))))))))))
