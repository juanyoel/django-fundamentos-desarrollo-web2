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

* Cuando implemantamos la view del create nos dará un error si no le pasamos los campos que pueden actualizarce, para ello modificamos el código de la siguiente manera:

![image](https://user-images.githubusercontent.com/84333525/141043886-5cea5078-ad2a-49f5-8795-297bc2320d4f.png)

* Cuando usamos el view para el delete tenemos que obligatoriamente pasarle un success_url sino obtenemos un error:

![image](https://user-images.githubusercontent.com/84333525/141044448-74df53e1-d88c-4493-bc82-8a907dd15b09.png)

* Cuando usamos la vista create sino le especificamos los campos nos retorna un error como el siguiente:

![image](https://user-images.githubusercontent.com/84333525/141045286-3c656acd-75f7-4141-892f-c6436beb3913.png)

Por lo que debemos modificar la vista del create de la siguiente forma:

![image](https://user-images.githubusercontent.com/84333525/141045739-fc158718-8ed1-480f-81d9-54a3fdc34180.png)

### CREAR LOS FORMULARIOS
* Para ello nos ubicamos en el directorio de la app de posts en este caso y creamos el archivo *forms.py*
* Hacemos las importaciones necesarias
* Cuando definimos la clase del formulario necesitamos definir la clase de *Meta*

![image](https://user-images.githubusercontent.com/84333525/141046155-05e61f3c-bb53-4f40-8b44-aeef1e23628a.png)

dónde definimos el modelo con el que estaremos trabajando además de los campos del mismo, en este ejemplo mirar que entre comillas utilizamos __all__ lo que significa que traerá todos los campos del modelo.

* Una vez implementado el modelo del formulario podemos trabajar con el en la vista, para ello primero lo importamos.
* Y seguidamente podemos usar el atributo form_class del Update y Create para poder trabajar con el formulario que hemos creado:

![image](https://user-images.githubusercontent.com/84333525/141046633-811e908d-f870-4a2c-8dc1-aeed3aa1ac42.png)

 * Luego de los pasos anteriores ya podemos modificar el archivo *post_form.html* creando un formulario vinculado a la clase formulario que hemos creado:

Los create / update o cualquier otro metodo que envíe información al servidor o que maneje iformación debe estar en etiquetas form como muestro en el siguiete ejemplo:

recordar siempre que es buena práctica de seguridad usar *csrf* en todos los formularios y además en este ejemlpo usamos la etiqueta *view_type* que nos mostrará que acción estamos realizando, recordar que es el mismo formulario para el create y el update.

![image](https://user-images.githubusercontent.com/84333525/141048038-817002e2-bffe-4d5f-8755-acec6e7419bd.png)

Otra cosa a tener en cuenta si hacemos las implementaciones así es que como ya estamos vinculando el formulario con sus respectivos campos, y tener al mismo tiempo los campos definidos en el view podemos obtener un error de la siguiente forma

![image](https://user-images.githubusercontent.com/84333525/141048182-b4337e6d-b115-44de-bdd9-266eda640239.png)

Para solucionar solo debemos borrar los campos y dejarlos de la siguiente forma:

![image](https://user-images.githubusercontent.com/84333525/141048233-45636620-9cb2-4607-a86e-ea86ea64b648.png)

* Luego para trabajar con el contexto definimos una función *get_context_data()* el cual modificamos para poder retornar a la vista (html) que acción estamos ejecutando.

* Con el filtro *|title* logramos capitalizar la palabra a la que le pongamos.

![image](https://user-images.githubusercontent.com/84333525/141048810-6ed7fd6e-f572-4cfa-b4ef-d1bd834b07d7.png)

* Importante también es definirle que tipo de datos estaremos manejando en el formulario:

![image](https://user-images.githubusercontent.com/84333525/141048942-f4e6aaa7-e0e1-4c08-8745-8f623d0efeaa.png)

## UN POCO DE MANEJO DE ESTILOS :)
A partir del minuto 3H:40M o un poco antes, me parece genial para hacer estilizar algunos ejemplos rápidos para entrevistas o algo así.

### Nota en el siguiente código muestro como puedo ver los detalles de los elementos de la lista, esto es super importante:

![image](https://user-images.githubusercontent.com/84333525/141053797-191e1f2c-a0bc-400a-8bb0-5cd3b254fd0d.png)

Debo crear el método get_absolute_url(self): --> le defino la página dónde se visualizaran los detalles y le paso como paámetro lo que espera la vita de detalles en este caso el slug para que pueda encontrar el elemento sobre el que estamos ejecutando la acción

![image](https://user-images.githubusercontent.com/84333525/141054054-cb1656e7-8c36-4901-b3e8-898ce1ebef70.png)

Modifico el link del html para que me lleve a la dirección deseada.

### AGREGAR CANTIDAD DE VISTAS COMENTARIOS Y LIKES A UN POST DETERMINADO
* Lo primero que hacemos es agregar el código html dónde ubicaremos el código

![image](https://user-images.githubusercontent.com/84333525/143312228-0fa5dd5d-fd2c-4b37-b555-c305f51d2285.png)

* Luego para estilizar un poco le agregamos icónos, para ello vamos a la página de fontawesome y seguimos las instrucciones.
* Luego de obtener la url de fontawesome la agregamos al proyecto en el archivo base.html

![image](https://user-images.githubusercontent.com/84333525/143312683-a7357e75-a7ae-4759-a819-e2d378740e80.png)

### SUPER IMPORTANTE ESTE PASO PARA CALCULAR LAS CANTIDADES DE VIEWS, COMMENTS Y LIKES
* Para ello modificamos el modelo de Post y le adicionamos las siguientes propiedades:

![image](https://user-images.githubusercontent.com/84333525/143313476-91a423ca-9365-42e4-9339-baae164aea35.png)

* Los nombres de los atributos a los que se hace referencia es debido a que cada uno de los modelos tiene una relación con el modelo Post, por eso es que se pueden acceder de esa manera: 

![image](https://user-images.githubusercontent.com/84333525/143313603-313dabc6-e2b2-43b9-a70e-8cc5b73584d3.png)

* Luego pasamos a vincular las nuevas propiedades creadas con el código html y de paso le pasamos los iconos importados de font awesome.

![image](https://user-images.githubusercontent.com/84333525/143314535-86395bfb-724c-4b42-9fa9-81ac94d3ff98.png)

* Luego podemos adicionar si queremos cuando fue posteado y lo hacemos de la siguiente manera:

![image](https://user-images.githubusercontent.com/84333525/143314982-32c2e5a5-cec9-493e-9d82-3baba6efc832.png)

### ESTILIZAR EL POST DETAIL VIEW
* Le agregamos toda la información que manejamos de los post a la página de detalles como ya hemos hecho antes en la lista.
* #### Ahora queremos darle funcionalidad al botón de dar like:

![image](https://user-images.githubusercontent.com/84333525/143316174-a93a8321-5ec9-4d88-bf1f-a1d97c7c9b17.png)

* Primero hacemos la función que nos permitirá verificar que existe el elemento sino retornará un error (para ello utilizamos el método get_object_or_404) luego verificamos si ya se le ha dado like o no, el método completo quedaría de la siguiente forma:

![image](https://user-images.githubusercontent.com/84333525/143317328-6d486bdb-3844-4d4f-92b9-3de7472e3d2b.png)

* Agregamos la nueva función al archivo *urls.py* :

![image](https://user-images.githubusercontent.com/84333525/143317682-fb1814e4-dcf5-4945-ad30-a194a76d6527.png)

* Luego en los modelos podemos definir un método igual a get_absolute_url pero para los likes:

![image](https://user-images.githubusercontent.com/84333525/143317957-1b96a780-3cb8-4dfc-bdf2-d18c57b18dfa.png)

* Luego vinculamos la función directamente con la vista (html):

![image](https://user-images.githubusercontent.com/84333525/143318335-925b5ee0-0f31-448c-95fa-2f73f67f34fc.png)

* #### DARLE FUNCIONALIDAD A LAS VISTAS QUE HA TENIDO EL POST
* Simplemente le agregamos la siguiente función a la clase PostDetailView:

![image](https://user-images.githubusercontent.com/84333525/143319261-d66e855d-e154-4742-82ec-0a1ff513cb3f.png)

### AGREGAR COMENTARIOS
* Lo primero que hacemos es crear el formulario, para ello vamos al archivo *forms.py* y lo creamos de la siguiente manera:

![image](https://user-images.githubusercontent.com/84333525/143319744-3f88ba11-2df1-463b-823e-a4e533999b4e.png)

* Luego nos ubicamos en nuestro archivo *views.py* e importamos el formulario que hemos creado.

#### ESITLO A LOS FORMULARIOS
* Vamos usar un paquete llamado django-crispy-forms, que instalamos usando el comando *pip install django-crispy-forms*
* Lo agregamos a las APPS instaladas en el archivo *settings.py*
* Le definimos de donde vamos a usar los templates (toda esta info se puede obtener en la documentación de la librería)

![image](https://user-images.githubusercontent.com/84333525/143627060-022fbf25-e95a-4a43-9632-514d4f020d9c.png)

* Se lo agregamos al archivo HTML

![image](https://user-images.githubusercontent.com/84333525/143627166-784ca0f5-00d1-4f86-abf6-f186937165ca.png)

* Cambiamos el código del formulario:

![image](https://user-images.githubusercontent.com/84333525/143627227-a036c523-2a69-4858-9b22-d71e1820c304.png)

* Si queremos estilizar un poco el text area como por ejemplo darle un poco menos de tamaño por defecto lo hacemos de la siguiente manera:

![image](https://user-images.githubusercontent.com/84333525/143627661-ca822114-0260-4700-88d9-454778a633a1.png)

* Hice lo mismo para el formualrio del create.

## TIPS
* Para cambiar la contraseña de un usuario como un admin podemos usar el siguiente comando: *python.exe manage.py changepassword admin*



