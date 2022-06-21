from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=20)
    Language =models.ForeignKey("Language",  on_delete=models.CASCADE)

    def __str__(self):
        return self.name    


  
"""
CASCADE = si efface parent alors efface enfant
PROTECT = efface que parent
SET_NULL = met null a la place
SET_DEFAULT = met valeur decider par default a la plce
DO_NOTHTING = laisse comme c est (a ne pas faire)

"""