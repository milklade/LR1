
class Teacher:
    """Класс преподавателя учебного заведения."""

    @staticmethod
    def validate_teacher_id(value):
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            raise ValueError("ID преподавателя должен быть положительным целым числом.")

    @staticmethod
    def validate_name(value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Поле '{field_name}' не может быть пустым.")

    @staticmethod
    def validate_phone(value):
        if not isinstance(value, str):
            raise ValueError("Телефон должен быть строкой.")

        digits = "".join(char for char in value if char.isdigit())

        if len(digits) < 10 or len(digits) > 15:
            raise ValueError("Телефон должен содержать от 10 до 15 цифр.")

        allowed_chars = set("+0123456789 -()")
        if any(char not in allowed_chars for char in value):
            raise ValueError("Телефон содержит недопустимые символы.")

    @staticmethod
    def validate_work_experience(value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Стаж должен быть неотрицательным целым числом.")

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
        self.validate_name(surname, "Фамилия")
        self.validate_name(first_name, "Имя")
        self.validate_name(patronymic, "Отчество")
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
