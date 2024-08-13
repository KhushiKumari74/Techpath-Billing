from django.apps import AppConfig


class WhitelableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.whitelable'
