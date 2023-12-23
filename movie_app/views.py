from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, Review

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)



@api_view(['GET'])
def directors_view(request):
    # Step 1. Collect directors from DB
    directors = Director.objects.all()

    # Step 2. Serialize directors
    serializer = DirectorSerializer(directors, many=True)
    # Step 3. Return serialized directors
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_list_view(request):
    # Step 1. Collect directors from DB
    movies = Movie.objects.all()

    # Step 2. Serialize directors
    serializer = MovieSerializer(movies, many=True)
    # Step 3. Return serialized directors
    return Response(data=serializer.data)