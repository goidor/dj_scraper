# dj_scraper

#### Steps to test the spiders:

* git clone https://github.com/goidor/dj_scraper.git
* cd dj_scraper/dj_scraping/
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py scrapy crawl nhsnetwork
* ./manage.py scrapy crawl rcplondon

#### To save the output to a file .json:

* ./manage.py scrapy crawl rcplondo -o file.json
