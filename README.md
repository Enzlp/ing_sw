# Demo Proyecto Ingeniería De Software

## Como correr la demo 

Para poder probar la demo armada, descargue el zip correspondiente a este branch y siga las instrucciones de abajo.

Primero, es necesario instalar las librerias usadas para esto fue elaborado un archivo txt con los requerimientos. Para poder instalar los requerimientos, seguir las instrucciones de abajo. Se  recomienda crear un ambiente virtual para poder instalar las librerías. En Windows:
```sh
python3 -m venv venv
venv\Scripts\activate.bat
pip install -r .\requirements.txt
```

Una vez instalada el entorno en el que se trabajará, se debe ejecutar este comando en cmd:
```sh
cd leaderboard_profes
./manage.py migrate
python manage.py runserver      
```

El programa quedará siendo ejecutado en segundo plano, de manera local, para poder ver el sitio web en su navegador. Una vez seguido los pasos anteriormente dichos, dirijase a su navegador e ingrese a http://127.0.0.1:8000/, donde podrá que encontrar el sitio web.

> [!IMPORTANT]
>A veces debido a fallas con django y manage.py, también puede serle más útil usar 
>```sh
>python manage.py migrate
>```
>O ignorar este paso completamente y probar solo con:
>```sh
>cd leaderboard_profes
>python manage.py runserver      
>```
## Como interactuar con la demo

Dentro de la landing page encontrarán un link al acceso y registro del sitio como tal. Para registrarse hay que seleccionar registrate, y proveer un usuario, contraseña y mail. Una vez registrado el usuario, será redirigido a la página de login, donde es necesario ingresar su nombre de usuario y contraseña.

Una vez dentro de la página principal, diríjase a la página de cursos. Aquí podrá crear un curso el cual podrá calificar luego. Una vez creado el curso puede ir a la página de opiniones y ver que el curso creado aparecerá dentro de las opciones de cursos disponibles, además de otras opciones de calificación como opiniones y reseñas que puede crear. 

Para poder volver a la página principal basta oprimir el botón de cerrar sesión.