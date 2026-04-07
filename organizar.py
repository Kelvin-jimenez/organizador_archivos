from pathlib import Path

carpeta_objetivo = Path("carpeta_prueba")

categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"]
}

extension_a_categoria = {}

for categoria, extensiones in categorias.items():
    for ext in extensiones:
        extension_a_categoria[ext.lower()] = categoria

archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]

for archivo in archivos:
    ext = archivo.suffix.lower()
    categoria = extension_a_categoria.get(ext, "Otros")

    destino = carpeta_objetivo / categoria
    destino.mkdir(exist_ok=True)

    nuevo_path = destino / archivo.name
    archivo.rename(nuevo_path)

    print(f"Movido: {archivo.name} → {categoria}/")