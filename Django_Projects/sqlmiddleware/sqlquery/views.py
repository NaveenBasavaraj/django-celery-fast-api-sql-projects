from django.shortcuts import render
from sqlquery.models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
# from django.db import connection
# from pygments import highlight
# from pygments.formatters import TerminalFormatter
# from pygments.lexers.sql import SqlLexer
# from sqlparse import format

# Create your views here.

def home(request):
    products = Product.objects.all()
    serialized_data = serialize("json", products)
    # query_list = list(connection.queries)
    # moved below to middleware
    # for q in query_list:
    #     sqlformatted = format(str(q["sql"]), reindent=True)
    #     print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        #print(q)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False, status=200)
