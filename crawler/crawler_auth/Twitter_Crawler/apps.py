from django.apps import AppConfig


class TwitterManualCrawlerConfig(AppConfig):
    name = 'Twitter_Crawler'
    def ready(self):
         print(f'{self.name} -> initialized')