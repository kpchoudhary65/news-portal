import requests
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import News
from .serializers import NewsSerializer

API_KEY = "3527fc1ea7734d8b9afdad14c4be8266"


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def create(self, request, *args, **kwargs):
        """News Portal Json data

        :param _type_ request: Get all data in 3rd party API and store in DB
        :return _type_: response data
        """
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        response_data = requests.get(url).json()
        data = [d for d in response_data["articles"] if d["urlToImage"] != "" and d["urlToImage"] is not None]
        response = self.serializer_class(data=data, many=True)
        response.is_valid(raise_exception=True)
        response.save()
        return Response(
            {
                "status": status.HTTP_201_CREATED,
                "message": "Record created",
                "data": response.data,
            }
        )

    def retrieve(self, request):
        """Retrieve all News data

        :param _type_ request: Get all data in json formate
        :return _type_: response data
        """
        news_obj = News.objects.filter()
        news_res = NewsSerializer(news_obj, many=True)
        return Response({news_res.data})
