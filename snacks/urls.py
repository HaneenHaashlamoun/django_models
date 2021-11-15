from django.urls import path
from .views import SnackListView,SnackListDetail

urlpatterns = [
    path('', SnackListView.as_view(), name="snack_list"),
    path('<int:pk>/', SnackListDetail.as_view(), name="snack_detail"),
]