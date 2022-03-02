import requests
import json
import concurrent.futures
import logging
import time
from csv import DictReader

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

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

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response.json()


TMER = '080322146'
AMOUNT = '1000'

def transfer(subscriber):
    data = collect(subscriber, 'CUSTOMER', '17', TMER, 'CHANNEL', '12', AMOUNT)
    if data['txnStatus']=='TS':
        logger.info("{}|{}|{}|{}".format(subscriber, data['status'], data['txnStatus'], data['transactionId']))
    else:
        logger.info("{}|{}|{}|{}|{}".format(subscriber, data['status'], data['txnStatus'], data['errors'][0]['code'], data['errors'][0]['message']))


def main(): 
    with open('list.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:





if __name__ =='__main__':
    main()
    
