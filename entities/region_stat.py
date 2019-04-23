class RegionStatEntity:
    """Region Stat entity"""

    __slots__ = (
        'id',
        'name',
        'comment_count',
    )

    def __init__(self, _id: int, _name: str, _comment_count: int = None):
        """
        Конструктор
        Args:
            _id: ID региона
            _name: Название региона
            _comment_count: Кол-во комментариев
        """
        self.id = _id
        self.name = _name
        self.comment_count = _comment_count
