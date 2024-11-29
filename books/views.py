from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(request):
	books = Book.objects.all()
	serializer = BookSerializer(books, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def get_book_by_id(request, pk):
	book = Book.objects.get(id=pk)
	serializer = BookSerializer(book, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
	serializer = BookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def update_book_by_id(request, pk):
	book = Book.objects.get(id=pk)
	serializer = BookSerializer(instance=book, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def delete_book_by_id(request, pk):
	book = Book.objects.get(id=pk)
	book.delete()
	return Response('Book was successfully deleted!')
