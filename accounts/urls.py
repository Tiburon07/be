from django.urls import path
from accounts.views import registrazione_view

urlpatterns = [
    path("registrazione/", registrazione_view, name='registrazion_view')
]
