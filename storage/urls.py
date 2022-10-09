from django.urls import path

from . import views

urlpatterns = [
    path("", views.storage_page, name="storage_page")
]
