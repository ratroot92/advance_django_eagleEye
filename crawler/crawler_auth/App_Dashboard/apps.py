from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'App_Dashboard'
    def ready(self):
         print(f'{self.name} -> initialized')