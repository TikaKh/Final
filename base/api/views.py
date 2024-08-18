from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Books
from .serializers import BookSerializer
@api_view(['GET'])
def get_routes(request):
    routes=[
        'GET/api'
        'GET/api/books'
        'GET/api/book/:id'

    ]
    return Response(routes)
@api_view(['GET'])
def get_books(request):
    books=Books.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_book(request,id):
    book = Books.objects.get(id=id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)