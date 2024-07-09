# apify_app/urls.py
from django.urls import path
from .views import ApifyDataView

urlpatterns = [
    path('apify-data/', ApifyDataView.as_view(), name='apify-data'),
]