from django.contrib import admin
from hosts.models import *


admin.site.register(HostModel)
admin.site.register(HostGroupModel)
admin.site.register(HostIPHistoryModel)
admin.site.register(OSModel)
admin.site.register(HostOSHistory)
