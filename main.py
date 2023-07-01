import requests

# BASE_URL = "https://irctc1.p.rapidapi.com/api/v1/"
BASE_URL = "https://irctc1.p.rapidapi.com/"
# HOST_URL = "irctc1.p.rapidapi.com"
HOST_URL = BASE_URL.replace('https://', '').replace('/', '')
API_DOCUMENTATION_URL = "https://rapidapi.com/IRCTCAPI/api/irctc1/"
API_KEY = "YOUR_API_KEY"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": HOST_URL
}


# =====================================================================================>

userSelection = int(input("What do you want to perform in Indian Railways?\n1. Search Stations\n2. Search Trains\n3. "
                          "Search the trains between stations\n4. Get live status of any train\n5. Get train "
                          "schedule\n6. Get PNR status\n7. Check seat availability\n8. Get Train classes\n9. Get fare "
                          "details.\n\n>>  "))


# =====================================================================================>

def search_stations():
    url = BASE_URL + "api/v1/" + "searchStation"
    station_code = input("Enter the station code - ")
    # station_code = "TATA"
    querystring = {"query": station_code}
    response = requests.get(url, headers=headers, params=querystring)
    for item in response.json()['data']:
        print("State Name - {}".format(item['state_name']))
    # return response.json()


def search_trains():
    url = BASE_URL + "api/v1/" + "searchTrain"
    train_no = input("Enter the station code - ")
    # train_no = "190"
    querystring = {"query": train_no}
    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


def search_trains_between_stations():
    url = BASE_URL + "api/v3/" + "trainBetweenStations"
    querystring = {"fromStationCode": "BVI", "toStationCode": "NDLS", "dateOfJourney": "<REQUIRED>"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def get_live_train_status():
    url = BASE_URL + "api/v1/" + "liveTrainStatus"
    querystring = {"trainNo": "19038", "startDay": "1"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def get_train_schedule():
    url = BASE_URL + "api/v1/" + "getTrainSchedule"
    querystring = {"trainNo": "12936"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def get_pnr_status():
    url = BASE_URL + "api/v3/" + "getPNRStatus"
    querystring = {"pnrNumber":"<REQUIRED>"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def check_seat_availability():
    url = BASE_URL + "api/v1/" + "checkSeatAvailability"
    querystring = {"classType": "2A", "fromStationCode": "ST", "quota": "GN", "toStationCode": "BVI",
                   "trainNo": "19038", "date": "2022-05-25"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def get_train_classes():
    url = BASE_URL + "api/v1/" + "getTrainClasses"
    querystring = {"trainNo": "19038"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


def get_fare():
    url = "https://irctc1.p.rapidapi.com/api/v2/getFare"
    querystring = {"trainNo": "19038", "fromStationCode": "ST", "toStationCode": "BVI"}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


# =====================================================================================>

data_dictionary = {
    1: "Search Stations",
    2: "Search Trains",
    3: "Search the trains between stations",
    4: "Get live status of any train",
    5: "Get train schedule",
    6: "Get PNR status",
    7: "Check seat availability",
    8: "Get Train classes",
    9: "Get fare"
}

method_dictionary = {
    1: search_stations,
    2: search_trains,
    3: search_trains_between_stations,
    4: get_live_train_status,
    5: get_train_schedule,
    6: get_pnr_status,
    7: check_seat_availability,
    8: get_train_classes,
    9: get_fare
}

# =====================================================================================>

print("User selected '{}' option.".format(data_dictionary.get(userSelection)))
method_dictionary.get(userSelection)

if userSelection in method_dictionary:
    print(method_dictionary[userSelection])
    method = method_dictionary[userSelection]
    method()


