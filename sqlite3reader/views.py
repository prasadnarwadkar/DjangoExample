import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import sqlite3
from django.contrib.auth.decorators import login_required
from sqlite3reader.models import TableNameColsAndRows

# Create your views here.
@login_required
def index(request):
    data = {}
    if "GET" == request.method:
        return render(request, "sqlite3reader/upload_sqlite3db.html", data)
	
    # if not GET, then proceed
    try:
        

        sqlite3FileName = request.FILES["sqlite3db_file"]

        # Connect to the SQLite database
        conn = sqlite3.connect(sqlite3FileName.name)

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a SQL query
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

        nested_list = []
        
        # Fetch all rows from the executed query
        tableNames = cursor.fetchall()
        tables =  [x[0] for x in tableNames]

        for tableName in tableNames:
            getColsQuery = f'SELECT name FROM PRAGMA_TABLE_INFO("{tableName[0]}");'
            cursor.execute(getColsQuery)
            cols = cursor.fetchall()
            cols = [x[0] for x in cols]

            cursor.execute(f'SELECT * FROM {tableName[0]};')
            rows = cursor.fetchall()
            #rows = [x[0] for x in rows]

            element1 = TableNameColsAndRows(tableName[0], cols, rows)
            nested_list.append(element1)
            print(tableName)

        cursor.close()
        # Close the connection
        conn.close()
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
    return render(request, "sqlite3reader/upload_sqlite3db.html", {"tables": tables, "nested_list": nested_list})