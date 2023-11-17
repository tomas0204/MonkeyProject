# Notas

## Vercel.json

```json
// Default vercel.json
{
  "builds": [
    {
      "src": "vercel_app/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "vercel_app/wsgi.py"
    }
  ]
}
// Version modificada 2
{
  "builds": [{
      "src": "vercel_app/wsgi.py",
      "use": "@ardnt/vercel-python-wsgi",
      "config": { "maxLambdaSize": "15mb" }
  }],
  "routes": [
      {
          "src": "/(.*)",
          "dest": "vercel_app/wsgi.py"
      }
  ]
}
```
