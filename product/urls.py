from django.urls import path
from .views import FoodListView, FoodDetailView

app_name = 'product'
urlpatterns = [
    path('test/', FoodListView.as_view(), name='food-list'),
    path('detail/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
]
