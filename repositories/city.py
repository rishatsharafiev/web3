from utils.db import get_connection
from utils.shortcuts import get_item

from entities import CityStatEntity, CityEntity


class CityRepository:
    """City Repository"""

    @staticmethod
    def get_by_region_id(region_id: int):
        sql_string = "SELECT id, name, region_id FROM city WHERE region_id=?"
        prepared_statements = (region_id,)

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string, prepared_statements)
            return [
                CityEntity(
                    _id=get_item(row, index=0), 
                    _name=get_item(row, index=1),
                    _region_id=get_item(row, index=2),
                ) for row in cursor.fetchall()
            ]

    @staticmethod
    def get_stat(region_id: int):
        sql_string = """SELECT city.id, city.name, COUNT(distinct comment.id) AS comment_count FROM city
                        INNER JOIN comment ON comment.city_id = city.id
                        WHERE city.region_id=?
                        GROUP BY city.id;
                    """

        prepared_statements = (region_id,)

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string, prepared_statements)
            return [
                CityStatEntity(
                    _id=get_item(row, index=0), 
                    _name=get_item(row, index=1),
                    _comment_count=get_item(row, index=2),
                ) for row in cursor.fetchall()
            ]
