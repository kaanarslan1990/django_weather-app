from django.urls import path
from .views import index, delete_city


urlpatterns = [
    path('', index, name='home'),
    path('delete/<id>', delete_city, name='delete')
]
