from django.apps import AppConfig


class GunlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gunler'

    def ready(self):
        import gunler.signals