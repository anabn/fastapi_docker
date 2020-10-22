# patient-service/app/api

import os
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

patient = Table(
    'patient',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('surname', String(50)),
    Column('age', Integer),
    Column('drugs_id', ARRAY(Integer)),
)

database = Database(DATABASE_URI)
