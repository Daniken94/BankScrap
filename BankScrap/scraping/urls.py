from django.contrib import admin
from django.urls import path
from .views import Index

app_name = 'scraping'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index")
]