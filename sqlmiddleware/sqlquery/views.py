from django.shortcuts import render
from sqlquery.models import Product
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json

# Create your views here.


def home(request):
    """
    View function for the home page.

    Retrieves all products from the database, serializes them into JSON format,
    and returns the serialized data as a JSON response.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response containing the serialized product data.
    """
    qs = Product.objects.all()
    serialized_Data = serialize("json", qs)
    serialized_Data = json.loads(serialized_Data)
    return JsonResponse(serialized_Data, status=200, safe=False)
