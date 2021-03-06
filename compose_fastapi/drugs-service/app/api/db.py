# drugs-service/app/api
import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

drugs = Table(
    'drugs',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('designation', String(50)),
)

database = Database(DATABASE_URI)