from django.conf.urls import url, include
from . import views
from .api import MessageResource, DeviceResource
from tastypie.api import Api
from django.conf import settings
from django.conf.urls.static import static


message_responce = MessageResource()
device_responce = DeviceResource()


v1_api = Api(api_name='v1')
v1_api.register(MessageResource())
v1_api.register(DeviceResource())



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices$', views.devices, name='Devices'),
    url(r'^device_add/$', views.device_add, name='Device_add'),
    url(r'^device/(?P<pk>[0-9]+)/$', views.device, name='Device'),
    url(r'^humans$', views.humans, name='Humans'),
    url(r'^human_add/$', views.human_add, name='Human_add'),
    url(r'^human/(?P<pk>[0-9]+)/$', views.human, name='Human'),
    url(r'^rules/$', views.rules, name='Rules'),
    url(r'^rule_add/$', views.rule_add, name='Rule_add'),
    url(r'^rule/(?P<pk>[0-9]+)/$', views.rule, name='Rule'),
    url(r'^messages/$', views.messages, name='Messages'),
    url(r'^message_add/$', views.message_add, name='Message_add'),
    url(r'^message/(?P<pk>[0-9]+)/$', views.message, name='Message'),
    url(r'^sensors/$', views.sensors, name='Sensors'),
    url(r'^blank/$', views.blank, name='main list'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^graphs/$', views.graphs, name='graphs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)