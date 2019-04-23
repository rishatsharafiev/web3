from utils.db import get_connection
from utils.shortcuts import get_item

from entities import RegionEntity, RegionStatEntity


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

    @staticmethod
    def get_stat():
        sql_string = """SELECT region.id, region.name, COUNT(distinct comment.id) AS comment_count FROM region
                        INNER JOIN city ON city.region_id = region.id
                        INNER JOIN comment ON comment.city_id = city.id
                        GROUP BY region.id
                        HAVING COUNT(distinct comment.id) > 5;
                     """

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string)
            return [
                RegionStatEntity(
                    _id=get_item(row, index=0), 
                    _name=get_item(row, index=1),
                    _comment_count=get_item(row, index=2),
                ) for row in cursor.fetchall()
            ]
