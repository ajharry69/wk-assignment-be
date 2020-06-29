from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'person'

    # noinspection PyUnresolvedReferences
    def ready(self):
        from person import signals
