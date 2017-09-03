from django.apps import AppConfig
from django.db.models import signals

class RedqueenConfig(AppConfig):

    name = 'redqueen'

    def ready(self):
        from django.contrib.auth.models import User
        from tastypie.models import create_api_key

        # This line dispatches signal to Tastypie to create APIKey
        signals.post_save.connect(create_api_key, sender=User)