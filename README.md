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