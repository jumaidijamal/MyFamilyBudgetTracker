class UserService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )
    
    def get_all_users(self):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Users"
            )
        )

        return (
            sheet
            .get_all_records()
        )

    def get_user_by_telegram_id(
        self,
        telegram_id
    ):

        telegram_id = (
            str(telegram_id)
        )

        users = (
            self.get_all_users()
        )

        for user in users:

            if (
                str(
                    user[
                        "TelegramID"
                    ]
                )
                == telegram_id
            ):
                return user

        return None