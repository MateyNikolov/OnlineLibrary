from django.db import models


class Profile(models.Model):

    NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )
    image_url = models.URLField()


class Book(models.Model):

    BOOK_MAX_LENGTH = 30

    title = models.CharField(
        max_length=BOOK_MAX_LENGTH
    )
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(
        max_length=BOOK_MAX_LENGTH
    )
