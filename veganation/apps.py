from django.apps import AppConfig


class VeganationConfig(AppConfig):
    name = 'veganation'

    def ready(self):
        import veganation.signals