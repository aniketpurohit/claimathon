from typing import Union
import os
from fastapi import FastAPI
import xmltodict

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/vehicle/{item_id}")
def read_item(item_id: Union[str, None] = None):
    if item_id != None:
        path = os.getcwd() + "\\data\\" + item_id +".xml"
        if os.path.exists(path):
            with open(path, 'r') as xml_data:
                data = xmltodict.parse(xml_data.read())
        else:
            return {"item_id" : "Auth Error"}
    else:
        return {"itme_id": "No car found"}

    return {item_id: data}
