## Como subir un repositorio local a la nube.

Para empezar hay que ejecutar los siguientes comandos para configurar ***git*** 

```
sudo apt install git

git config --global user.name <tu-usuario-de-github>
git config --global user.email <tu-email-del-usuario-de-github>
```

Una vez realizado el paso anterior, ya tenemos ***git*** configurado, ahora para configurar ***gh*** ejecutamos el siguiente comando:

```
sudo apt install gh
```

Para configurar tu información en gh hay 2 maneras, aquí se va a mostrar 1 de ellas, que es haciendo la autenticación mediante navegador, pero nos podemos autenticar mediante la terminal en caso de tener un [token de github](https://github.com/settings/tokens)

El token necesita al menos los siguientes checkbox para funcionar:

![](./img/token.png)

Una vez generado procedemos a usar el siguiente comando:

```
gh auth login
```

Al ejecutar el comando podemos interactuar con la terminal mediante el uso de las flechas del teclado, el texto que aparezca en azul (como en la primera imagen) es la selección actual. Seleccionamos Github.com

![](./img/1.png)

Como metodo para las operaciones en Github utilizaremos el protocolo ssh

![](./img/2.png)

En el paso actual nos pedirá una clave pública, si no la tenemos creada, cancelaremos con Control + C y ejecutaremos el comando ***ssh-keygen*** y dejaremos todos los campos vacios para generar una clave, luego repetiremos todos los pasos hasta el actual, ahora nos saldrá nuestra clave, como en la imagen, la seleccionamos.

![](./img/3.png)

Ahora podemos autenticarnos con el token de Github que generamos anteriormente.

![](./img/4.png)

Una vez autenticados nos saldrá algo similar a lo siguiente:

![](./img/5.png)

Para crear un repositorio basico podemos hacer lo siguiente:

Creamos una carpeta prueba, nos movemos dentro de ella e inicializamos un repositorio de git

![](./img/repo1.png)

Ejecutamos el comando **```gh repo create```** y elegimos la segunda opción, subir un repositorio local existente

![](./img/repo2.png)

Ahora nos pide, en orden: 
+ La ruta al repositorio
+ El nombre
+ Una descripción 
+ La visibilidad

![](./img/repo3.png)

Añadimos un remoto del repositorio y especificamos como deberia llamarse el remoto, por defecto origin

![](./img/repo4.png)

Como no podemos subir un repositorio vacio, creamos un README.md con un titulo y una frase descriptiva.

![](./img/repo5.png)

Hecho esto, añadimos los cambios con ***```git add .```*** , ***```git commit -m "mensaje"```*** y ***```git push```***.

Al ejecutar git push, va a dar un fallo, porque no hemos vinculado la rama del repositorio local con el repositorio remoto, por lo que ejecutamos ***```git push -u origin main```*** (-u es la versión corta del parámetro ***```--set-upstream```***), y como es la primera vez que hacemos algo en github desde esta máquina nos pregunta si queremos seguir conectandonos y recordar nuestra elección para un futuro

![](./img/repo6.png)

El repositorio queda de la siguiente manera:

![](./img/repo7.png)

## Crear un script que automatice la creación del repo

Ahora vamos a crear un script que automatice la creación de repositorios, para ello vamos a necesitar un token de autenticación de github, si no sabes o no tienes uno, puedes generarlo [aquí](https://github.com/settings/tokens?type=beta).

Una vez que tenemos el token de autorización

### Script de repo

```
#!/bin/bash

take() {
        dir=$@
        mkdir -p $dir && cd $dir
}

if [ "$#" -eq 0 ]; then
        echo "Error: Se requiere al menos un argumento"
        exit 1
fi

actual_dir=$(pwd)

take "$actual_dir/$1"

echo "-----------------------------------------------------"
echo "Entrando en $1"
echo "-----------------------------------------------------"

git init

touch README.md

echo -e "# $1\n\nRepository of $1" | tee -a README.md > /dev/null

echo "-----------------------------------------------------"
echo "README.md añadido"
echo "-----------------------------------------------------"

gh auth login --with-token < <ruta-a-tu-token-de-github>.txt
gh repo create --private -s $actual_dir/$1 -r main --add-readme

echo "-----------------------------------------------------"
echo "Has sido autenticado y tu repo se ha creado"
echo "-----------------------------------------------------"

git add .
git commit -m "initial commit for this repo"
git push -u main master

echo "-----------------------------------------------------"
echo "Se han añadido los cambios locales a tu repositorio"
echo "-----------------------------------------------------"
```



#### Modo de uso:

> Este script no es perfecto y no tiene todas las posibilidades del comando gh por lo que su uso se limita a 1 sola cosa con 1 solo modo de uso.

Para poder usar este script en todos lados, podemos situar el script en la ruta