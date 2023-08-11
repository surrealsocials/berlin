from django.contrib import admin
from .models import NewsArticle
from .models import ContactMessage

admin.site.register(ContactMessage)
admin.site.register(NewsArticle)
