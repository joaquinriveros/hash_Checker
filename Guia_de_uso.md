# Calculadora de Hashes (MD5, SHA-1, SHA-256)

Este programa permite calcular los valores hash de archivos individuales o carpetas completas, utilizando tres algoritmos criptográficos: `MD5`, `SHA-1` y `SHA-256`.

------------------------------------------------------------------------

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas

------------------------------------------------------------------------

## Cómo ejecutar el programa?

1. **Descarga o descomprime** el contenido de la carpeta.
2. Asegúrate de que estén los siguientes archivos:
   - `main.py`
   - `utils.py`
3. Ejecuta el programa con:

```bash
python main.py
```
------------------------------------------------------------------------

## Interfaz

_ **El programa mostrará una ventana con dos botones:**

    . Seleccionar archivo: Permite elegir un archivo específico y calcula sus hashes.
    . Seleccionar carpeta: Escanea todos los archivos dentro de una carpeta seleccionada y calcula sus hashes, generando un solo log para todos.

------------------------------------------------------------------------

## ¿Qué contiene el log generado?

_ **El archivo de log incluye:**

    .Nombre del archivo
    .Ruta del archivo
    .Fecha y hora de cálculo
    .Hash MD5
    .Hash SHA-1
    .Hash SHA-256

------------------------------------------------------------------------

## Notas:

    .Todos los logs se guardan en una carpeta elegida por el usuario.
    .No se sobrescriben logs anteriores, ya que cada uno incluye fecha y hora en el nombre.

------------------------------------------------------------------------
