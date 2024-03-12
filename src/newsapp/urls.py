
from django.urls import path, include
from newsapp.views import FetchArticleView

urlpatterns = [
   
    path("", FetchArticleView.as_view(), name="fetch_news"),
]
