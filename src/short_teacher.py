
from .teacher import Teacher
from .teacher_base import TeacherBase


class ShortTeacher(TeacherBase):
    """Класс краткого представления преподавателя."""

    def __init__(self, teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError(
                "Необходимо передать объект класса Teacher."
            )

        super().__init__(
            teacher.teacher_id,
            teacher.surname,
            teacher.first_name
        )

    def __str__(self):
        """Возвращает краткую информацию о преподавателе."""
        return (
            f"Преподаватель: {self.surname} "
            f"{self.first_name}, ID: {self.teacher_id}"
        )
