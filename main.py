from fastapi import FastAPI
from routes import nfa

app = FastAPI()

app.include_router(nfa.router, prefix="/nfa")

@app.get("/")
def home():
    return {"message": "Welcome to the Automata API"}
