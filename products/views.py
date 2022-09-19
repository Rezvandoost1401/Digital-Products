
from django.views.generic import TemplateView
from django.shortcuts import render

from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer





class IndexPageview(TemplateView):
    
    def get(self, request, **kwargs):
        product_data = []
        all_products = Product.objects.all()[:3]

        for product in all_products:
            product_data.append({
                'title': product.title,
                'cover': product.avatar.url,
                #'category': product.categories.title,
                #'category': ProductSerializer('categoreis'),
                'created_at': product.created_time.date,
            })

        context = {
            'product_data' : product_data
        }

        return render(request, 'index.html', context)




class CategoryListView(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)



class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)



class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)



class ProductDetailView(APIView):
    
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get (self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get (self, request, product_id, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f, context={'request': request})
        return Response(serializer.data)
