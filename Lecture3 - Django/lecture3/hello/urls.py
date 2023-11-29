from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('go/dung', views.dung, name='Dung'),
    path('<str:name>', views.greet, name='greet')
]
