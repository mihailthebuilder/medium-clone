from django.shortcuts import render
from .models import Article
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        print(serializer.data[0]["title"])
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get("article")

        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response(
            {"success": "Article '{}' created successfully.".format(article_saved)}
        )
