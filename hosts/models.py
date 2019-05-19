from django.db import models
from django.contrib.auth.models import User, Group
from services.models import ServiceModel
import uuid


def get_first_superuser():
    return User.objects.filter(is_superuser=True).first()


class HostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    hostname = models.CharField(max_length=128, verbose_name="Hostname", blank=False, null=False)

    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="host_create_by")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="host_update_by")

    description = models.TextField(verbose_name="Description")
    services = models.ManyToManyField(to=ServiceModel)

    def __str__(self):
        return self.hostname

    def __unicode__(self):
        return self.hostname


class HostGroupModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name="OS name", unique=True)
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="host_grp_create_by")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="host_grp_update_by")
    manageBy = models.ForeignKey(to=Group, on_delete=models.SET(get_first_superuser), verbose_name="Manage By", related_name="host_grp_manage_by")

    description = models.TextField(verbose_name="Description")
    hosts = models.ManyToManyField(to=HostModel)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class HostIPHistoryModel(models.Model):
    ipAddr = models.GenericIPAddressField(unique=True)
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By")
    host = models.ForeignKey(to=HostModel, on_delete=models.CASCADE,verbose_name="Host", )
    isPrimary = models.BooleanField(verbose_name="Is Primary Network Card", default=False)
    isDisabled = models.BooleanField(verbose_name="Is Network Card Disabled", default=False)

    class Meta:
        unique_together = ('host', 'isPrimary')

    def __str__(self):
        return self.ipAddr

    def __unicode__(self):
        return self.ipAddr



class OSModel(models.Model):
    name = models.CharField(max_length=128, verbose_name="OS name", unique=True)
    version = models.CharField(max_length=32, verbose_name="Version Of OS", blank=True, null=True)
    releaseDate = models.DateField(verbose_name="Released Date of OS", blank=True, null=True)

    def __str__(self):
        return str(self.name) + str(self.version)

    def __unicode__(self):
        return str(self.name) + str(self.version)

    def get_name_os(self):
        return self.name

class HostOSHistory(models.Model):
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By")
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    os = models.ForeignKey(to=OSModel, verbose_name="OS", on_delete=models.CASCADE)
    host = models.ForeignKey(to=HostModel, verbose_name="Host", on_delete=models.CASCADE)

    def __str__(self):
        return self.host.__str__() + " - " + self.os.get_name_os()

    def __unicode__(self):
        return self.host.__str__() + " - " + self.os.get_name_os()

