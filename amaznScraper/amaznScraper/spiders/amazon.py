# -*- coding: utf-8 -*-
import scrapy
from ..items import AmaznscraperItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    page_number = 2

    start_urls = ['https://www.amazon.in/s?k=book&ref=nb_sb_noss']

    def parse(self, response):
        items = AmaznscraperItem()

        productTitle = response.css('#dealTitle .a-declarative').css('::text').extract()
        dealPrice = response.css('.a-row .layer .backGround').css('::text').extract()
        originalPrice = response.css('.a-text-strike::text').extract()
        thumbnail = response.css('.s-image::attr(src)').extract()
        productLink = response.css('#dealTitle .a-declarative').css('::attr(href)').extract()

        items['productTitle'] = productTitle
        items['dealPrice'] = dealPrice
        items['originalPrice'] = originalPrice
        items['thumbnail'] = thumbnail
        items['productLink'] = productLink

        yield items

        # next_page = 'https://www.amazon.in/gp/goldbox/ref=gbps_ftr_s-4_42f8_page_' + str(
         #   AmazonSpider.page_number) + '?gb_f_c2xvdC00=dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,page:2,sortOrder:BY_SCORE,dealsPerPage:48&pf_rd_p=54fdcd6b-da8c-4a8d-a66d-2e41c6b742f8&pf_rd_s=slot-4&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=QQRWPNYGWXCT6AHVDMRN&ie=UTF8'
        # if AmazonSpider.page_number <= 209:
         #   AmazonSpider.page_number += 1
          #  yield response.follow(next_page, callback=self.parse)
