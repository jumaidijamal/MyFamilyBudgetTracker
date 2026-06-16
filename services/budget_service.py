from datetime import datetime


class BudgetService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    # ==========================
    # GET SHEET
    # ==========================

    def get_sheet(self):

        return (
            self.sheet_service
            .get_sheet(
                "Budgets"
            )
        )

    # ==========================
    # GET ALL
    # ==========================

    def get_all_budgets(self):

        return (
            self
            .get_sheet()
            .get_all_records()
        )

    # ==========================
    # GET BUDGET
    # ==========================

    def get_budget(
        self,
        user_id,
        category_id,
        period="Monthly"
    ):

        budgets = (
            self
            .get_all_budgets()
        )

        for budget in budgets:

            if (
                budget["UserID"]
                == user_id
                and
                budget["CategoryID"]
                == category_id
                and
                budget["Period"]
                == period
            ):

                return budget

        return None

    # ==========================
    # GENERATE ID
    # ==========================

    def generate_budget_id(self):

        budgets = (
            self
            .get_all_budgets()
        )

        number = (
            len(
                budgets
            )
            + 1
        )

        return (
            f"BGT{number:03d}"
        )

    # ==========================
    # CREATE BUDGET
    # ==========================

    def create_budget(
        self,
        user,
        category,
        amount,
        period="Monthly"
    ):

        sheet = (
            self.get_sheet()
        )

        budget_id = (
            self
            .generate_budget_id()
        )

        now = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        row = [

            budget_id,

            user[
                "UserID"
            ],

            user[
                "DisplayName"
            ],

            period,

            category[
                "CategoryID"
            ],

            category[
                "CategoryName"
            ],

            float(
                amount
            ),

            0,

            float(
                amount
            ),

            now,

            now
        ]

        sheet.append_row(
            row
        )

        return {

            "BudgetID":
                budget_id,

            "Amount":
                float(amount)
        }

    # ==========================
    # UPDATE BUDGET
    # ==========================

    def update_budget(
        self,
        budget_id,
        amount
    ):

        sheet = (
            self.get_sheet()
        )

        rows = (
            sheet
            .get_all_records()
        )

        for index, row in enumerate(
            rows,
            start=2
        ):

            if (
                row["BudgetID"]
                == budget_id
            ):

                used = float(
                    row["Used"]
                )

                remaining = (
                    float(amount)
                    - used
                )

                now = (
                    datetime.now()
                    .strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )

                sheet.update_cell(
                    index,
                    7,
                    float(amount)
                )

                sheet.update_cell(
                    index,
                    9,
                    remaining
                )

                sheet.update_cell(
                    index,
                    11,
                    now
                )

                return {

                    "BudgetID":
                        budget_id,

                    "Amount":
                        float(amount),

                    "Remaining":
                        remaining
                }

        return None