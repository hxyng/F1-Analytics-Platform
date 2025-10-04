from fastapi import FastAPI
import fastf1

app = FastAPI()

@app.get("/lap-times/{year}/{gp}/{driver}")
def get_lap_times(year: int, gp: str, driver: str):
    session = fastf1.get_session(year, gp, 'R')
    session.load()
    laps = session.laps.pick_driver(driver)
    return {"driver": driver, "laps": laps['LapTime'].astype(str).tolist()}