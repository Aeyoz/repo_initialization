# Como crear un repositorio en la nube desde 0.

Como punto de partida tenemos el ordenador y vamos a necesitar los paquetes git y gh, además de tener las configuraciones pertinentes realizadas en cada uno de ellos.
En el paquete de git ejecutaremos los comandos de **git config --global user.name <NOMBRE>** y **git config --global user.email <EMAIL>**
En el paquete de gh ejecutaremos el comando de **gh auth login** y seguiremos los pasos que se nos indica por pantalla.

A continuación crearemos el repositorio en local, para ellos crearemos una carpeta que la llamaremos **prueba** y nos situaremos en ella.
Ejecutamos el comando **git init** , añadimos un fichero **README.md** y ejecutamos los comandos **git add .**, **git commit -m "<MENSAJE>"**.
Ejecutamos el comando **gh repo create** y seguimos los pasos que se nos indica por pantalla, y a continuacion ejecutamos el comando **git push -u origin prueba**
