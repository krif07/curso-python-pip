import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]

@app.get('/resources')
def get_resources():
    return {'Empresa': 'Platzi'}

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Página de contacto</h1>
        <p>Cristian Dávila</p>
        <p>krif07@gmail.com</p>
        <p>Test Automation Engineer</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()