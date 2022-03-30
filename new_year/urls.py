from django.urls import path

from . import views

# route,views,name

urlpatterns = [
    path("", views.index,name="index")
]