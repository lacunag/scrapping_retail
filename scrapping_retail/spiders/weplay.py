import scrapy


class WeplaySpider(scrapy.Spider):
    name = "weplay"
    allowed_domains = ["weplay.cl"]
    start_urls = ["https://weplay.cl"]

    def parse(self, response):
        pass
