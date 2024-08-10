#!/bin/bash
set -e

# Verificar si virtualenv está instalado, si no, instalarlo
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv no se encontró, instalándolo..."
    python3 -m pip install virtualenv
fi

# Eliminar el directorio venv si ya existe
if [ -d "venv" ]; then
    echo "Eliminando directorio venv existente..."
    rm -rf venv
fi

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar pip en el entorno virtual si no está disponible
if ! command -v pip &> /dev/null
then
    echo "pip no se encontró en el entorno virtual, instalándolo..."
    curl https://bootstrap.pypa.io/get-pip.py | python3
fi

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python3 manage.py collectstatic --noinput --clear
