#before running this code, we will need to create a project with scrapy
#we can do this by running the command: scrapy startproject myproject

import scrapy

#this class creates a new spider
#"name" is used to run this spider. i.e. "scrapy crawl description"
#start_urls is a list of URLs where the spider will begin to crawl from
#async def start is an asynchronous method that tells scrapy how to 
#start crawling and use async features if needed
#for each URL in start_urls, it yields a scrapy.Requests object. 
#the callback is set to self.parse_description, so the response will be handled by 
#that method.

class MySpiderProject(scrapy.Spider): 
    name = "description" 
    start_urls = ["https://targetwebsite"]

    async def start(self): 
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_description) 


#this method is called for each response from the URLs. 
#it uses xpath to extract the content of the <meta name = "description"> tag from the HTML
    def parse_description(self, response): 
        description = response.xpath('//meta[@name="description"]/@content').get()
        print("Description:", description)