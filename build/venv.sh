#!/bin/bash

# Definir o diretório raiz e build
ROOT_DIR="$(dirname "$(dirname "$(realpath "$0")")")"
BUILD_DIR="$ROOT_DIR/build"
VENV_DIR="$ROOT_DIR/.venv"

# Verifica se a pasta 'build' existe
if [ ! -d "$BUILD_DIR" ]; then
    echo "A pasta '$BUILD_DIR' não existe."
    exit 1
fi

# Criar o ambiente virtual na raiz do projeto
python3 -m venv "$VENV_DIR"

# Identificar o SO e ativar o ambiente virtual corretamente
if [[ "$(uname -s)" == "MINGW"* || "$(uname -s)" == "CYGWIN"* || "$(uname -s)" == "MSYS"* ]]; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Instalar dependências se o arquivo requirements.txt existir dentro da pasta build
if [ -f "$BUILD_DIR/requirements.txt" ]; then
    "$VENV_DIR/bin/python" -m pip install -r "$BUILD_DIR/requirements.txt"
else
    echo "Arquivo requirements.txt não encontrado na pasta build."
fi