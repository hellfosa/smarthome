from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from .models import Message, Device
from django.conf.urls import url

class MessageResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        fields = ['channel', 'signal']
        allowed_methods = ['get', 'put', 'post']
        include_resource_uri = False
        detail_uri_name = 'message_uuid'
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()

class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'device'
        fields = ['name', 'channel', 'value', 'group', 'action']
        allowed_methods = ['get', 'put', 'post']
        include_resource_uri = False
        detail_uri_name = 'device_uuid'
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()

def prepend_urls(self):
    return [
        url(r"^(?P<resource_name>%s)/$" % self._meta.resource_name,
            self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
    ]