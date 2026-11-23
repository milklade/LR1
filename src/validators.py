
def validate_integer(value, field_name, minimum):
    """Проверяет целое число и его минимальное значение."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{field_name} должно быть целым числом.")

    if value < minimum:
        raise ValueError(
            f"{field_name} должно быть не меньше {minimum}."
        )


def validate_name(value, field_name):
    """Проверяет, что строковое поле не пустое."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Поле '{field_name}' не может быть пустым.")


def validate_phone(value):
    """Проверяет формат телефона."""
    if not isinstance(value, str):
        raise ValueError("Телефон должен быть строкой.")

    digits = "".join(char for char in value if char.isdigit())

    if not 10 <= len(digits) <= 15:
        raise ValueError("Телефон должен содержать от 10 до 15 цифр.")

    allowed_chars = set("+0123456789 -()")

    if any(char not in allowed_chars for char in value):
        raise ValueError("Телефон содержит недопустимые символы.")
