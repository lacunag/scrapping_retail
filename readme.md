# Proyecto de Scrapping Empresas Retail

Este proyecto tiene como objetivo realizar la extracción de datos de empresas retail utilizando la biblioteca Scrapy en Python. Permite obtener información relevante de diferentes sitios web de empresas del sector retail, como nombres de productos, precios, descripciones, etc.

## Requerimientos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes requisitos:

- Python 3.6 o superior: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Scrapy: Para instalar Scrapy, ejecuta el siguiente comando en tu terminal:

    ```
    pip install scrapy
    ```

## Ejecución

Sigue estos pasos para ejecutar el proyecto:

1. Clona este repositorio en tu máquina local o descárgalo como archivo ZIP.

2. Abre una terminal y navega hasta el directorio raíz del proyecto.

3. Ejecuta el proyecto con el siguiente comando:

    ```
    scrapy crawl <nombre-del-spider>
    ```

    Lista completa de los Spider creados.

    ```
    scrapy list
    ```

    Reemplaza `<nombre-del-spider>` con el nombre del spider que deseas ejecutar. 

    ```
    scrapy crawl retail_spider
    ```

4. Espera a que el scrapping se complete y los datos sean extraídos. Los resultados se mostraran por pantalla.

¡Eso es todo! Ahora puedes utilizar este proyecto como punto de partida para extraer datos de empresas retail utilizando Scrapy y Python.