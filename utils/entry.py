class EntryUtils:
    @staticmethod
    def check_status() -> tuple[bool, bool, bool, bool]:
        users = []

        # TODO: add check users

        return True, True, True, True

    @staticmethod
    def close_all() -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    def open_all() -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    def set_admin_entry(is_open: bool) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    def set_employee_entry(is_open: bool) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    def set_student_entry(is_open: bool) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    def set_guest_entry(is_open: bool) -> bool:
        try:
            return True
        except Exception:
            return False
