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


def parse_data(resulting_data,output_cur):
        data = json.loads(resulting_data)
        
        if data['success'] == False:
               return "error"
        else:
            # need to extract data in the rates array
            exchange_rate_array = data["rates"] 

            exchange_rate_ratio = exchange_rate_array[f"{output_cur}"]
            return exchange_rate_ratio



         
        