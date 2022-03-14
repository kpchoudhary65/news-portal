import requests
from django.core.management.base import BaseCommand
from newsapp.models import News
from newsapp.serializers import NewsSerializer

API_KEY = "3527fc1ea7734d8b9afdad14c4be8266"


class Command(BaseCommand):
    help = "Create news"

    def handle(self, *args, **options):
        News.objects.all().delete()

        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        response_data = requests.get(url).json()
        data = [d for d in response_data["articles"] if d["urlToImage"] != "" and d["urlToImage"] is not None]
        response = NewsSerializer(data=data, many=True)
        response.is_valid(raise_exception=True)
        response.save()
