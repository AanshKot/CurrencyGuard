import requests
import json
from flask import flash

def fixer_call(output_cur,input_cur):
        url = f"https://api.apilayer.com/fixer/latest?symbols={output_cur}&base={input_cur}"

        payload = {}
        headers= {
        "apikey": "GAgukOHFv2D7nd1NxwWWXuekB5o7DnLR"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text

        return result


def parse_data(resulting_data):
        data = json.load(resulting_data)

        if data['success'] == False:
               flash("Currency Conversion failed, please check inputted currencies",category="error")
               

         
        