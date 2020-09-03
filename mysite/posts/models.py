from django.db import models
from drinks.models import Drinks

class Blog(models.Model):
    title=models.CharField(max_length=200)
#    likes=models.IntegerField(default=0, null=False)
#    drink = models.ForeignKey(to=Drinks,on_delete=models.CASCADE,related_name="posts")
#    account = models.ForeignKey(
#        to=get_user_model(), on_delete=models.DO_NOTHING, related_name="posts"
#    )
#    content = models.TextField(blank=True, null=False, default="")
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
