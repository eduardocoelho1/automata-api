from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import dfa, dpda, dtm

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(dfa.router, prefix="/dfa")
app.include_router(dpda.router, prefix="/dpda")
app.include_router(dtm.router, prefix="/dtm")

@app.get("/")
def home():
    return {"message": "Welcome to the Automata API"}
