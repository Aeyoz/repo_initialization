#!/usr/bin/python3

import sys
import os

def create_repo():

    VALID_ANSWERS = ["si", "yes", "s", "y"]
    VALID_OPTIONS = ["-p", "-r", "-h", "-d"]

    if len(sys.argv) < 2:
        print("NO HAS INTRODUCIDO UN NOMBRE PARA TU REPO")
        print("Usa repo -h para obtener más información de como usar este comando")
        return -1

    help_text = """
El comando repo tiene la siguiente estructura:
repo <nombre-del-repo> <parámetros-opcionales>
Parámetros opcionales:

-r:
    Ignora el resto de parámetros que hayas introducido y te lleva
    a una pantalla de terminal que te pide confirmación para borrar
    el repo que le indiques en <nombre-del-repo>.

-p:
    Crea el repositorio como privado, por defecto el repositorio que
    crees será público.

-h:
    Te lleva a esta página de ayuda

-d <descripción>:
    Establece una descripción para tu repositorio

-b:
    Establece el nombre remoto de tu repositorio (por defecto main)

-s <ruta-al-repo>:
    Establece la ruta que se va a usar para la creación del repositorio 
    (por defecto la ruta que se usa es: 
    tu directorio actual + el nombre indicado en repo <nombre-del-repo>)
"""

    repo_name_candidate = sys.argv[1]
    if repo_name_candidate in VALID_OPTIONS:
        print(help_text)
        return 0

    repo_name = sys.argv[1]
    options = sys.argv[2:]
    final_command = ["gh", "repo", "create", repo_name, "-r main", "-s ."]
    visibility = ["--public"]


    repo_path = os.getcwd() + f"/{sys.argv[1]}"

    default = True

    if options:
        default = False

    if not default:
        skip = False
        for option in options:
            if skip:
                skip = False
                continue
            match option:
                case "-h":
                    print(help_text)
                    return 0
                case "-b":
                    try:
                        branch_name = options[options.index("-b") + 1]
                        if branch_name in VALID_OPTIONS:
                            print("No puedes usar una opción del comando como rama para tu repo")
                            print("Usa -b '<nombre-de-la-rama-principal>'")
                            return -1
                    except:
                        print("No especificaste un nombre de rama remota para el repositorio")
                        return -1
                    final_command[4] = f"-r {branch_name}"
                    skip = True            
                case "-p":
                    visibility = ["--private"]
                case "-r":
                    final_command = ["gh", "repo", "delete", repo_name]
                case "-d":
                    try:
                        description = options[options.index("-d") + 1]
                        if description in VALID_OPTIONS:
                            print("No puedes usar una opción del comando como descripción para tu repo")
                            print("Usa -d '<alguna-descripción>'")
                            return -1
                    except:
                        print("No especificaste una descripción para el repositorio")
                        return -1
                    final_command.append(f"--description '{description}'")
                    skip = True
                case "-s":
                    try:
                        path = options[options.index("-s") + 1] + repo_name
                        if path in VALID_OPTIONS:
                            print("No puedes usar una opción del comando como ruta de tu repo, por favor usa una válida")
                            print("Usa -s <ruta-al-repo>")
                            return -1
                    except:
                        print("No especificaste una ruta para el repositorio")
                        return -1
                    repo_path = path
                    final_command[5] = f"-s {path}"
                    skip = True
                    print(f"La opción -s hace lo que debe, la ruta: {path}")
                case _:
                    print("Opción desconocida o inválida")
                    print(help_text)
                    return -1

    if not os.path.exists(repo_path):
        print("El repositorio que estas intentando crear no tiene carpeta en tu sistema")
        print("Estas son las opciones validas:")
        print(", ".join(VALID_ANSWERS))
        if (user_answer := input(f"¿Deseas crear la carpeta {repo_path}?\n").lower()) in VALID_ANSWERS:
            try:
                os.makedirs(repo_path)
            except:
                print()
                print("----------------------------------------IMPORTANTE----------------------------------------")
                print("           Ejecuta el script mediante sudo si quieres crear el repo en esta ruta")
                print("------------------------------------------------------------------------------------------")
                print()
                return -1
            print("Se procederá a crear el repositorio")
            os.chdir(repo_path)
        else:
            print(f"Se abortó la creación del repositorio {repo_name}")
            return -1

    final_command.extend(visibility)
#    final_command.append("--add-readme")


    os.system("pwd")
    os.system(f"git init {repo_path}")
    os.system("touch README.md")
    os.system(f"echo -e '# $1\n\nRepository of {repo_name}' | tee -a README.md > /dev/null")
    os.system("gh auth login --with-token < /home/pc22-dpl/access.txt")
    print(" ".join(final_command))
    # gh repo create --private -s $actual_dir/$1 -r main --add-readme
    # gh repo create mano -r main -s /home/pc22-dpl/mano
    os.system(" ".join(final_command))
    os.system("git add .")
    os.system("git commit -m 'primera prueba en python'")
    os.system(f"git push -u {repo_name} origin main")



create_repo()
#os.system("mkdir /home/pc22-dpl/mano2")
#os.system("git init /home/pc22-dpl/mano2")
#os.system("gh repo create mano2 --private -s /home/pc22-dpl/mano2 --add-readme -r main --description 'descripcion de prueba'")