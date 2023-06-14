import scrapy
from ..items import ParamsItem

class WeplaySpider(scrapy.Spider):
    name = "weplay"
    allowed_domains = ['www.weplay.cl']
    start_urls = [
        'https://www.weplay.cl/juegos.html',
        'https://www.weplay.cl/accesorios.html',
        'https://www.weplay.cl/consolas.html',
        'https://www.weplay.cl/tecnologia.html',
        'https://www.weplay.cl/ropa.html',
        'https://www.weplay.cl/figuras-y-juguetes.html'
    ]

    def parse(self, response):
        # Aquí se realiza el procesamiento y extracción de los datos de la página
        # Puedes utilizar selectores CSS o XPath para seleccionar y extraer los elementos

        # Ejemplo de extracción de elementos:
        for item in response.css('.product-item-details'):
            title = item.css('.product-item-link::text').get().strip()
            link = item.css('::attr(href)').get()
            price = item.css('.price::text').get()
            special_price = item.css('.special-price .price ::text').get()

            # Crear una instancia del item y pasar los valores extraídos
            params = ParamsItem()
            params['title'] = title
            params['link'] = link
            params['price'] = price
            params['special_price'] = special_price

            yield params
