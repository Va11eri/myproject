from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # Уникальное ограничение для поля email
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.email


class Coords(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)


class PerevalAdded(models.Model):
    id = models.AutoField(primary_key=True)
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    winter_level = models.CharField(max_length=255, blank=True)
    summer_level = models.CharField(max_length=255, blank=True)
    autumn_level = models.CharField(max_length=255, blank=True)
    spring_level = models.CharField(max_length=255, blank=True)
    images = models.ManyToManyField(Image, through='PerevalImages')
    status = models.CharField(
        max_length=255,
        choices=(
            ('new', 'New'),
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        )
    )

    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    id = models.AutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField()

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    id = models.AutoField(primary_key=True)
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_images'


class SprActivitiesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'
