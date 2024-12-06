import threading
import uvicorn
import streamlit as st
from fastapi import FastAPI

# FastAPI app
api_app = FastAPI()

@api_app.get("/hello")
def say_hello():
    return {"message": "Hola desde FastAPI"}

# Thread para ejecutar FastAPI
def run_fastapi():
    uvicorn.run(api_app, host="127.0.0.1", port=8000)

# Ejecutar FastAPI en un hilo
threading.Thread(target=run_fastapi, daemon=True).start()

# Streamlit app
st.title("Integración de Streamlit y FastAPI")

if st.button("Llamar API de FastAPI"):
    import requests
    response = requests.get("http://127.0.0.1:8000/hello")
    st.write(response.json())
