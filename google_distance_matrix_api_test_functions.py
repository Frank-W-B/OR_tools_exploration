import os
import json
from urllib.request import urlopen


data = dict()
data['addresses'] = ['3610+Hacks+Cross+Rd+Memphis+TN', # depot
                     '1921+Elvis+Presley+Blvd+Memphis+TN',
                     '149+Union+Avenue+Memphis+TN',
                     '1034+Audubon+Drive+Memphis+TN',
                     '1532+Madison+Ave+Memphis+TN',
                     '706+Union+Ave+Memphis+TN',
                     '3641+Central+Ave+Memphis+TN',
                     '926+E+McLemore+Ave+Memphis+TN',
                     '4339+Park+Ave+Memphis+TN',
                     '600+Goodwyn+St+Memphis+TN',
                     '2000+North+Pkwy+Memphis+TN',
                     '262+Danny+Thomas+Pl+Memphis+TN',
                     '125+N+Front+St+Memphis+TN',
                     '5959+Park+Ave+Memphis+TN',
                     '814+Scott+St+Memphis+TN',
                     '1005+Tillman+St+Memphis+TN'
                    ]

def create_distance_matrix(data):
    addresses = data["addresses"]
    API_key = os.environ["GOOGLE_DISTANCE_MATRIX_API_KEY"]


    # Distance Matrix API only accepts 100 elements per request, so must get data with multiple requests
    max_elements = 100
    num_addresses = len(addresses) # 16 in this example
    # Maximum number of rows that can be computed per request (16 addresses per row, 100/16 = 6.25, 6)
    max_rows = max_elements // num_addresses
    # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example, 2 * 6 + 4 = 16)
    q, r = divmod(num_addresses, max_rows)  # q = 16 / 6 = 2, r = 16-12 = 4
    print(f"q: {q}, r: {r}")
    dest_addresses = addresses  # request will go to each address
    distance_matrix = []
    # Send q requests, returning max_rows per request.
    for i in range(1):
        origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]  # subset origin addresses
        response = send_request(origin_addresses, dest_addresses, API_key)
        distance_matrix += build_distance_matrix(response)

    #if r > 0:
    #    origin_addresses = addresses[q * max_rows: q * max_rows + 4]
    #    response = send_request(origin_addresses, dest_addresses, API_key)
    #    distance_matrix += build_distance_matrix(response)

    return distance_matrix       

def send_request(origin_addresses, dest_addresses, API_key):
    """ Build and send request for the origin and destination addresses."""
    
    def build_address_str(addresses):
        # Build a pipe-separated string of addresses
        address_str = ''
        for i in range(len(addresses) - 1):
            address_str += addresses[i] + '|'
        address_str += addresses[-1]
        return address_str        

    request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    origin_address_str = build_address_str(origin_addresses)
    print(f"\nOrigin addresses: {origin_address_str}")
    dest_address_str = build_address_str(dest_addresses)
    print(f"\nDestination addresses: {dest_address_str}")
    request = request + '&origins=' + origin_address_str + '&destinations=' + \
                        dest_address_str + '&key=' + API_key
    print(f"\nRequest: {request}")
    jsonResult = urlopen(request).read()
    breakpoint()
    response = json.loads(jsonResult)
    return response

def build_distance_matrix(response):
    """Note distance (instead of duration) is asked for in the call below"""
    distance_matrix = []
    for row in response['rows']:
        row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
        distance_matrix.append(row_list)
    return distance_matrix





distance_matrix = create_distance_matrix(data)
print(f"Distance matrix: {distance_matrix}")
