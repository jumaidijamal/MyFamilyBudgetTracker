from datetime import date
from datetime import datetime
from datetime import (
    date,
    timedelta
)


class ReportService:

    # ==========================
    # INITIALIZATION
    # ==========================
    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    # ==========================
    # ALL TRANSACTIONS
    # ==========================
    def get_all_transactions(
        self
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
        )

        return (
            sheet
            .get_all_records()
        )

    # ==========================
    # TODAY TRANSACTION
    # ==========================
    def get_today_transactions(
        self
    ):

        rows = (
            self
            .get_all_transactions()
        )

        today = (
            date.today()
            .isoformat()
        )

        result = []

        for row in rows:

            trx_date = str(
                row[
                    "TransactionDate"
                ]
            )

            status = (
                row[
                    "Status"
                ]
            )

            if (
                trx_date
                == today
                and
                status
                == "Posted"
            ):

                result.append(
                    row
                )

        return result

    # ==========================
    # TODAY SUMMARY
    # ==========================
    def get_today_summary(
        self
    ):

        rows = (
            self
            .get_today_transactions()
        )

        income = 0
        expense = 0
        saving = 0

        categories = {}

        for row in rows:

            amount = float(
                row[
                    "Amount"
                ]
            )

            trx_type = (
                row[
                    "Type"
                ]
                .lower()
            )

            category = (
                row[
                    "CategoryName"
                ]
            )

            if trx_type == "income":
                income += amount

            elif trx_type == "expense":
                expense += amount

            elif trx_type == "saving":
                saving += amount


                categories[
                    category
                ] = (
                    categories.get(
                        category,
                        0
                    )
                    + amount
                )

        return {

            "income":
                income,

            "saving":
                saving,

            "expense":
                expense,

            "net":
                income
                - expense
                - saving,

            "categories":
                categories
        }

    # ==========================
    # WEEK SUMMARY
    # ==========================
    def get_week_summary(
        self
    ):

        rows = (
            self
            .get_all_transactions()
        )

        today = (
            date.today()
        )

        start_date = (
            today
            - timedelta(
                days=today.weekday()
            )
        )

        expense = 0
        income = 0
        categories = {}

        for row in rows:

            status = (
                str(
                    row[
                        "Status"
                    ]
                )
                .lower()
            )

            if (
                status
                != "posted"
            ):
                continue

            trx_date = (
                date.fromisoformat(
                    str(
                        row[
                            "TransactionDate"
                        ]
                    )
                )
            )

            if not (
                start_date
                <= trx_date
                <= today
            ):
                continue

            trx_type = (
                row[
                    "Type"
                ]
                .lower()
            )

            amount = float(
                row[
                    "Amount"
                ]
            )

            category = (
                row[
                    "CategoryName"
                ]
            )

            if (
                trx_type
                == "expense"
            ):

                expense += amount

                categories[
                    category
                ] = (
                    categories.get(
                        category,
                        0
                    )
                    + amount
                )

            elif (
                trx_type
                == "income"
            ):

                income += amount

        return {

            "expense":
                expense,

            "income":
                income,

            "net":
                income - expense,

            "categories":
                categories,

            "start_date":
                start_date,

            "end_date":
                today
        }

    # ==========================
    # MONTH SUMMARY
    # ==========================
    def get_month_summary(
        self
    ):

        rows = (
            self
            .get_all_transactions()
        )

        today = (
            date.today()
        )

        current_month = (
            today.month
        )

        current_year = (
            today.year
        )

        expense = 0
        income = 0
        categories = {}

        for row in rows:

            status = (
                str(
                    row[
                        "Status"
                    ]
                )
                .lower()
            )

            if (
                status
                != "posted"
            ):
                continue

            trx_date = (
                date.fromisoformat(
                    str(
                        row[
                            "TransactionDate"
                        ]
                    )
                )
            )

            if (
                trx_date.month
                != current_month
            ):
                continue

            if (
                trx_date.year
                != current_year
            ):
                continue

            trx_type = (
                row[
                    "Type"
                ]
                .lower()
            )

            amount = float(
                row[
                    "Amount"
                ]
            )

            category = (
                row[
                    "CategoryName"
                ]
            )

            if (
                trx_type
                == "expense"
            ):

                expense += amount

                categories[
                    category
                ] = (
                    categories.get(
                        category,
                        0
                    )
                    + amount
                )

            elif (
                trx_type
                == "income"
            ):

                income += amount

        return {

            "expense":
                expense,

            "income":
                income,

            "net":
                income - expense,

            "categories":
                categories,

            "month":
                current_month,

            "year":
                current_year
        }

    # ==========================
    # HISTORY
    # ==========================    
    def get_recent_transactions(
        self,
        limit=10
    ):

        rows = (
            self
            .get_all_transactions()
        )

        transactions = []

        for row in rows:

            status = (
                str(
                    row[
                        "Status"
                    ]
                )
                .lower()
            )

            if (
                status
                != "posted"
            ):
                continue

            transactions.append(
                row
            )

        transactions.sort(
            key=lambda row:
            (
                row[
                    "TransactionDate"
                ],
                row[
                    "CreatedDate"
                ]
            ),
            reverse=True
        )

        return (
            transactions[
                :limit
            ]
        )

    # ==========================
    # SUMMARY
    # ==========================   
    def get_asset_summary(
        self
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Wallets"
            )
        )

        wallets = (
            sheet
            .get_all_records()
        )

        result = {}

        total_assets = 0

        for wallet in wallets:

            owner = (
                wallet[
                    "Owner"
                ]
            )

            if owner not in result:

                result[
                    owner
                ] = []

            balance = float(
                wallet.get(
                    "CurrentBalance",
                    0
                )
            )

            result[
                owner
            ].append({

                "WalletID":
                    wallet[
                        "WalletID"
                    ],

                "WalletName":
                    wallet[
                        "WalletName"
                    ],

                "Balance":
                    balance,

                "OwnerType":
                    wallet[
                        "OwnerType"
                    ]
            })

            total_assets += balance

        return {

            "Owners":
                result,

            "TotalAssets":
                total_assets
        }