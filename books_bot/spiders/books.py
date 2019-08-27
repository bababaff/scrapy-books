# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


def product_info(response, value):
    return response.xpath(f"//th[text()='{value}']/following-sibling::td/text()").get()


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').getall()

        for book in books:
            abs_book_url = response.urljoin(book)

            yield Request(abs_book_url, callback=self.parse_book)

        # Process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').get()
        abs_next_page_url = response.urljoin(next_page_url)

        if next_page_url:
            # Here because we're in the parse function we don't need to mention the callback
            yield Request(abs_next_page_url)

    def parse_book(self, response):
        title = response.xpath("//h1/text()").get()
        price = response.xpath("//*[@class='price_color']/text()").get()

        img_url = response.xpath("//img/@src").get()
        img_url = img_url.replace('../../', 'http://books.toscrape.com/')

        rating = response.xpath(
            "//*[contains(@class, 'star-rating')]/@class").get()
        rating = rating.split(" ")[-1]

        # description = response.xpath("//article/p/text()").get()
        description = response.xpath(
            "//*[@id='product_description']/following-sibling::p/text()").get()

        # Product Information Data Points
        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')
        price_without_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        number_of_reviews = product_info(response, 'Number of reviews')

        yield {
            'title': title,
            'price': price,
            'img_url': img_url,
            'rating': rating,
            'description': description,
            'upc': upc,
            'product_type': product_type,
            'price_without_tax': price_without_tax,
            'price_with_tax': price_with_tax,
            'tax': tax,
            'availability': availability,
            'number_of_reviews': number_of_reviews
        }
