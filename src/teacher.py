
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

    
    @classmethod
    def from_string(cls, data):
        """Создаёт преподавателя из строки."""
        parts = data.split(";")

        if len(parts) != 6:
            raise ValueError(
                "Строка должна содержать 6 значений, разделённых ';'."
            )

        return cls(
            teacher_id=int(parts[0]),
            surname=parts[1],
            first_name=parts[2],
            patronymic=parts[3],
            phone=parts[4],
            work_experience=int(parts[5])
        )

    @classmethod
    def from_dict(cls, data):
        """Создаёт преподавателя из словаря."""
        required_fields = {
            "teacher_id",
            "surname",
            "first_name",
            "patronymic",
            "phone",
            "work_experience"
        }

        if not isinstance(data, dict):
            raise ValueError("Данные должны быть словарём.")

        if set(data.keys()) != required_fields:
            raise ValueError("Неверный набор полей преподавателя.")

        return cls(**data)

    @classmethod
    def from_json(cls, json_data):
        """Создаёт преподавателя из JSON-строки."""
        import json

        try:
            data = json.loads(json_data)
        except (TypeError, json.JSONDecodeError):
            raise ValueError("Некорректный JSON.")

        return cls.from_dict(data)

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




    def __str__(self):
        """Возвращает полную информацию о преподавателе."""
        return (
            f"Преподаватель: {self.__surname} "
            f"{self.__first_name} {self.__patronymic}\n"
            f"ID: {self.__teacher_id}\n"
            f"Телефон: {self.__phone}\n"
            f"Стаж работы: {self.__work_experience} лет"
        )

    def __repr__(self):
        """Возвращает краткое представление преподавателя."""
        return (
            f"Teacher(id={self.__teacher_id}, "
            f"name='{self.__surname} {self.__first_name}')"
        )

    def __eq__(self, other):
        """Сравнивает двух преподавателей по всем полям."""
        if not isinstance(other, Teacher):
            return NotImplemented

        return (
            self.__teacher_id == other.__teacher_id
            and self.__surname == other.__surname
            and self.__first_name == other.__first_name
            and self.__patronymic == other.__patronymic
            and self.__phone == other.__phone
            and self.__work_experience == other.__work_experience
        )
