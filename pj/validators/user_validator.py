class UserValidator:
    @classmethod
    def is_valid(cls, user):
        return bool(user.get_user_id() and user.get_device_id())
