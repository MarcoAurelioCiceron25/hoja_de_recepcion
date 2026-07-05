import base64

# Abrir el logo dentro de la carpeta data
with open("data/logo.png", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

# Guardar la cadena en un archivo
with open("data/logo_base64.txt", "w") as out:
    out.write(encoded)

print("✅ Logo convertido a Base64 y guardado en data/logo_base64.txt")
