from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqlLexer
from sqlparse import format
from django.conf import settings
from decimal import Decimal

def new_middleware(get_response):
    def middleware(request):
        #print("before")
        response = get_response(request)
        if settings.DEBUG:
            query_list = list(connection.queries)
            total_execution_time = Decimal()
            print("=========================")
            print("[SQL stats]")
            print(f"{query_list} total queries")
            print("=========================")
            for q in query_list:
                total_execution_time += Decimal(q["time"])
                sqlformatted = format(str(q["sql"]), reindent=True)
                print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
            print(f"total time {total_execution_time}")
            print("=========================")
        #print("after")
        return response
    return middleware