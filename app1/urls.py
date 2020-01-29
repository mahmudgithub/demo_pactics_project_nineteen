from django.urls import path
from .views import lol

urlpatterns = [
	path('',lol.as_view(),name='hello'),
]