from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50, unique=True)
    longtitude = models.FloatField(unique=True)
    latitude = models.FloatField(unique=True)
    covid = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name


class HospitalUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.username


class Blood(models.Model):
    type = models.CharField(max_length=5)
    count = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.type


class FindById(models.Model):
    national_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=25)
    date_of_lost = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=5, default='')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class FindByClothe(models.Model):
    shirt_color = models.CharField(max_length=10)
    trouser_color = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10)
    skin_color = models.CharField(max_length=10)
    height = models.CharField(max_length=5)
    gender = models.CharField(max_length=5, default='')
    date_of_lost = models.DateTimeField(auto_now_add=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)


class Room(models.Model):
    number = models.IntegerField(null=False)
    price = models.IntegerField()
    type = models.CharField(max_length=10)
    available = models.BooleanField(null=False, default=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.number
