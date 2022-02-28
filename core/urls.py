from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path('', landing_page, name="landing-page"),
    path('file_view/', file_view, name="file_view"),
    path('file_add/', file_add, name="file_add"),
    path('file_detail/<int:pk>/', file_detail, name="file_detail"),
    path('file_delete/<int:pk>/', file_delete, name="file_delete"),
]
