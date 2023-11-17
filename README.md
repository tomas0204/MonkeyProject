# Django + Vercel + Tailwind = ❤️

**Es una base lista para ser clonada!**

- Ya te reconoce los staticsfiles
- Te permite trabajar con Tailwind
- Usas Vercel
- Usas Django

*Que mas puedes pedir?*

Solo te falta el dominio para tu grandiosa app/web, pero ese no te lo puedo dar yo...

## Antes de empezar a programar!

Tu carpeta `static/` ahora esta dentro de `theme/static/` si quieres agregar otras carpetas puedes cambiar tu configuracion de `STATICFILES_DIRS`

```py
#vercel_app/settings.py
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "theme/static/"),
  os.path.join(BASE_DIR, "RUTA_DE_TU_OTRA_CARPETA")
]
```

Te recomiendo crear un entorno virtual, asi tendras mas control de todo

```sh
python -m venv venv
```

Activa tu entorno

```sh
source venv/bin/activate
```

Instala los requerimientos, este archivo `requirements.txt` solo contiene lo basico para hacer funcionar esta pagina, asi que tienes que instalar los modulos faltantes

```sh
pip install -r requirements.txt
```

## A tomar en cuenta

Antes de entrar a produccion te recomiendo checar estos detalles

```py
#vercel_app/settings.py
Debug = False
```

Haz las migraciones!

```sh
python manage.py makemigrations && python manage.py migrate
```

Tambien puedes poner las migraciones "automaticas" en el archivo `vercel_build_staticfiles.sh` **descomentando** la linea que viene abajo de `Automatic Migrations` esto hara que las migraciones se hagan cada que se recopilen los staticsfiles

```sh
# Automatic migrations                                       # esta linea NO se debe descomentar
#echo "Iniciando migraciones..."                             # esta linea se debe descomentar
#python manage.py makemigrations && python manage.py migrate # esta linea se debe descomentar
```

Tienes Super usuario?

```sh
python manage.py createsuperuser
```
