from django.urls import path
from shopApp.views import index, about, form_comment, add_contact

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('form_comment/', form_comment, name = 'form_comment'),
    path('add_contact/', add_contact, name = 'add_contact'),
]