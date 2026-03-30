import uvicorn
from fastapi import FastAPI

app = FastAPI()

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

data = {"is_active": False}


@app.get("/")
def check():
    return {"is_active": data['is_active']}


@app.get("/on")
def set_on():
    data['is_active'] = True
    return {"is_active": data['is_active']}


@app.get("/off")
def set_off():
    data['is_active'] = False
    return {"is_active": data['is_active']}


@app.get("/switch")
def switch():
    data['is_active'] = not data['is_active']
    return {"is_active": data['is_active']}


if __name__ == "__main__":
    uvicorn.run(f'main:app', host='localhost', port=8000)


# https://github.com/espressif/arduino-esp32/blob/master/libraries/DNSServer/examples/CaptivePortal/CaptivePortal.ino