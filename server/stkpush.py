import json
import requests
from accessToken import data, MpesaAccessToken

def lipa_na_mpesa_online(data):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token,
               "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=data, headers=headers)
    response_dict = response.json()
    if "ResponseDescription" in response_dict:
        return response_dict["ResponseDescription"]
    elif "errorMessage" in response_dict:
        return response_dict["errorMessage"]
    else:
        return response_dict

lipa_na_mpesa_online(data)