from django.forms import ModelForm
from food.models import Item

class create_item(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"