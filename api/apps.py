from django.apps import AppConfig  # type: ignore


class GatewayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
