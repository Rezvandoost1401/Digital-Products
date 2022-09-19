
from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Category
        fields = ('id', 'title', 'description', 'avatar', )




class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = File
        fields = ('id', 'title', 'file', )



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta :
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files',)


