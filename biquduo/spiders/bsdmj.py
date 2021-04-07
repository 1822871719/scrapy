import scrapy
from biquduo.items import BiquduoItem

class BsdmjSpider(scrapy.Spider):
    name = 'bsdmj'
    allowed_domains = ['www.vbiquge.com']
    start_urls = ['https://www.vbiquge.com/85_85133/136574.html']

    def parse(self, response):
        item = BiquduoItem()
        item["bookname"] = response.xpath("//div[@class='con_top']//a[3]/text()").extract()
        item["chaptername"] = response.xpath("//div[@class='bookname']//h1/text()")[0].extract()
        item["chapter"] = response.xpath("//div[@id='content']/text()").extract()
        next_page_link = response.xpath('//div[@class="bottem2"]/a[3]/@href').extract()
        if len(next_page_link[0]) > 10:
            next = "https://"+self.allowed_domains[0] + next_page_link[0]
            yield scrapy.Request(next,
                                 callback=self.parse)
        yield item
