class EntryLexicon:
    OPEN: str = "✅ Открыт"
    CLOSE: str = "❌ Закрыт"

    INFO: str = (
        "На данный момент:\n"
        "Вход для администраторов: {status_admin}\n"
        "Вход для сотрудников: {status_employee}\n"
        "Вход для студентов: {status_student}\n"
        "Вход для гостей: {status_guest}"
    )

    ALL_SUCCESS = "✅ Турникет для всех пользователей успешно {action}."
    ALL_ERROR = "❌ Ошибка: не удалось {action} турникет для всех пользователей."

    ADMIN_SUCCESS = "✅ Турникет для администратора успешно {action}."
    ADMIN_ERROR = "❌ Ошибка: не удалось {action} турникет для администратора."

    EMPLOYEE_SUCCESS = "✅ Турникет для сотрудников успешно {action}."
    EMPLOYEE_ERROR = "❌ Ошибка: не удалось {action} турникет для сотрудников."

    STUDENT_SUCCESS = "✅ Турникет для студентов успешно {action}."
    STUDENT_ERROR = "❌ Ошибка: не удалось {action} турникет для студентов."

    GUEST_SUCCESS = "✅ Турникет для гостей успешно {action}."
    GUEST_ERROR = "❌ Ошибка: не удалось {action} турникет для гостей."
