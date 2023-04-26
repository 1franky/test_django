from django.urls import path
from face import views

urlpatterns = [
    path('getFaces', views.image_to_numpy),
    path('getFaces2', views.image_to_numpy2),
]
