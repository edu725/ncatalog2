from django.db import models
from users.models import User

class Clothing(models.Model):
    title = models.CharField(max_length=200)
    path = models.ImageField(upload_to="img/%Y/%m/%d/", blank=True)
    description = models.TextField()

    def total_likes(self):
        return Like.objects.filter(clothing=self).count()
    
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'clothing')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} on {self.clothing}'