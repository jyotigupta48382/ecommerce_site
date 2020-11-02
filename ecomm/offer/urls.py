from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="offer"),
    path("offerpost/<int:id>", views.Offerpost, name="offerPost"),


]
