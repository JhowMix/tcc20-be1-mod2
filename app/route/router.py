from bson.json_util import dumps
from fastapi import APIRouter

from app.setting import database

from bson.json_util import dumps, loads


client = database.client['devices']
router = APIRouter()


@router.get("/devices")
async def read_router():
    return loads(dumps(client.find({}, {'_id': False})))

