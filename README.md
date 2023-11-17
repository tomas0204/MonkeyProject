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
python -m venv NOMBRE
```

Activa tu entorno

```sh
# Unix
source NOMBRE/bin/activate
```

Instala los requerimientos, este archivo `requirements.txt` solo contiene lo basico para hacer funcionar esta pagina, asi que tienes que instalar los modulos faltantes

```sh
pip install -r requirements.txt
```

## Desarrollo!

Para iniciar localmente debes de ejecutar Tailwind y luego el servidor de Django, el proceso debe ser en distintas terminales

```sh
# Terminal 1
python manage.py tailwind start
```

```sh
# Terminal 2
python manage.py runserver
```

Asegurate de tener `Debug` en `True`

```py
#vercel_app/settings.py
Debug = True
```

Verifica tus `ALLOWED_HOSTS` y si tienes formularios no te olvides de `CSRF_TRUSTED_ORIGINS`

```py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1', 'https://.vercel.app']
```

## Produccion!

Para subir tu pagina correctamente a Vercel, deberias tener estos aspectos en cuenta:

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

Verifica tus `ALLOWED_HOSTS` y si tienes formularios no te olvides de `CSRF_TRUSTED_ORIGINS`

```py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1', 'https://.vercel.app']
```

<hr/>

> Este repositorio fue creado el `17 / Nov / 2023`
