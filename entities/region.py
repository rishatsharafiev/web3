class RegionEntity:
    """Region entity"""

    __slots__ = (
        'id',
        'name',
    )

    def __init__(self, _id: int, _name: str):
        """
        Конструктор
        Args:
            _id: ID региона
            _name: Название региона
        """
        self.id = _id
        self.name = _name
