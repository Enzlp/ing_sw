# Demo Proyecto Ingeniería De Software

## Como correr la demo 

Primero, es necesario instalar las librerias usadas para esto fue elaborado un archivo txt con los requerimientos. Para poder instalar los requerimientos, seguir las instrucciones de abajo. Se  recomienda crear un ambiente virtual para poder instalar las librerías.
```sh
python3 -m venv .venv
pip install -r .\requirements.txt
```

Una vez instalada el entorno en el que se trabajará, se debe ejecutar este comando en cmd:
```sh
cd leaderboard_profes
./manage.py migrate
python manage.py runserver      
```

El programa quedará siendo ejecutado en segundo plano, de manera local, para poder ver el sitio web en su navegador. Una vez seguido los pasos anteriormente dichos, dirijase a su navegador e ingrese a http://127.0.0.1:8000/, donde podrá que encontrar el sitio web.

## Como interactuar con la demo



# 2023-2-grupo-1
Se implementó:
- página de registro
- landing page
- página de login
- página de perfil
- ver cursos
- crear cursos
- enviar reseñas de cursos
- ver reseñas


```sh
python3 -m venv .venv
pip install -r .\requirements.txt
```
En esta parte se debe entrar al ambiente virtual, que varía según el sistema operativo.
```sh
cd leaderboard_profes
./manage.py migrate
python manage.py runserver      
```
Se debe ingresar a http://127.0.0.1:8000/, desde donde al apretar Opiniones, permitirá ver las reseñas y crearlas. Mientras que al apretar Cursos, permitirá ver los cursos y crearlos.