import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key = ' CQpTmd4soNAeYxYAI68y6oLa0ycCCfsemHeP2NB42ExuwQSP'
    consumer_secret = 'TTClArMdw24tV8hyZDxvmHinGGWausrZo1j9cAMvfUXEFDrr5aohFU7SlFkUWfLQ'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    validated_mpesa_access_token = None
    try:
        r = requests.get(MpesaC2bCredential.api_URL,
                         auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
        print(f"Status Code: {r.status_code}")
        print(f"Response Text: {r.text}")

        r.raise_for_status() 
        try:
            mpesa_access_token = r.json()
            formated_res = json.dumps(mpesa_access_token, indent=4)
            validated_mpesa_access_token = mpesa_access_token['access_token']
            print(formated_res)
        except json.JSONDecodeError:
            print("Error decoding JSON. Response content is not valid JSON.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')