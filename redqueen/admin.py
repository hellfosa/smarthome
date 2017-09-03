from django.contrib import admin
from redqueen.models import Human, Message, Device, Rule

# Register your models here.
admin.site.register(Human)
admin.site.register(Message)
admin.site.register(Device)
admin.site.register(Rule)
