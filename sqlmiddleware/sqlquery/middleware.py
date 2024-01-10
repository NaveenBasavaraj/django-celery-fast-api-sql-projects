from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqlLexer
from django.conf import settings
from decimal import Decimal


def new_middleware(get_response):
    """
    Middleware is a way of processing requests and responses globally before they reach the view or after they leave the view.
    This middleware is used to print out the SQL queries that are executed during the processing of a request when Django is running in debug mode.
    It also prints the number of unique queries that were executed.
    """

    def middleware(request):
        """
        This function is the actual middleware that processes the request and response.
        """
        print("before")
        response = get_response(request)
        print("after")
        if settings.DEBUG:
            print("debug mode")
            duplicates = set()
            num_queries = len(connection.queries)
            total_execution_time = Decimal()
            for query in connection.queries:
                if query["sql"] in duplicates:
                    continue
                duplicates.add(query["sql"])
                total_execution_time += Decimal(query["time"])
                sqlformatted = format(str(query["sql"]))
                print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
            print("=====================================")
            print("[SQL stats]")
            print(f"Number of Queries: {num_queries  - len(duplicates)} ")
            print("=====================================")
        return response

    return middleware
