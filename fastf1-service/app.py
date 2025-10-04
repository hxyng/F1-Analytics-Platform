from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import fastf1

app = FastAPI()

origins = [
        "http://localhost:3000"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,  # Allow cookies, authorization headers, etc.
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],  # Allow all headers
)

@app.get("/lap-times/{year}/{gp}/{driver}")
def get_lap_times(year: int, gp: str, driver: str):
    session = fastf1.get_session(year, gp, 'R')
    session.load()
    laps = session.laps.pick_driver(driver)
    return {"driver": driver, "laps": laps['LapTime'].astype(str).tolist()}