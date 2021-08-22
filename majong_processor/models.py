from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name_text = models.CharField(max_length=10)
    def __str__(self):
        return (str(self.id) + ', ' + self.name_text)

class RoundScore(models.Model):
    id = models.IntegerField(primary_key=True)
    is1 = models.IntegerField()
    is2 = models.IntegerField()
    is3 = models.IntegerField()
    is4 = models.IntegerField()

    def __str__(self):
        return (str(self.is1) + ', ' + str(self.is2) + ', ' + str(self.is3) + ', ' + str(self.is4))

class PlayerShuffle(models.Model):
    id = models.IntegerField(primary_key=True)
    name_text = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.id) + ', ' + self.name_text)

class RoundScoreShuffle(models.Model):
    id = models.IntegerField(primary_key=True)
    is1 = models.IntegerField()
    is2 = models.IntegerField()
    is3 = models.IntegerField()
    is4 = models.IntegerField()

    def __str__(self):
        return (str(self.is1) + ', ' + str(self.is2) + ', ' + str(self.is3) + ', ' + str(self.is4))

# make two databases for shuffling access, in case when new values are not written to database after
# old records are already deleted
class DatabaseShuffle(models.Model):
    shuffle = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.shuffle))

    def get_value(self):
        return self.shuffle
