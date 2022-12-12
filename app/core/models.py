from django.db import models
from django.db.models.signals import post_save, pre_delete
from core.utils import image_directory_path
from core.signals import format_img, file_cleanup


class Item(models.Model):

    STATUS_OPTS = [
        (1, "In stock"),
        (2, "Preorder"),
        (3, "Arrival expected"),
        (4, "Not Avaliable"),
        (5, "Not manufactured"),
    ]

    title = models.CharField(max_length=255, default='')
    number = models.PositiveIntegerField(unique=True)
    price = models.PositiveIntegerField()
    status = models.PositiveIntegerField(choices=STATUS_OPTS)
    image = models.ImageField(upload_to=image_directory_path)


    def __str__(self):
        return f'{self.title}'
post_save.connect(format_img, sender=Item, dispatch_uid='Item.format_img')
pre_delete.connect(file_cleanup, sender=Item, dispatch_uid='Item.file_cleanup')