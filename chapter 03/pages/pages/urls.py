from django.urls import path
from .views import HomPageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomPageView.as_view(), name='home'),    
]