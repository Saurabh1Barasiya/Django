from django.apps import AppConfig

# yaha kaam karne ke baad hamko __init__.py par jayege.

class BlogConfig(AppConfig):
    name = 'blog'

    # ye likhna h yaha.
    def ready(self):    
        import blog.signals
