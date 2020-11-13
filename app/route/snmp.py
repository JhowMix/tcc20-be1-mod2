from model.address import Address
from datetime import date
import json, requests

from pprint import pprint
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
headers = {"Content-Type", "application/json"}

url = "http://10.10.0.3:3000/device/"
headers = {'content-type': 'application/json'}

@router.post("/snmp/check")
async def check_life(address: Address):
    raw = requests.post(url+'check', data=json.dumps(address.__dict__), headers=headers)
    return (raw.json())

@router.post("/snmp/device")
async def scan_device(address: Address):
    raw = requests.post(url+'scan', data=json.dumps(address.__dict__), headers=headers)
    return (raw.json())
