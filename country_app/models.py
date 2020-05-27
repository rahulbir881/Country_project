from django.db import models

class Continent(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.name

class Country(models.Model):
    name=models.CharField(max_length=50)
    flag=models.ImageField(upload_to='pics')
    area=models.IntegerField()
    population=models.IntegerField()
    choices=(
        ('Europe','Europe'),
        ('Asia','Asia'),
        ('America','America'),
        ('Africa','Africa'),
        ('Ocenia','Ocenia')
    )

    capital=models.CharField(max_length=30)
    language=models.CharField(max_length=50)
    continent=models.ForeignKey(Continent,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
