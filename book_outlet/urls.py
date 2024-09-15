from . import views
from django.urls import path

urlpatterns = [
    path("",views.index),
    path("<slug:slug>",views.book_detail, name="detail-page")
]
