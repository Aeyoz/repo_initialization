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