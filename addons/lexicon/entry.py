class EntryLexicon:
    OPEN: str = "✅ *Открыт*"
    CLOSE: str = "❌ *Закрыт*"

    INFO: str = (
        "*На данный момент:*\n\n"
        "👨‍💻 Администраторы: {status_admin}\n"
        "💼 Сотрудники: {status_employee}\n"
        "🎓 Студенты: {status_student}\n"
        "🧑‍💼 Гости: {status_guest}"
    )

    ALL_SUCCESS = "✅ Турникет для *всех пользователей* успешно {action}."
    ALL_ERROR = "❌ Ошибка: не удалось {action} турникет для *всех пользователей*."

    ADMIN_SUCCESS = "✅ Турникет для *администраторов* успешно {action}."
    ADMIN_ERROR = "❌ Ошибка: не удалось {action} турникет для *администраторов*."

    EMPLOYEE_SUCCESS = "✅ Турникет для *сотрудников* успешно {action}."
    EMPLOYEE_ERROR = "❌ Ошибка: не удалось {action} турникет для *сотрудников*."

    STUDENT_SUCCESS = "✅ Турникет для *студентов* успешно {action}."
    STUDENT_ERROR = "❌ Ошибка: не удалось {action} турникет для *студентов*."

    GUEST_SUCCESS = "✅ Турникет для *гостей* успешно {action}."
    GUEST_ERROR = "❌ Ошибка: не удалось {action} турникет для *гостей*."

    ERROR = "❌ *Повторите запрос снова*"
