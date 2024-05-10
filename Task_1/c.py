import requests

try:
    def get_country_data(alpha2_code):
        url = "https://restcountries.eu/rest/v2/all"
        timeout = (5, 5)
        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:
            return response.json()[0]
        else:
            print(f"Error: {response.status_code} while fetching data for {alpha2_code}")
            return None

    def find_largest_population(codes):
        max_population = -float("inf")
        largest_country = None

        for code in codes:
            country_data = get_country_data(code)
            if country_data:
                population = country_data.get("population", 0)
                if population > max_population:
                    max_population = population
                    largest_country = code

        if largest_country:
            country_data = get_country_data(largest_country)
            return f"{largest_country} ({country_data['population']} people)"
        else:
            return "No valid country codes provided or data unavailable"

    country_codes = input("Enter 3 comma-separated alpha2 codes (e.g. AF,AX,BE): ").upper().split(",")
    largest_populated = find_largest_population(country_codes)
    print(largest_populated)

except requests.exceptions.Timeout:
    print("Request timed out!")
