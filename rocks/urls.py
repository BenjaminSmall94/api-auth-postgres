from django.urls import path
from .views import RockList, RockDetail, RockUpdateDelete, RockCreate

urlpatterns = [
    path("", RockList.as_view(), name="rock_list"),
    path("<int:pk>", RockDetail.as_view(), name="rock_detail"),
    path("create/", RockCreate.as_view(), name="rock_create"),
    path("update/<int:pk>", RockUpdateDelete.as_view(), name="rock_update"),
    path("delete/<int:pk>", RockUpdateDelete.as_view(), name="rock_delete"),
]