from django.db import models

class Score(models.Model):
    def __str__(self):
        return self.score
    
    score = models.CharField(max_length=255, nullable = False)