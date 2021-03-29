from rest_framework import serializers
from books.models import Books

"""
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    authors = serializers.CharField(required=False, allow_blank=True, max_length=100)
    publisher = serializers.CharField(required=False, allow_blank=True, max_length=100)
    publication_date = serializers.DateTimeField(required=False)
    number_of_pages = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.save()
        return instance
"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'authors', 'publisher', 'publication_date', 'number_of_pages']