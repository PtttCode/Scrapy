import scrapy
import re


class RSpider(scrapy.Spider):
    name = "mm131reptile"
    start_urls = ['http://www.mm131.com/xinggan/list_6_2.html']
    num=[]
    count=0
    mark=True


    def parse(self,response):
        if self.mark:
            yield scrapy.Request(self.start_urls[0],callback=self.MainTraverse)
            self.mark=False
        nextTarget = response.css("dd.page a:contains('下一页')::attr(href)").extract_first()
        nextTarget = "http://www.mm131.com/xinggan/"+nextTarget
        print("abcdefg",nextTarget)
        if nextTarget is not None:
            yield scrapy.Request(nextTarget,callback=self.MainTraverse)
            #dont_filter=True意味着scrapy接收重复请求
            yield scrapy.Request(nextTarget,callback=self.parse,dont_filter=True)



    def MainTraverse(self, response):
        for url in {}.fromkeys(response.xpath('//dl[@class="list-left public-box"]/dd/a[@target="_blank"]/@href').extract()).keys():
            yield scrapy.Request(url,callback=self.parseLink)

    def parseLink(self,response):
        mark=response.css("div.content-page span.page_now::text").extract_first()
        if mark == "1":
            total=response.css("div.content-page span.page-ch::text").extract_first()
            total=int(re.sub("\D","",total))
            self.num.append(total)
            print(self.num)
        imgSrc = response.css("div.content-pic img::attr(src)").extract_first()
        nextPage = response.css("div.content-page a:contains('下一页')::attr(href)").extract_first()
        yield {
            'title': response.css("h5::text").extract_first(),
            'link': imgSrc
        }
        if nextPage is not None:
            yield response.follow(nextPage, callback=self.parseLink)
        else:
            self.count+=1
            print("Count",self.count)


