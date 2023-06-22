# PDFSplitterAndCompressor
Esta es una aplicación web que permite dividir un archivo PDF en páginas individuales y comprimirlos en un archivo ZIP. La aplicación está escrita en Python y utiliza Flask como framework web.
## Instalación
1. Clona este repositorio:
    ````bash
   git clone https://github.com/ChristianGonzal3z/PDFSplitterAndCompressor.git
    ````
2. Navega al directorio del proyecto:
   ````bash
   cd  PDFSplitterAndCompressor
   ````
3. Instala las dependencias:
    ````bash
    pip install -r requirements.txt
    ````
## Uso
1. Ejecuta la aplicación:
    ````bash
    python app.py
    ````
2. Abre tu navegador web y visita `http://localhost:5000`.

3. Selecciona un archivo PDF y haz clic en "Split and Zip" para dividir el archivo y comprimirlo en un archivo ZIP.

5. El archivo ZIP resultante se descargará automáticamente.

## Docker
1. Navega al directorio de la aplicación: 

```bash
  cd PDFSplitterAndCompressor
```
2. Construye la imagen de Docker a partir del Dockerfile:

```bash
  docker build -t PDFSplitterAndCompressor .
```
3. Inicia un contenedor a partir de la imagen de Docker:

```bash
  docker run -p 5000:5000 PDFSplitterAndCompressor
```