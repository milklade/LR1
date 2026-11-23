
from .validators import (
    validate_integer,
    validate_name,
    validate_phone
)


class Teacher:
    """Класс преподавателя учебного заведения."""

    @staticmethod
    def validate_teacher_id(value):
        validate_integer(value, "ID преподавателя", 1)

    @staticmethod
    def validate_surname(value):
        validate_name(value, "Фамилия")

    @staticmethod
    def validate_first_name(value):
        validate_name(value, "Имя")

    @staticmethod
    def validate_patronymic(value):
        validate_name(value, "Отчество")

    @staticmethod
    def validate_phone(value):
        validate_phone(value)

    @staticmethod
    def validate_work_experience(value):
        validate_integer(value, "Стаж работы", 0)

    def __init__(
        self,
        teacher_id: int,
        surname: str,
        first_name: str,
        patronymic: str,
        phone: str,
        work_experience: int
    ):
        self.validate_teacher_id(teacher_id)
        self.validate_surname(surname)
        self.validate_first_name(first_name)
        self.validate_patronymic(patronymic)
        self.validate_phone(phone)
        self.validate_work_experience(work_experience)

        self.__teacher_id = teacher_id
        self.__surname = surname.strip()
        self.__first_name = first_name.strip()
        self.__patronymic = patronymic.strip()
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
