from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth'
    def ready(self):
         print(f'{self.name} -> initialized')