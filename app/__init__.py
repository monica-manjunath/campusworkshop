"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7j23hp8u7g2ed79eg-a.oregon-postgres.render.com",
        database="todo_ij3r",
        user="root",
        password="kz6xIHS2NWU3jD0MdYJ2xKT3GuJV3Ob7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
