from datetime import datetime


class AdminService:

    def __init__(
        self,
        sheet_service,
        started_at
    ):
        self.sheet_service = (
            sheet_service
        )

        self.started_at = (
            started_at
        )

    def get_dashboard(self):

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

        uptime = (
            datetime.now()
            - self.started_at
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

            "uptime":
                str(
                    uptime
                ).split(
                    "."
                )[0],

            "server_time":
                datetime.now(),

            "version":
                "v1.0.0"
        }