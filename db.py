import sqlite3
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    DATABASE_URL = "postgresql://postgres:P7EojxrDZ1dzVd6@db.hhlzeuppjxwtpyheroie.supabase.co:5432/postgres"
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

#  os.environ.get('DATABASE_URL')