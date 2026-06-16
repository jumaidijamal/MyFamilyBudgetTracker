from datetime import datetime

class HealthService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    def get_health(self):

        users = (
            self.sheet_service
            .get_sheet(
                "Users"
            )
            .get_all_records()
        )

        wallets = (
            self.sheet_service
            .get_sheet(
                "Wallets"
            )
            .get_all_records()
        )

        categories = (
            self.sheet_service
            .get_sheet(
                "Categories"
            )
            .get_all_records()
        )

        transactions = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
            .get_all_records()
        )

        return {

            "status":
                "Online",

            "users":
                len(users),

            "wallets":
                len(wallets),

            "categories":
                len(categories),

            "transactions":
                len(transactions),

            "server_time":
                datetime.now()
        }