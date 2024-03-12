import requests
from celery import shared_task
from time import sleep
from newsapp.models import Article 



@shared_task
def check_running():
    print("news is fetching")
    print("sleeping for 10 sec")
    sleep(10)
    print("news fetch")


@shared_task
def fetch_and_store_news():

    URL = "https://newsapi.org/v2/top-headlines?country=in&apiKey=88fa1355f64c4c75abbee545c1b86344"
    response = requests.get(url=URL)
    if(response.status_code != 200):
        pass
    data = response.json()
    total_results = data['totalResults'] 
        
    for article in data['articles']:
    # Check if the article already exists in the database based on unique identifier (e.g., title)
        if not Article.objects.filter(title=article.get('title')).exists():
            Article.objects.create(
                source_id =  article['source']['id'] if article['source']['id'] else None,
                source_name =  article['source']['name'] if article['source']['name'] else None,
                author = article['author'] if article['author'] else None,
                title = article['title'] ,
                description = article['description'] if article['description'] else None,
                url = article['url'] if article['url'] else None,
                url_to_image = article['urlToImage'] if article['urlToImage'] else None,
                published_at = article['publishedAt'] if article['publishedAt'] else None,
            )
            print("Article Added")