"""
    DSC510
    Wk12
    Assignment 12.1
    Erin Howland
    06 Mar 2021
"""

import requests

# Create pretty Welcome
print("="*25 + '\n' + "="*8 + ' Welcome ' + "="*8 + '\n' + "="*25 + '\n')

print("For best results, please enter all prompts accurately.\n"
      "Note that state/province may be optional based on location.\n"
      "State is required for all US city searches for disambiguation (e.g. Denver IA vs Denver CO).\n")

# DRY principle
country_prompt = "Please enter two-letter country abbreviation (e.g. United Kingdom = UK): "
invalid_country_code = "Error: Invalid country code. Country code should follow ISO 3166 Alpha-2."
url_parts = ["http://api.openweathermap.org/data/2.5/weather?", "q=", "zip=", "&APPID=a4aa7c40ff1520761fed7bd2b7750ee2"]

# list of valid country codes (ISO 3166) from https://en.wikipedia.org/w/index.php?title=List_of_ISO_3166_country_codes&oldid=1008867175
# states, provinces, and city names are not validated in this way because there is so much variation - no worldwide naming conventions
country_codes = ['AS', 'GU', 'MP', 'PR', 'UM', 'VI', 'AI', 'BM', 'FK', 'GI', 'GS', 'IO', 'KY', 'MS', 'PN', 'SH', 'TC',
                 'VG', 'PS', 'VA', 'AF', 'AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD',
                 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CF',
                 'CG', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO',
                 'DZ', 'EC', 'EE', 'EG', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM',
                 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS',
                 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC',
                 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MM',
                 'MN', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR',
                 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA',
                 'SB', 'SC', 'SD', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SY', 'SZ',
                 'TD', 'TG', 'TH', 'TJ', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ',
                 'VC', 'VE', 'VN', 'VU', 'WS', 'YE', 'ZA', 'ZM', 'ZW']


# to allow user to define units of measurement; I have chosen limit to imperial and metric standards
# I have included wind speed as an output item, and there's no Kelvin equivalent for speed like there is for metric and imperial
def unit():
    unit_type = input("Imperial (I) or Metric (M)? ")
    while True:
        if unit_type.upper() == "I":
            return 'imperial', 'mph', '°F'
        elif unit_type.upper() == "M":
            return 'metric', 'm/s', '°C'
        else:
            print("Invalid unit of measure.\n" + unit_type)

# to allow searches by city name: take user input, access API, receive info in json format
def by_city():
    city = input("Please enter city name: ")
    # to check that an entry has been made for city
    if city == '':
        print("You did not enter a city.")
        return
    state = input("Please enter state or province name: ")
    # to check that an entry has been made for state
    if state == '':
        print("You did not enter a state.")
        return
    country = input(country_prompt)
    # to validate country input
    if country.upper() not in country_codes:
        print(invalid_country_code)
        return
    system, speed, temperature = unit()
    location = [city, state, country]
    separator = ','
    url = url_parts[0] + url_parts[1] + separator.join(location) + "&units=" + system + url_parts[-1]
    # try except block for checking URL response: HTTP errors and general exceptions (identical block reused in zip fn)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # not a 200
        print("Error: " + str(e))
        return
    except:
        # unspecified error
        print("Unspecified error. Are you connected to the Internet?")
        return
    # connection ok (200)
    weather_dictionary = response.json()
    output(weather_dictionary, speed, temperature)


# to allow searches by zip code: take user input, access API, receive info in json format
def by_zip():
    zip_code = input("Please enter zip code: ")
    # to check that an entry has been made for zip code
    if zip_code == '':
        print("You did not enter a zip code.")
        return
    country = input(country_prompt)
    # to validate country input
    if country.upper() not in country_codes:
        print(invalid_country_code)
        return
    system, speed, temperature = unit()
    location = [zip_code, country]
    separator = ','
    url = url_parts[0] + url_parts[2] + separator.join(location) + "&units=" + system + url_parts[-1]
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # not a 200
        print("Error: " + str(e))
        return
    except:
        # unspecified error
        print("Unspecified error. Are you connected to the Internet?")
        return
    # connection ok (200)
    weather_dictionary = response.json()
    output(weather_dictionary, speed, temperature)


# to define output information and create readable output
def output(weather_dictionary, speed_units, temperature_units):
    current_temp = weather_dictionary['main']['temp']
    max_temp = weather_dictionary['main']['temp_max']
    min_temp = weather_dictionary['main']['temp_min']
    wind = weather_dictionary['wind']['speed']
    latitude = weather_dictionary['coord']['lat']
    longitude = weather_dictionary['coord']['lon']
    humidity = weather_dictionary['main']['humidity']
    conditions = weather_dictionary['weather'][0]['description']
    print('Current Temperature : {} {}'.format(current_temp, temperature_units))
    print('High Temperature : {} {}'.format(max_temp, temperature_units))
    print('Low Temperature : {} {}'.format(min_temp, temperature_units))
    print('Wind Speed : {} {}'.format(wind, speed_units))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humidity))
    print('Description : {}'.format(conditions))


def main():
    # create loop for user to request weather as many times as they'd like
    while True:
        weather_search = input('To search weather conditions by zip code, enter 1.\n'
                               'To search weather conditions by city name, enter 2.\n'
                               'To exit search, enter 0.\n'
                               '> ')
        if weather_search == '1':
            print("Ok, we'll search for weather based on zip code.")
            by_zip()
        elif weather_search == '2':
            print("Ok, we'll search for weather based on city name.")
            by_city()
        elif weather_search == '0':
            print('Thanks for using weather search! Good bye.')
            break
        else:
            print("Invalid entry. Valid entries include:\n"
                  "1 to search by zip code\n"
                  "2 to search by city name\n"
                  "0 to exit search")


if __name__ == "__main__":
    main()
