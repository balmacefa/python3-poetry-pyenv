from fastapi import FastAPI
from pywebio.platform.fastapi import webio_routes
from pywebio.output import put_text
from pywebio.input import input
from app.internal_tool import internal_tool_pdf_reader

app = FastAPI()

# Define tus funciones de PyWebIO
def home():
    put_text("¡Bienvenido a la página principal!")

def about():
    put_text("Esta es la página 'Acerca de'.")

def contact():
    name = input("Ingresa tu nombre:")
    put_text(f"Gracias por contactarnos, {name}!")

# Agrega las rutas de PyWebIO correctamente
routes = webio_routes({
    '/': home,
    '/about': about,
    '/contact': contact,
    '/internal_tool_pdf_reader': internal_tool_pdf_reader
})

for route in routes:
    app.router.routes.append(route)  # Agrega las rutas manualmente
