# EntregaFinal-Alcala

El video mostrando a fondo todo el blog con las funcionalidades está en este link:
https://www.loom.com/share/86b7ed2cc0304d268f4951ee00ca5bf5?sid=e253df1e-b7ba-4db7-bdaf-14ea9dc6c97f

Al clonar el repositorio, y una vez creado el entorno virtual, hay que instalar django y pillow con el comando:

    pip install -r requirements.txt

Después hay que correr las migraciones para db.sqlite3 con el comando:

    python manage.py migrate

Ahí ya está listo para correr el servidor. Si quisiera acceder al admin puede crear primero el superusuario, y si no ya directamente:

    python manage.py runserver

Al correr el servidor, será llevado directamente a la página de inicio. Ahí, hay un botón para ir a 'Sobre mí', donde podrá ver un poco acerca mío, el creador de Blog. Desde el navbar se puede ir a la pestaña 'Explorar' donde aparecen todos los posteos de todos los usuarios.

En la pestaña explorar, hay una barra para filtrar los posteos. Se puede filtrar por título y por autor.

Para poder escribir un post, o hacer comentarios a posteos en la pestaña Explorar, es necesario estar loggeado. Para eso, en el navbar puede ir al botón 'Registrarse' para crear un usuario completando el formulario que aparece. Luego, en 'Login', ingrese el usuario y contraseña que creó anteriormente.

Una vez loggeado, en la pestaña explorar aparece un botón para crear un posteo, y se habilita para escribir comentarios debajo de cada posteo. En los comentarios de tu usuario, hay un botón de eliminar a la derecha para eliminar los comentarios que hiciste. Antes de eliminarlo hay otro template para confirmar que se quiere eliminar el comentario.

Ahora también tiene habilitada la pestaña 'Perfil' en el navbar. Ahí podrá escribir su biografía, y guardarla para que ya quede en el perfil. Abajo, están los botones 'Editar perfil' y 'Subir avatar'. Desde editar perfil, se ven los campos para editar la información del perfil de usuario. En subir avatar, se puede subir una imagen o gif que se verá en la pestaña 'Perfil' y en el navbar al lado del mensaje de bienvenida.

Por último, también se muestran todos los posteos de tu usuario en la pestaña perfil. Desde acá se puede crear un posteo nuevo, editar los posteos anteriores y eliminarlos.

Para cerrar sesión, simplemente hay que usar el botón Logout de la navbar.

¡Que te diviertas con Blog!