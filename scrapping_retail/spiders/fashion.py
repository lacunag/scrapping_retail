import scrapy
from ..items import ParamsItem

class FashionSpider(scrapy.Spider):
    name = "fashion"
    allowed_domains = ["fashion.com"]
    start_urls = [
        'https://fashionspark.com/hombre/hombre-juvenil/polar.html',
        'https://fashionspark.com/hombre/hombre-juvenil/chaquetas.html',
        'https://fashionspark.com/hombre/hombre-juvenil/polerones.html',
        'https://fashionspark.com/hombre/hombre-juvenil/parkas.html',
        'https://fashionspark.com/hombre/hombre-juvenil/pantalones.html',
        'https://fashionspark.com/hombre/hombre-juvenil/buzos-y-joggers.html',
        'https://fashionspark.com/hombre/hombre-juvenil/jeans.html',
        'https://fashionspark.com/hombre/hombre-juvenil/poleras.html',
        'https://fashionspark.com/hombre/hombre-juvenil/camisas.html',
        'https://fashionspark.com/hombre/hombre-juvenil/sweaters.html',
        'https://fashionspark.com/hombre/hombre-sport/poleras.html',
        'https://fashionspark.com/hombre/hombre-sport/buzos.html',
        'https://fashionspark.com/hombre/hombre-sport/polerones.html',
        'https://fashionspark.com/hombre/hombre-sport/chaquetas.html',
        'https://fashionspark.com/hombre/ropa-interior/pijamas.html',
        'https://fashionspark.com/hombre/ropa-interior/calcetines.html',
        'https://fashionspark.com/hombre/ropa-interior/boxer.html'

    ]

    def parse(self, response):
        productos = response.css('li.item.product.product-item')
        
        for item in productos:
            title           = item.css('.product-item-name a::text').get().strip()
            special_price   = item.css('.price-container.price-final_price .price-wrapper .price::text').get()
            link            = item.css('.product-item-link::attr(href)').get()
            price           = item.css('.price-box .old-price .price-wrapper .price::text').get()

            params = ParamsItem()
            params['title'] = title
            params['special_price'] = special_price
            params['link'] = link
            params['price'] = price

            yield params