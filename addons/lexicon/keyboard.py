class KeyboardLexicon:
    OPEN_CLOSE: str = "↔️ Открыть/Закрыть турникет"
    OPEN_CLOSE_CALL: str = "open_close"

    # USERS: str = "ℹ️ Просмотреть пользователей"

    ADD: str = "🆕 Добавить пользователя"
    ADD_CAL: str = "add_new_user"

    FIND: str = "🔄 Найти пользователя"
    FIND_CALL: str = "find_user"

    OPEN: str = "✅ Открыть"
    OPEN_CALL: str = "open_"

    CLOSE: str = "❌ Закрыть"
    CLOSE_CALL: str = "close_"

    BACK: str = "🔙 Вернуться назад"
    BACK_CALL: str = "back"
    SPEC_BACK_CALL: str = "spec_back_"

    OPEN_ADMINS: str = "✅ Открыть для администраторов"
    CLOSE_ADMINS: str = "❌ Закрыть для администраторов"
    OPEN_CLOSE_ADMIN_CALL: str = "open_close_admins"

    OPEN_EMPLOYEES: str = "✅ Открыть сотрудников"
    CLOSE_EMPLOYEES: str = "❌ Закрыть для сотрудников"
    OPEN_CLOSE_EMPLOYEES_CALL: str = "open_close_employees"

    OPEN_STUDENTS: str = "✅ Открыть для студентов"
    CLOSE_STUDENTS: str = "❌ Закрыть для студентов"
    OPEN_CLOSE_STUDENTS_CALL: str = "open_close_students"

    OPEN_GUESTS: str = "✅ Открыть для гостей"
    CLOSE_GUESTS: str = "❌ Закрыть для гостей"
    OPEN_CLOSE_GUESTS_CALL: str = "open_close_guests"

    OPEN_ALL: str = "✅ Открыть всем"
    OPEN_ALL_CALL: str = "open_all"

    CLOSE_ALL: str = "❌ Закрыть всем"
    CLOSE_ALL_CALL: str = "close_all"

    EDIT_NAME: str = "🔁 Изменить ФИО"
    EDIT_NAME_CALL: str = "edit_name_"

    EDIT_PHOTO: str = "🔁 Изменить фото"
    EDIT_PHOTO_CALL: str = "edit_photo_"

    EDIT_TYPE: str = "🔁 Изменить тип"
    EDIT_TYPE_CALL: str = "edit_type_"

    EDIT_DATE: str = "🔁 Изменить срок действия"
    EDIT_DATE_CALL: str = "edit_date_"

    DELETE: str = "❌ Удалить пользователя"
    DELETE_CALL: str = "delete_"

    ADMIN: str = "👨‍💻 Администратор"
    EMPLOYEE: str = "💼 Сотрудник"
    STUDENT: str = "🎓 Студент"
    GUEST: str = "🧑‍💼 Гость"

    TYPES: tuple = (
        ADMIN,
        EMPLOYEE,
        STUDENT,
        GUEST,
    )
