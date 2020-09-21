from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class DataFile(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True,
                            null=True, related_name='children')

    class MPTTMeta:
        order_by_insertion = ['name']

    def __str__(self):
        return self.name
