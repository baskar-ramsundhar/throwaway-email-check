import requests
import hashlib
import json

CONFIG_FILE = "config.json"

def load_config(config_filepath = CONFIG_FILE):
    # Loading config from a JSON file.
    with open(config_filepath) as f:
        config = json.load(f)
    return config

def is_throwaway(email, api_url):
    # Creating a get url that would contain both api_url + email
    # using requests library to return api responses.
    url = api_url + email
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        isDisposable = data.get('isDisposable', False)
        return isDisposable
    except requests.exceptions.RequestException as e:
        #print(f"Error checking email {email}: {e}")
        return e

def hash_email(email):
    #Using the hashlib library to encode the email to hexadecimal.
    #In this scenario, the downstream stakeholders are internal teams so the only issue that would arise would be related to data governance and security mandates.
    #The drawbacks of having an SHA256 encoded email would result in further decoding work for the internal campaign teams who use the final transformed dataset.
    return hashlib.sha256(email.encode()).hexdigest()