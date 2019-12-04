from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User, Group
from services.models import ServiceModel
from hosts.validators import validate_mac_address
import uuid


def get_first_superuser():
    return User.objects.filter(is_superuser=True).first()


class HostModel(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # hostname of server
    hostname = models.CharField(max_length=128, verbose_name="Hostname", blank=False, null=False, unique=True)

    # Full qualified domain name
    fqdn = models.CharField(max_length=128, verbose_name="Full qualified domain name", null=True)

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

    # Number of CPU core
    numCpuCore = models.IntegerField(null=True, verbose_name="Number of CPU core")

    # Size of Ram in mb
    ramSize = models.IntegerField(null=True, verbose_name="Size of Ram")

    # Size of Disk
    diskSize = models.IntegerField(null=True, verbose_name="Size of Disk")

    def __str__(self):
        return self.hostname

    def __unicode__(self):
        return self.hostname


class OSModel(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # FK to User model
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By",
                                 related_name="os_createBy")
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By",
                                 related_name="os_updateBy")

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # Name of Operation System
    name = models.CharField(max_length=128, verbose_name="OS name", unique=True)

    # Version of Operation system
    version = models.CharField(max_length=32, verbose_name="Version Of OS", blank=True, null=True)

    # Release date of Operation system
    releaseDate = models.DateField(verbose_name="Released Date of OS", blank=True, null=True)

    def __str__(self):
        return str(self.name) + " - " + str(self.version)

    def __unicode__(self):
        return str(self.name) + " - " + str(self.version)

    def get_name_os(self):
        return self.name


class NetworkCard(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # MAC Address
    macAddr = models.CharField(unique=True, max_length=17, verbose_name="Mac Address", validators=[validate_mac_address, ])

    # Inferface name
    ifName = models.CharField(max_length=16, verbose_name="Interface Name")

    # Status of interface
    isUp = models.BooleanField(default=False, verbose_name="Status of Interface")

    # Is in use
    isInUse = models.BooleanField(default=False, verbose_name="Interface in using")

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # FK to User model
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="nic_updateby")
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="nic_createby")

    # FK to HostModel
    hostID = models.ForeignKey(to=HostModel, on_delete=models.CASCADE,verbose_name="Host", related_name='nic_host')

    def __str__(self):
        return self.macAddr

    def __unicode__(self):
        return self.macAddr


class IpAddrMapNIC(models.Model):
    # id with uuid values
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # FK to Network card ID
    nicID = models.ForeignKey(to=NetworkCard, on_delete=models.CASCADE, verbose_name="Network Card ID", related_name='ipAddr_nic')

    # Datetime fields
    createDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Updated")
    updateDate = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    # FK to User model
    updateBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Update By", related_name="mapip_updateby")
    createBy = models.ForeignKey(to=User, on_delete=models.SET(get_first_superuser), verbose_name="Create By", related_name="mapip_createby")

    # Ip Address
    ipAddr = models.GenericIPAddressField(blank=False, null=False, verbose_name="Ip Address")

    # Subnet
    subnetMask = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(32)])

    # Is in use
    isInUse = models.BooleanField(default=False, verbose_name="Interface in using")


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

