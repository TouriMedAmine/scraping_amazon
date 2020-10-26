# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scrapy
from ..importitems import BookItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1603731994&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0",
        ]
    
    def parse(self, response):
        item = BookItem()
        book_name = response.css('.a-color-base.a-text-normal').extract()
        book_author = response.css('.a-color-secondary .a-size-base.a-link-normal').extract()
        book_price = response.css('.a-spacing-top-small .a-price-whole').extract()
        book_imageLink = response.css('.s-image').extract()
        