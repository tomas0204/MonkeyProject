import os
import django
from pathlib import Path

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vercel_app.settings')  # Reemplaza "tu_proyecto" con el nombre de tu proyecto
django.setup()

from index.models import Word

def clear_database():
    try:
        # Elimina todas las palabras en la tabla Word
        Word.objects.all().delete()
        print("Base de datos limpiada exitosamente. Todas las palabras han sido eliminadas.")
    except Exception as e:
        print(f"Error al limpiar la base de datos: {e}")

if __name__ == "__main__":
    clear_database()
