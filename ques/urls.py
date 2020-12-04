
from django.urls import path
from .views import home, ans
urlpatterns = [

    path('', home),
    path('ans/',ans,name='ans-url')
]