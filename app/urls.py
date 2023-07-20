from django.urls import path
from app import views

urlpatterns = [
    path('boisson',views.boisson_list,name="boisson"),
    path('boisson/<id>',views.boisson_detail)
]
