from django.urls import path
from .views import ListApiView, DetailApiView

urlpatterns = [
    path('',ListApiView.as_view(), name = "ApiView"),
    path('<int:pk>/',DetailApiView.as_view(), name = "ApiDetail")
]
