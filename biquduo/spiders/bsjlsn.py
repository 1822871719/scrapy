import scrapy
from biquduo.items import BiquduoItem


class DsxSpider(scrapy.Spider):
    name = 'bsjlsn'
    allowed_domains = ['www.bqg5.cc']
    start_urls = ['https://www.bqg5.cc/114_114800/165881699.html']

    def parse(self, response):
        item = BiquduoItem()
        item["bookname"] = response.xpath("//div[@class='con_top']//a[3]/text()").extract()
        item["chaptername"] = response.xpath("//div[@class='bookname']//h1/text()")[0].extract()
        item["chapter"] = response.xpath("//div[@id='content']/p/text()").extract()
        next_page_link = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract()
        if len(next_page_link[0]) > 12:
            next = "https://"+self.allowed_domains[0] + next_page_link[0]
            yield scrapy.Request(next,
                                 callback=self.parse)
        yield item
