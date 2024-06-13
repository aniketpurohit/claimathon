from typing import Union
from fastapi import FastAPI
import xmltodict
import logging
import requests

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/vehicle/{vehicle_id}")
async def read_item(vehicle_id: Union[str, None] = None):
    if vehicle_id != None:
        logging.info(f"vehicle_id received {vehicle_id}")
        path = r"https://azurefunctionstest9197.blob.core.windows.net/data/"+ vehicle_id +".xml"
        xml_data = requests.get(path)
        if xml_data.status_code == 200:
            logging.info(f"vehicle found : {vehicle_id}")
            data = xmltodict.parse(xml_data.text)
        elif xml_data.status_code ==404:
            logging.info("File not found")
            return {"Error":"File not found", "status code": 404}
        else:

            return {"Error" :xml_data.text , "status code": xml_data.status_code}
    else:
        return {"paramter": "parameter not found"}

    return {vehicle_id: data}
