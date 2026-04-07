# 📂 Organizador de Archivos con Python

Script de automatización desarrollado con Python para organizar archivos dentro de una carpeta según su tipo.

## 🚀 Objetivo
Clasificar automáticamente archivos en subcarpetas según su extensión.

## 🛠 Tecnologías utilizadas
- Python
- pathlib

## 📁 Estructura del proyecto
- `organizar.py` → script principal
- `carpeta_prueba/` → carpeta con archivos de prueba

## ⚙️ Funcionalidad
El script organiza archivos en las siguientes categorías:
- `Imagenes`
- `Documentos`
- `Videos`
- `Musica`
- `Otros`

## 🧠 Lógica del script
1. Lee los archivos de la carpeta objetivo
2. Detecta la extensión de cada archivo
3. Determina la categoría correspondiente
4. Crea la carpeta de destino si no existe
5. Mueve el archivo automáticamente

## ▶️ Cómo ejecutar
```bash
python3 organizar.py