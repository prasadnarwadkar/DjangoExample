from django.db import models

# Create your models here.
class TableNameColsAndRows:
    def __init__(self, name, cols, rows:list):
        self.name = name
        self.cols = cols
        self.rows = rows

    @staticmethod
    def getcols(name, list):
        return [nested_elem for nested_elem in list if nested_elem.name == list][0].cols
