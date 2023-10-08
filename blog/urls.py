from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blogindex')
]
