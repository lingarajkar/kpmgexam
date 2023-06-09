import requests
import json

def get_aws_metadata():
    url = 'http://169.254.169.254/latest/meta-data/'
    response = requests.get(url)
    data = {}
    
    if response.status_code == 200:
        metadata_endpoints = response.text.split('\n')
        for endpoint in metadata_endpoints:
            endpoint_url = url + endpoint
            endpoint_response = requests.get(endpoint_url)
            
            if endpoint_response.status_code == 200:
                endpoint_data = endpoint_response.text
                data[endpoint] = endpoint_data
    
    return data

metadata = get_aws_metadata()
json_output = json.dumps(metadata, indent=4)
print(json_output)