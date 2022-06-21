from django.db import models
from django.contrib.auth.models import User

# ONE TO MANY
# UN LANGUAGE A PLUSIEURS FRAMEWORK
# CHAQUE FRAMEWORK N'A QUE 1 LANGUAGE

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

# MANY TO MANY
# UNE ECOLE A PLUSIEURS ETUDIANTS 
# UN ETUDIANT PEUVENT AVOIR  PLUSIEURS ECOLES
# UN ETUDIANT DOIT AVOIR AU MOIN UNE ECOLE

# fais une 3eme table de rapport entre les 2

class School(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    school = models.ManyToManyField(School)
    
    def __str__(self):
        return self.name
    
    
# ONE TO ONE
# chaque user a 1 profile
# chaue profile a 1 user
# mais aucin rapport entre chaqu un

class Profile(models.Model):
    school = models.CharField( max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.name