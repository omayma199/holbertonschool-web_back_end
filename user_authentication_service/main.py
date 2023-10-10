#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
