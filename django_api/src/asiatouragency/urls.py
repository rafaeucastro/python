from django.urls import path
from . import views

# Here you associate your view\endpoints with the url
urlpatterns = [
    path("tours/", views.index, name="tours"),
]