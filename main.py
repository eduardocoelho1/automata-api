from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import dfa, dpda, dtm

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(dfa.router, prefix="/dfa", tags=["DFA"])
app.include_router(dpda.router, prefix="/dpda", tags=["DPDA"])
app.include_router(dtm.router, prefix="/dtm", tags=["DTM"])

@app.get("/")
def home():
    """
    Welcome message
    """
    return {"message": "Welcome to the Automata API"}
