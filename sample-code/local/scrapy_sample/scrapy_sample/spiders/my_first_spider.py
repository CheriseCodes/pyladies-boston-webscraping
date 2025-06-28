'''
Step 1: Create a new Scrapy project

scrapy startproject my_project

Step 2: Create a new spider in my_project/spiders/ folder
Step 3: Run the crawler

cd my_project
scrapy crawl first  # without saving
scrapy crawl first -O first.json # with saving

Step 4 (Optional): Update settings.py to limit visits

DEPTH_LIMIT = 3

'''
import scrapy


class MyFirstSpider(scrapy.Spider):
    name = "first"
    start_urls = [
        "https://www.torontopubliclibrary.ca/search.jsp?Ntt=python&Ndrs=",
    ]
    def clean(self, data):
        if data is None:
            return data
        else:
            return data.strip()
    def parse(self, response):
        for book in response.css("div.description"): # div.description.small-9.medium-10.columns
            yield {
                "title": self.clean(book.css("div.title.align-top > a > span::text").get()),
                "author": self.clean(book.css("div.format-year > span::text").get()),
                "year": self.clean(book.css("div.format-year > div > strong > span.date::text").get()),
            }

        next_page = response.css("#search-bar-bottom > div > ul > li.pagination-next > a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
