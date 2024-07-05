import requests
import datetime

def get_driving_time(api_key, origin, destination, departure_time=None):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    
    # Parameters
    params = {
        'origins': origin,
        'destinations': destination,
        'key': api_key,
        'mode': 'driving'
    }
    
    if departure_time:
        params['departure_time'] = departure_time
    
    # Making the request
    response = requests.get(base_url, params=params)
    # print("Request URL:", response.url)
    
    # Parsing the response
    if response.status_code == 200:
        data = response.json()
        #print("Response JSON:", data)
        if data['status'] == 'OK':
            result = data['rows'][0]['elements'][0]
            if result['status'] == 'OK':
                duration = result['duration_in_traffic']['text'] if 'duration_in_traffic' in result else result['duration']['text']
                return duration
            else:
                return f"Error: {result['status']}"
        else:
            return f"Error: {data['status']}"
    else:
        return f"HTTP Error: {response.status_code}"

# Example usage



api_key = 'AIzaSyBEPK0j_w8O5TABTnV62Cjv-IpJ3ISDqrk'

# origin = input("Enter address: ")

addresses = [
    "14890 Henry St, Corona, CA 92880",
    "20750 Earlgate St, Walnut, CA 91789",
    "2997 Pembroke Cir, Corona, CA 92879",
    "480 Bristol Way, Corona, CA 92879",
    "246 W Cork Tree Dr, Orange, CA 92865",
    "13081 Detroit Ct Chino, CA 91710",
    "1454 Valeview Dr, Diamond Bar, CA 91765",
    "24150 Willow Creek Rd, Diamond Bar, CA 91765",
    "16310 McGill Rd La Mirada, CA 90638",
    "18568 Nottingham Ln Rowland Heights, CA 91748",
    "14728 Rick Ln, Corona, CA 92880",
    "13865 Peach Grove Ln, Corona, CA 92880",
    "7415 Crescent Ave Buena Park, CA 90620",
    "10912 Linnell Ave, Garden Grove, CA 92843",
    "1039 N Liberty Ln Anaheim, CA 92805",
    "5152 Vallecito Ave Westminster, CA 92683",
    "1075 Via Blairo, Corona, CA 92879",
    "14245 Sapphire Hill Ln, Chino Hills, CA 91709",
    "5530 Vía Vallarta Yorba Linda, CA 92887",
    "13860 Elgers St Cerritos, CA 90703",
    "1856 Conejo Ln, Fullerton, CA 9283",
    "8784 E Banner Ridge Dr Anaheim, CA 92808",
    "15063 Avenida Compadres, Chino Hills, CA 91709",
    "10912 Linnell Ave, Garden Grove, CA 92843",
    "20665 E Fuero Dr Walnut, CA 91789",
    "7801 Norann Cir, La Palma, CA 90623",
    "7801 Norann Cir, La Palma, CA 90623",
    "19 Sorbonne St Westminster, CA 92683",
    "2619 Mill Ln Fullerton, CA 92831",
    "2017 W Sycamore Ave Orange, CA 92868",
    "1580 W Chanticleer Rd Anaheim, CA 92802",
    "9471 Cherwell Ct, Cypress, CA 90630",
    "45 Proclamation Way Irvine, CA 92602"
]

destinationMikey = '3801 W Temple Ave, Pomona, CA'
destinationJosh = '670 Spectrum Center Dr, Irvine, CA'
destinationCova = '5675 E La Palma Ave Suite 185, Anaheim, CA'
destinationJustin = '2767 E Imperial Hwy, Brea, CA'

totals = []

for origin in addresses:
    
    print("Address:", origin)

    now = datetime.datetime.now()
    departure_time = int((datetime.datetime(now.year, now.month, now.day+1, 9, 0).timestamp()))

    driving_time_mikey = get_driving_time(api_key, origin, destinationMikey, departure_time)
    print(f"Mikey driving time: {driving_time_mikey}")
    driving_time_josh = get_driving_time(api_key, origin, destinationJosh, departure_time)
    print(f"Josh driving time: {driving_time_josh}")
    driving_time_cova = get_driving_time(api_key, origin, destinationCova, departure_time)
    print(f"Cova driving time: {driving_time_cova}")
    driving_time_justin = get_driving_time(api_key, origin, destinationJustin, departure_time)
    print(f"Justin driving time: {driving_time_justin}")

    total = int(driving_time_mikey.split()[0]) + int(driving_time_josh.split()[0]) + int(driving_time_cova.split()[0]) + int(driving_time_justin.split()[0])
    print("Total time:", total, " min\n\n")

