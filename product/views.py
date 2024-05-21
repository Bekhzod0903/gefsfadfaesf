from django.views.generic import ListView, DetailView
from .models import Foods

# Use Django's built-in ListView for listing foods
class FoodListView(ListView):
    model = Foods
    template_name = 'food/food_list.html'
    context_object_name = 'foods'  # changed from 'food' to 'foods' for clarity
    ordering = ['-pk']

# Use Django's built-in DetailView for food detail
class FoodDetailView(DetailView):
    model = Foods
    template_name = 'food/food_detail.html'
