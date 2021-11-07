# django-fundamentos-desarrollo-web2

## ESTE PROYECTO ES CONTYINUACION DEL CURSO DE SOLO PYTHON FUNDAMENTOS DEL DESARROLLO WEB (2H56M)

### CREAR PROYECTO
* Para crear el proyecto lo hacemos con el comando *django-admin startproject [nombreProyecto]*
* Configuramos el archivo *settings.py* para tenerlo listo para trabajar con imágenes posteriormente.

![image](https://user-images.githubusercontent.com/84333525/140631855-2fc4eb06-4ed6-4bde-92b2-b436e80d7184.png)

* Configuarmos el archivo *urls.py* para poder trabajar con las imágenes:

![image](https://user-images.githubusercontent.com/84333525/140631968-5374b4a1-c852-441b-8c68-82be5b68686e.png)

* Creamos y corremos las migraciones con los comandos:
  - *python manage.py makemigrations*
  - *pyhton manage.py migrate*

* Creamos el super usuario con el comando:
  - *python manage.py createsuperuser*

* Corremos el servidor para verificar que todo esté bien:
  - *python manage.py runserver*

* Configuración para trabajar con templates y boostrap (En otros proyectos lo he trabajado de una forma diferente esta es sólo una forma más de hacerlo)
  - Nos aseguramos de configurar la carpeta dónde se encontrarán ubicados los templates de la app:

  ![image](https://user-images.githubusercontent.com/84333525/140632069-11b68650-12eb-4e81-a4c5-9d9fbe3fdecb.png)

 - Luego creamos una carpeta con el nombre templates donde crearemos los archivos .html de nuestro proyecto.

* Como nota importante, para habilitar el autocomletado del lenguaje de plantillas de Django o de cualquier otro proyecto se hace de la siguiente manera:
    Se escoge Django en la siguiente configuración del PyCharm
    
    ![image](https://user-images.githubusercontent.com/84333525/140632270-8f43f7d2-3829-427d-ac20-607e12ceff10.png)

* Creamos el archivo base.html que es dónde pondremos el código único para toda la parte visual de la app.

    ![image](https://user-images.githubusercontent.com/84333525/140632287-72eb8d3b-c472-4b9c-8693-042a5667d2d9.png)
    
### CREAR LA PRIMERA APP POST
* Creamos la app posts con el siguiente comando:
  - *python manage.py start app [nombreApp]*
* Cuando creamos una app nueva debemos incluirla en el archivo *settings.py* en la sección de *INSTALEED_APPS*

  ![image](https://user-images.githubusercontent.com/84333525/140632347-d39dd007-30ef-40e2-9692-a871290bc72d.png)
  
* Definimos nuestro modelo de POSTS:
  - Nos ubicamos en el archivo *models.py*
  
  ![image](https://user-images.githubusercontent.com/84333525/140632454-ffc7f896-6d32-40ec-9bc7-400754f31de2.png)

  - Recordar que los posts siempre tienen que heredar de models.Model
  - Los campos que son CharacterField siempre hay que pasarle como parámetro la longitud
  - En este caso los campos que son de fechas se le pasan como parámetros en el primero de los casos para que se autocomplete el campo en caso de la acción que se requiera, creación o actualización.

* Definimos nuestro modelo de COMENTARIOS
  
  ![image](https://user-images.githubusercontent.com/84333525/140632611-f229f683-edb7-4568-b926-7758adf4ec13.png)

- Recordar en este caso que cuando hacemos una relación uno a uno se utiliza ForeignKey con la tabla que se está haciendo la relación, además de que siempre hay que pasarle un segundo parámetro en el que se define que acción se va ha realizar en caso de que se borre el elemento con el que se hace relación.

* Definimos nuestro modelo de Vistas y además el de los likes:

![image](https://user-images.githubusercontent.com/84333525/140632698-babc873c-c79d-4ca9-8095-1dd253a252a8.png)

![image](https://user-images.githubusercontent.com/84333525/140632734-2230c49c-038c-412b-bcda-781586c7eced.png)

* Recordar que cuando hacemos cambios en los modelos siempre debemos crear y correr migraciones.

* Agregamos los modelos a nuestro panel de administración

![image](https://user-images.githubusercontent.com/84333525/140632831-921e4c13-93a6-4dd4-b8d8-181c08c4daa6.png)

*******django allauth*******
Instalamos este paquete con el comando: pip install django-allauth

* De la documentación (DOC)[https://django-allauth.readthedocs.io/en/latest/installation.html] nos copiamos la variable AUTHENTICATION_BACKENDS en nuestro archivo settings.py

* También copiamos de la documentación apps que hay que agregar a la variable INSTALLED_APPS:

  ![image](https://user-images.githubusercontent.com/84333525/140633011-9498dc42-3ccf-4764-9fd0-0310678d1b9b.png)

* Agregamos la variable SITE_ID:

  ![image](https://user-images.githubusercontent.com/84333525/140633031-7226eabd-71da-4b84-b25e-5bbd3aaa3ff0.png)

* Agregamos el siguiente path en nuestro archivo *urls.py* del proyecto

![image](https://user-images.githubusercontent.com/84333525/140633068-d09fbc15-0a2b-4c55-9145-27c64ef037cb.png)

* Creamos y corremos migraciones

### CONFIGURAR EL USUARIO DE AUTENTICACION
* Es decir el usuario que se autentica, para ello creamos el modelo de usuario, teniendo siempre en cuenta que va heredar del usuario base.
* Para ello importamos el AbstractUer y heredamos de ella, esto se va a estar encargando username, password, emial
* Cuando vamos a sobre escribir la manera por defecto que tiene Django de trabajar con los usuarios tenemos que especificar en el archivo settings.py dónde econtrar el modelo de usuario:

![image](https://user-images.githubusercontent.com/84333525/140633341-8647cda5-81c5-487d-a4fa-49de0ce2b81b.png)

De momento definremos el usuario de la siguiente manera para más adelante trabajar con el:

![image](https://user-images.githubusercontent.com/84333525/140633358-759e0e8a-73c7-484e-9884-01a81444a950.png)

* Como de costumbre cada vez que trabajamos con los modelos, debemos crear y correr migraciones.
  - Para evitar errores, eliminamos la carpeta de migraciones, además eliminamos la BD. 

* Creamos nuevamente el super usuario.

### CREAR VISTAS PARA TRABAJAR CON NUESTROS MODELOS
* Crearemos vistas basadas en clases, para ello hacemos todas las importaciones que vamos a necesitar

![image](https://user-images.githubusercontent.com/84333525/140634057-cc28d6dc-35fb-458f-90ee-367b9868e4f0.png)

![image](https://user-images.githubusercontent.com/84333525/140634138-58ed2573-6f17-4ded-a601-5f762b622b26.png)

### CREAR LAS URLS PARA CADA UNA DE LAS VISTAS CREADAS

![image](https://user-images.githubusercontent.com/84333525/140634323-d0ab99b7-8b0c-4eb5-8cfd-5d285c1b3d81.png)

### MODIFICAMOS EL MODELO O MODELOS QUE NECESITEN SLUG COMO POST
* Ya sabemos para que es el slug que no es más que un identificador y es de tipo models.SlugField()

### NOTA: EL ORDEN DE LAS URLS SI IMPORTA, LOS PATH QUE NO TIENEN SLUG U OTRO IDENTIFICADOR DEBEN IR ANTES DE LOS QUE SI LO TIENEN




