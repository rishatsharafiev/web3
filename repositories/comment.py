from utils.db import get_connection

from entities import CommentEntity


class CommentRepository:
    """Comment Repository"""

    @staticmethod
    def create(comment_entity: CommentEntity):
        sql_string = "INSERT INTO comment(first_name, second_name, last_name, phone, email, text, city_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        prepared_statements = (
            comment_entity.first_name, 
            comment_entity.second_name, 
            comment_entity.last_name, 
            comment_entity.phone, 
            comment_entity.email, 
            comment_entity.text, 
            comment_entity.city_id
        )

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string, prepared_statements)
            connection.commit()
            return cursor.lastrowid
