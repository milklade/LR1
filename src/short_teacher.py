
from .teacher import Teacher


class ShortTeacher:
    """Класс краткого представления преподавателя."""

    def __init__(self, teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError(
                "Необходимо передать объект класса Teacher."
            )

        self.__teacher_id = teacher.teacher_id
        self.__surname = teacher.surname
        self.__first_name = teacher.first_name

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def surname(self):
        return self.__surname

    @property
    def first_name(self):
        return self.__first_name

    def __str__(self):
        return (
            f"Преподаватель: {self.__surname} "
            f"{self.__first_name}, ID: {self.__teacher_id}"
        )

    def __repr__(self):
        return (
            f"ShortTeacher(id={self.__teacher_id}, "
            f"name='{self.__surname} {self.__first_name}')"
        )
