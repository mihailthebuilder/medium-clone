from rest_framework import serializers

# we could use a model serializer instead of this, but it's useful to know this case
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)