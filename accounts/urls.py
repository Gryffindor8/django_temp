from django.urls import path
from .views import signin,home, signout

app_name = "auth"

urlpatterns = [
    path('', signin, name="login"),
    path('home', home, name="home"),
    path('signout', signout, name="signout"),

]
