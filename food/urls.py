from django.urls import path
from django.contrib import admin

from food.views import FoodCategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', FoodCategoryListView.as_view(), name='category_food_list'),
]


