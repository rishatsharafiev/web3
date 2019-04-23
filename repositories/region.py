from utils.db import get_connection
from utils.shortcuts import get_item

from entities import RegionEntity


class RegionRepository:
    """Region Repository"""

    @staticmethod
    def get_all():
        sql_string = "SELECT id, name FROM region"

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string)
            return [
                RegionEntity(
                    _id=get_item(row, index=0), 
                    _name=get_item(row, index=1)
                ) for row in cursor.fetchall()
            ]

