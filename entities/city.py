class CityEntity:
    """City entity"""

    __slots__ = (
        'id',
        'name',
        'region_id',
    )

    def __init__(self, _id: int, _name: str, _region_id: int):
        """
        Конструктор
        Args:
            _id: ID города
            _name: Название города
            _region_id: ID региона
        """
        self.id = _id
        self.name = _name
        self.region_id = _region_id

    def entity_to_dict(self):
        """
        Entity to dict
        """
        return {
            'id': self.id,
            'name': self.name,
            'region_id': self.region_id,
        }
