from django.db import models

def get_foodimage_path(instance, filename):
    return "food_images/%s" % filename

def get_image_path(instance, filename):
    ext = filename.split(".")[-1]
    if isinstance(instance, Brand):
        return f"{instance.name}/brand_img.{ext}"
    return f"{instance.brand.name}/{instance.id}_img.{ext}"

class Brand(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, unique=True, default="Anoymous")
    desc = models.TextField(max_length=512, null=True, blank=False)
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name
    
class Drinks(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)
    price = models.PositiveIntegerField(default=None, null=True)
    desc = models.TextField(max_length=1024, null=True, blank=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.DO_NOTHING, null=True, default=None,related_name='drinks')
    image = models.ImageField(upload_to=get_image_path, null=True)
    food_images = models.ImageField(upload_to=get_foodimage_path)
    likes = models.PositiveIntegerField(default=0, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name