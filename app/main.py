from fastapi import FastAPI

app = FastAPI()

@app.get('/api/')
def home():
    return "Hola mundo"