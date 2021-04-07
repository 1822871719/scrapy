import scrapy
from biquduo.items import Biquduo__Item


class QftSpider(scrapy.Spider):
    name = 'qft'
    allowed_domains = ['www.bjcan.com']
    start_urls = ['http://www.bjcan.com/chapter/57249/441db1e986e04.html']

    def parse(self, response):
        item = Biquduo__Item()
        item["bookname"] = response.xpath('//div[@class="crumbs-nav"]/a[4]/text()').extract()
        item["chaptername"] = response.xpath("//h3/text()")[0].extract()
        item["chapter"] = response.xpath("//div[@class='read-content j_readContent']/p/text()").extract()
        next_page_link = response.xpath("//a[@id='j_chapterNext']/@href").extract()
        if "398d91ac84363" not in next_page_link:
            # next = "https://"+self.allowed_domains[0] + next_page_link[0]
            yield scrapy.Request(next_page_link[0],
                                 callback=self.parse)
        else:
            pass
        # print(item, next_page_link[0])
        yield item
        print(self.name)
