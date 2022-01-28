import sqlite3 as s

connection = s.connect("pt_app_obj.bd")  # connection a la bd
connection.row_factory = s.Row  # pour acceder aux valeurs avec le noms des champs 
cursor = connection.cursor()