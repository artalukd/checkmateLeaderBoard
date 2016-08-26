from django.db import models

class PlayerProfile(models.Model):
    index = models.CharField(max_length= 201, primary_key = True)
    rank = models.IntegerField(default = 0)
    teamname = models.CharField(max_length=200)
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200,blank=True)
    pokemoney = models.IntegerField(default = 1000)

    def __str__(self):
        return self.user.username
