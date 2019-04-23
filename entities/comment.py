class CommentEntity:
    """Comment entity"""

    __slots__ = (
        'first_name',
        'second_name',
        'last_name',
        'phone',
        'email',
        'text',
        'city_id',
    )

    def __init__(self, _first_name: str, _last_name: str, _text: str, _city_id: int = None, 
                _second_name: str = None, _phone: str = None, _email: str = None):
        """
        Конструктор
        Args:
            _first_name: Имя
            _second_name: Отчество
            _last_name: Фамилия
            _phone: Телефон
            _email: Email
            _text: Текст
            _city_id: id города
        """
        self.first_name = _first_name
        self.second_name = _second_name
        self.last_name = _last_name
        self.phone = _phone
        self.email = _email
        self.text = _text
        self.city_id = _city_id
