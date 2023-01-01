# Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 main.py
```

# App Project

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# App Project con Docker

```
cd app
# construir la app
docker-compose build
# para bajar el contenedor
docker-compose down
# para correr el contenedor
docker-compose up -d
# para listar los contenedores activos
docker-compose ps
# correr la app dentro del contenedor
docker-compose exec app-csv bash
# en el bash del contendor
python main.py
```

# web-server Project

```sh
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
ir a 
http://localhost:8000/
http://localhost:8000/contact
```