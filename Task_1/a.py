import requests

try:
    timeout = (5, 5)
    response = requests.get("https://restcountries.eu/rest/v2/all", timeout=timeout)

    if response.status_code == 200:
        countries = response.json()

except requests.exceptions.Timeout:
    print("Request timed out!")
