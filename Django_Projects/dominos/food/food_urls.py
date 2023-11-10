from django.urls import path
from food.views import *

app_name = 'food'
urlpatterns = [
    path('', hello, name="hello"),
    path('item/', item_view, name="item_view"),
    path('item/<int:item_id>', detail_view, name="detail_view"),
    # create item form
    path('item/create', create_view, name="create_view"),
    # edit item form
    path('item/update/<int:item_id>', update_view, name="update_view"),
    # delete item form
    path('item/delete/<int:item_id>', delete_view, name="delete_view"),
]
