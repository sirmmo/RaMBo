from django.contrib import admin

from models import *

admin.site.register(Resource)
admin.site.register(ResourceCategory)
admin.site.register(ResourceProperty)

admin.site.register(UserConnection)
admin.site.register(ConnectionRequest)
