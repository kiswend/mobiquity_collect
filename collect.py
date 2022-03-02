import requests
import json

def collect(sendermsisdn, senderrole, senderwallet, receivermsisdn, receiverrole, receiverwallet, amount):
    url = "http://localhost:9999/jigsaw/serviceRequest/COLLECT"

    payload = json.dumps({
      "sender": {
        "idType": "mobileNumber",
        "productId": senderwallet,
        "idValue": sendermsisdn,
        "userRole": senderrole # CUSTOMER or CHANNEL
      },
      "receiver": {
        "idType": "mobileNumber",
        "productId": receiverwallet,
        "idValue": receivermsisdn,
        "userRole": receiverrole
      },
      "transactor": {
        "idType": "loginId",
        "productId": "12",
        "idValue": "netadminN",
        "password": "1qaz@WSX"
      },
      "serviceCode": "COLLECT",
      "transactionAmount": amount,
      "initiator": "transactor",
      "mfsTenantId": "mfsPrimaryTenant",
      "currency": "101",
      "bearerCode": "WEB"
    })
    headers = {
      'Content-Type': 'application/json'
    }
    
    print(payload)

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


TMER = '080322146'

from csv import DictReader
# open file in read mode
with open('list.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # row variable is a dictionary that represents a row in csv
        #print(row)
        #collect(row['MSISDN'], 'CUSTOMER', '12', TMER, 'CHANNEL', '12', row['AMOUNT'])
        #collect(TMER, 'CHANNEL', '12', row['MSISDN'], 'CUSTOMER', '17', row['AMOUNT'])
        collect(row['MSISDN'], 'CUSTOMER', '12', TMER, 'CHANNEL', '12', '2000')
        collect(TMER, 'CHANNEL', '12', row['MSISDN'], 'CUSTOMER', '17', '2000')