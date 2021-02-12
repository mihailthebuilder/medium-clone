from django.shortcuts import render
from .models import Article
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return Response({"articles": articles})
