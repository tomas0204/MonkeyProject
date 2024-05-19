#!/bin/bash

# Verificar si virtualenv está instalado, si no, instalarlo
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv no se encontró, instalándolo..."
    pip install virtualenv
fi

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar pip en el entorno virtual si no está disponible
if ! command -v pip &> /dev/null
then
    echo "pip no se encontró en el entorno virtual, instalándolo..."
    curl https://bootstrap.pypa.io/get-pip.py | python
fi

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --noinput --clear
