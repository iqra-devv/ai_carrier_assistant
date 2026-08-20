from django.db import models

# Create your models here.
class Skill(models.Model):

    name = models.CharField(
        max_length = 100,
        unique = True
    )

    category = models.CharField(
        max_length=100,
        blank = True,
        null = True,
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        auto_now = True,
    )


    def save(self,*args,**kwargs):
        self.name = self.name.strip().lower()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name