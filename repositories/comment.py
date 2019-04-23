from utils.db import get_connection
from utils.shortcuts import get_item

from entities import CommentEntity


class CommentRepository:
    """Comment Repository"""

    @staticmethod
    def get_all():
        sql_string = """SELECT comment.id, comment.first_name, comment.second_name, comment.last_name, 
                        comment.phone, comment.email, comment.text AS region_name FROM comment;
                    """

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string)
            return [
                CommentEntity(
                    _first_name=get_item(row, index=1),
                    _last_name=get_item(row, index=3),
                    _text=get_item(row, index=6),
                    _id=get_item(row, index=0), 
                    _second_name=get_item(row, index=2),
                    _phone=get_item(row, index=4),
                    _email=get_item(row, index=5),
                ) for row in cursor.fetchall()
            ]

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

    @staticmethod
    def remove(pk: int):
        sql_string = "DELETE FROM comment WHERE id=?"
        prepared_statements = (pk,)

        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_string, prepared_statements)
            connection.commit()
            return cursor.lastrowid
