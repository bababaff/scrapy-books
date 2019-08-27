# Scrapy Books Bot
This is a Scrapy project to scrape books data from http://books.toscrape.com.

## Extracted data

This project extracts all the books data from http://books.toscrape.com.
The extracted data looks like this sample:

    {  
        "title":"Soumission",
        "price":"£50.10",
        "img_url":"http://books.toscrape.com/media/cache/ee/cf/eecfe998905e455df12064dba399c075.jpg",
        "rating":"One",
        "description":"Dans une France assez proche de la .....",
        "upc":"6957f44c3847a760",
        "product_type":"Books",
        "price_without_tax":"£50.10",
        "price_with_tax":"£50.10",
        "tax":"£0.00",
        "availability":"In stock (20 available)",
        "number_of_reviews":"0"
     }


## Spiders

This project contains a spider and you can list them using the `list`
command:

    $ scrapy list
    books

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl books

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl books -o books.json
