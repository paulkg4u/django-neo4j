from django.db import models

# Create your models here.
from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom
)

from django_neomodel import DjangoNode


class Person(DjangoNode):
    name = StringProperty()
    age = IntegerProperty()
    friends = RelationshipTo('Person', 'FRIENDS')
    acted_in = RelationshipFrom('Movie', 'ACTED_IN')

    class Meta:
        app_label = 'user'


class Movie(DjangoNode):
    title = StringProperty()
    year = IntegerProperty()
    actors = RelationshipTo('Person', 'ACTED_IN')
    directors = RelationshipTo('Person', 'DIRECTED')

    class Meta:
        app_label = 'user'
