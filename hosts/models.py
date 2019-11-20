from django.db import models
from django.contrib.auth.models import User, Group
from services.models import ServiceModel
from hosts.validators import validate_mac_address
import uuid


def get_first_superuser():
    return User.objects.filter(is_superuser=True).first()


class OSModel(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Name of Operation System
    name = models.CharField(max_length=128, verbose_name="OS name", unique=True)

    # Version of Operation system
    version = models.CharField(max_length=32, verbose_name="Version Of OS", blank=True, null=True)

    # Release date of Operation system
    releaseDate = models.DateField(verbose_name="Released Date of OS", blank=True, null=True)

    # FK to User model
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="os_createBy")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="os_updateBy")

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    def __str__(self):
        return str(self.name) + " - " + str(self.version)

    def __unicode__(self):
        return str(self.name) + " - " + str(self.version)

    def get_name_os(self):
        return self.name


class HostModel(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # hostname of server
    hostname = models.CharField(max_length=128, verbose_name="Hostname", blank=False, null=False, unique=True)

    # FK to User model
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By",
                                 related_name="host_createBy")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By",
                                 related_name="host_updateBy")
    manageBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Manage By",
                                 related_name="host_manageBy")

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # Description/ Note to this server
    description = models.TextField(verbose_name="Description")

    # FK to ServiceModel. Contain information on installed services
    services = models.ManyToManyField(to=ServiceModel)

    # FK to OSModel. Contain information OS of server
    os = models.ForeignKey(to=OSModel, on_delete=models.SET_NULL, verbose_name="Os system of host", blank=True, null=True, related_name="host")

    def __str__(self):
        return self.hostname

    def __unicode__(self):
        return self.hostname


class NetworkCard(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # IP Address
    ipAddr = models.GenericIPAddressField(unique=True, verbose_name="IP address")

    # MAC Address
    macAddr = models.CharField(max_length=17, verbose_name="Mac Address", validators=[validate_mac_address, ])

    # Inferface name
    ifName = models.CharField(max_length=16, verbose_name="Interface Name")

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # FK to User model
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By")

    # FK to HostModel
    host = models.ForeignKey(to=HostModel, on_delete=models.CASCADE,verbose_name="Host", related_name='ipAddr')

    def __str__(self):
        return self.ipAddr

    def __unicode__(self):
        return self.ipAddr


class HostGroupModel(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Name
    name = models.CharField(max_length=128, verbose_name="Name of Host Group", unique=True)

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # FK to User model
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="host_grp_create_by")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="host_grp_update_by")
    manageBy = models.ForeignKey(to=Group, on_delete=models.SET(get_first_superuser), verbose_name="Manage By", related_name="host_grp_manage_by")

    # Description of Host Group
    description = models.TextField(verbose_name="Description")

    # FKs to HostModel
    hosts = models.ManyToManyField(to=HostModel)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



# class HostOSHistory(models.Model):
#     createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By")
#     createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
#     os = models.ForeignKey(to=OSModel, verbose_name="OS", on_delete=models.CASCADE)
#     host = models.ForeignKey(to=HostModel, verbose_name="Host", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.host.__str__() + " - " + self.os.get_name_os()
#
#     def __unicode__(self):
#         return self.host.__str__() + " - " + self.os.get_name_os()

