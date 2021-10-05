from django.conf import settings 
from django.db import models


class statuscategory(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category



class statusdescription(models.Model):
    author=models.CharField (max_length=20)
    description=models.TextField()
    time=models.CharField(max_length=10)
    

    status_category=models.ForeignKey(
        'statuscategory',
         on_delete=models.CASCADE
        
        )
   
   

    def __str__(self):
        if len(self.description)>50:
            return self.description[:50]+"..."
        return self.description




   


