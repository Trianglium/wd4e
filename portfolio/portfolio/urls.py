from django.urls import path, include
from portfolio.views import AboutView, IndexView
app_name = 'portfolio'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]
