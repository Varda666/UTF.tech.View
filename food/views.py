from rest_framework.generics import (ListAPIView)
from models import FoodCategory
from serializers import FoodListSerializer


class FoodCategoryListView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer

