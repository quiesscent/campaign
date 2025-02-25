# credentials.py
import base64
import requests
from requests.auth import HTTPBasicAuth
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

class MpesaAccessToken:
    @staticmethod
    def get_access_token():
        # Daraja Sandbox credentials
        consumer_key = 'aZPo66U3mqRyFIevpbhOYNDAy2JB0fvGeJitOG2RIe8IkzSs'
        consumer_secret = 'p7ev4dnWB6XOs8QRQPuGpQWpgvbkvGAvrTy3nAMUhUk27mpMAL7Wlns69f2qEn2I'
        api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        json_response = response.json()
        return json_response['access_token']

    @classmethod
    def validated_mpesa_access_token(cls):
        return cls.get_access_token()

class LipanaMpesaPpassword:
    # Daraja Sandbox credentials
    Business_short_code = 174379
    Shortcode_password = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    @staticmethod
    def get_lipa_time():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @property
    def decode_password(self):
        lipa_time = self.get_lipa_time()
        password = f"{self.Business_short_code}{self.Shortcode_password}{lipa_time}"
        return base64.b64encode(password.encode()).decode()
