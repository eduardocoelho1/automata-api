from fastapi import FastAPI
from routes import dfa, npda, mntm

app = FastAPI()

app.include_router(dfa.router, prefix="/dfa")
app.include_router(npda.router, prefix="/npda")
app.include_router(mntm.router, prefix="/mntm")

@app.get("/")
def home():
    return {"message": "Welcome to the Automata API"}
