
from abc import ABC, abstractmethod


class TeacherBase(ABC):
    """Базовый класс с общими данными преподавателя."""

    def __init__(self, teacher_id, surname, first_name):
        self.__teacher_id = teacher_id
        self.__surname = surname
        self.__first_name = first_name

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def surname(self):
        return self.__surname

    @property
    def first_name(self):
        return self.__first_name

    def __repr__(self):
        return (
            f"{type(self).__name__}(id={self.teacher_id}, "
            f"name='{self.surname} {self.first_name}')"
        )

    @abstractmethod
    def __str__(self):
        """Возвращает текстовое представление преподавателя."""
        pass
