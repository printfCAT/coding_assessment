import requests

try:
    timeout = (5, 5)
    response = requests.get("https://restcountries.eu/rest/v2/all", timeout=timeout)

    if response.status_code == 200:
        countries = response.json()

        for country in countries:
            name = country["name"]["common"]
            alpha2_code = country["cca2"]
            flag = country["flags"]["png"]
            print(f"Name: {name}, Alpha2 Code: {alpha2_code}, Flag: {flag}")

    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.Timeout:
    print("Request timed out!")
