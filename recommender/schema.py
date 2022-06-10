import graphene
from graphene_django import DjangoObjectType

from .models import Movie, Rating
from graphql import GraphQLError
from django.db.models import Q


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class RatingType(DjangoObjectType):
    class Meta:
        model = Rating


class Query(graphene.ObjectType):
    movies  = graphene.List(MovieType)
    ratings = graphene.List(RatingType)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_ratings(self, info, **kwargs):
        return Rating.objects.all()

