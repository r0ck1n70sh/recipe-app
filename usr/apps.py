from django.apps import AppConfig


class UsrConfig(AppConfig):
    name = 'usr'
    def ready(self):
        import usr.signals
