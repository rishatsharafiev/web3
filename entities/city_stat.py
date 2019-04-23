class CityStatEntity:
    """City Stat entity"""

    __slots__ = (
        'id',
        'name',
        'comment_count',
    )

    def __init__(self, _id: int, _name: str, _comment_count: int):
        """
        Конструктор
        Args:
            _id: ID города
            _name: Название города
            _comment_count: Кол-во комментариев
        """
        self.id = _id
        self.name = _name
        self.comment_count = _comment_count
