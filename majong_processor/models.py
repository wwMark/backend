from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name_text = models.CharField(max_length=10)
    def __str__(self):
        return (str(self.id) + ', ' + self.name_text)

class Round(models.Model):
    id = models.BigAutoField(primary_key=True)

class Score(models.Model):
    score = models.IntegerField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)

