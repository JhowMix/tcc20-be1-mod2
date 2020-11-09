from fastapi import APIRouter
from typing import Optional
from bson.json_util import dumps, loads
from operator import is_not
from functools import partial

from setting import database


client = database.client['devices']
router = APIRouter()


@router.get("/device/dashboard/throughput")
async def read_router_dashboard():
    return loads(dumps(client.find({'status': 'On'}, {'_id': False})))


@router.get("/device/all")
async def read_router_list():
    return loads(dumps(client.find({}, {'_id': False})))


@router.get("/device/{engine_id}/port/chart/all")
async def read_interfaces(engine_id: str, q: Optional[str] = None):
    raw = client.find({'engineId': engine_id}, {'_id': False, 'ports': True})
    raw[0]['ports'] = list(filter(lambda port: port['state'] == 1,  raw[0]['ports']))

    result = list(map(lambda port: {
        'id': port['index'], 
        'name': port['name'],
        'value': port['throughput']}, raw[0]['ports']))
    
    for i in result:
        i['value'] = round(i['value'], 1)

    return loads(dumps(result))

