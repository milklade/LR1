class Teacher:
    """Класс преподавателя учебного заведения."""

    def __init__(
        self,
        teacher_id: int,
        surname: str,
        first_name: str,
        patronymic: str,
        phone: str,
        work_experience: int
    ):
        self.__teacher_id = teacher_id
        self.__surname = surname
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__phone = phone
        self.__work_experience = work_experience

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def surname(self):
        return self.__surname

    @property
    def first_name(self):
        return self.__first_name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def phone(self):
        return self.__phone

    @property
    def work_experience(self):
        return self.__work_experience
