# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:56:22 2018

@author: PATIR
"""

import scrapy


class RSpider(scrapy.Spider):
    name="reptile"
    start_urls=['http://www.27270.com/ent/meinvtupian']

    '''def MainTraverse(self,response):
        for'''
      
    def parse(self,response):
        for url in {}.fromkeys(response.css("div.MeinvTuPianBox li>a::attr(href)").extract()).keys():
            yield response.follow(url,callback=self.parseLink)
    
    
    def parseLink(self,response):
        imgSrc=response.css("div.articleV4Body img::attr(src)").extract_first()
        yield{
        'title':response.css("h1.articleV4Tit::text").extract_first(),
        'link':imgSrc
        }
        nextPage=response.css("li#nl a::attr(href)").extract_first()
        if nextPage is not None:
            yield response.follow(nextPage,callback=self.parseLink)
        

