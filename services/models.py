from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
import uuid


def get_first_superuser():
    return User.objects.filter(is_superuser=True).first()


class ServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64, verbose_name="Service Name")
    port = models.CharField(max_length=32, validators=[validate_comma_separated_integer_list])
    description = models.TextField(verbose_name='Description', blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="srv_create_by")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="srv_update_by")

    class Meta:
        unique_together = ('name', 'port')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

