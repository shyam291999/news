import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from newsapp.models import Article
from newsapp.serializers import ArticleSerializer
from newsapp.tasks import check_running


class FetchArticleView(APIView):

    def get(self, request):
        check_running.delay()
        return Response({"message": "Welcome to News"}, status=status.HTTP_200_OK)
