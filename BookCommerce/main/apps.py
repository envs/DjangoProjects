from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        #return super().ready()
        from . import signals