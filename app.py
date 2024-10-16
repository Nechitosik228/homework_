from datetime import datetime
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Header, Query



app=FastAPI()


@app.get("/user/{user_id}")
def user(user_id:int,
         timestamp:Annotated[datetime|None,Query()],
         x_client_version:Annotated[str|None,Header()]):
    return [f"Hello,{user_id}",
            {"time":timestamp,
             "client_version":x_client_version}]



if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8080)
