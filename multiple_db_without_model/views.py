from django.shortcuts import render, HttpResponse
from django.db import connections
import pandas as pd
# Create your views here.

cursor1= connections['primary'].cursor()
cursor2 = connections['secondary'].cursor()

def testdb_cursor1(request):
    if request.method == 'GET':
        query = """ select * from mytable limit 10 """
        with cursor1 as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            columns = cursor.description
            cursor.close()
            column = []
            for col in columns:
                column.append(col.name)
            df = pd.DataFrame(result,columns=column)
            result_df = HttpResponse(df.to_html())
            return result_df


def userdb_cursor2(request):
    if request.method == 'GET':
        query = """ select * from mytable limit 10 """
        with cursor2 as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            columns = cursor.description
            cursor.close()
            column = []
            for col in columns:
                column.append(col.name)
            df = pd.DataFrame(result,columns=column)
            result_df = HttpResponse(df.to_html())
            return result_df