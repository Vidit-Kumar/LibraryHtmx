from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json
from .. import models
from . import serializers


class CheckoutEndpoint(APIView):

    def post(self, request, *args, **kwargs):
        try:
            book_id = request.data['pk']
            book = models.Library.objects.get(pk=book_id)
        except models.Library.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        if not book.is_in_stock:
            return Response({"error": "Book already checked out"}, status=status.HTTP_409_CONFLICT)

        book.is_in_stock = False
        book.save()  # Saves and updates dateCheckedOut
        book_serializer = serializers.LibraryModelSerializer(book)  # Serialize the updated book
        return Response(book_serializer.data, status=status.HTTP_200_OK)    


class BooksEndpoint(APIView):

    def get(self, request, *args, **kwargs):
        books = models.Library.objects.all()
        serialized_data = serialize("json", books)
        return JsonResponse({'book_list': json.loads(serialized_data)}, status=status.HTTP_200_OK)