class BalanceService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    def get_balance(
        self,
        wallet_id
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Wallets"
            )
        )

        rows = (
            sheet
            .get_all_records()
        )

        for row in rows:

            if (
                row["WalletID"]
                == wallet_id
            ):
                return float(
                    row[
                        "CurrentBalance"
                    ]
                )

        return 0

    def update_balance(
        self,
        wallet_id,
        amount,
        trx_type
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Wallets"
            )
        )

        records = (
            sheet
            .get_all_records()
        )

        for index, row in enumerate(
            records,
            start=2
        ):

            if (
                row["WalletID"]
                == wallet_id
            ):

                current = float(
                    row[
                        "CurrentBalance"
                    ]
                )

                if trx_type in (
                    "expense",
                    "saving"
                ):
                    current -= amount

                elif trx_type == "income":
                    current += amount

                else:
                    raise ValueError(
                        f"Unknown transaction type: {trx_type}"
                    )

                current = round(
                    current,
                    2
                )

                sheet.update_cell(
                    index,
                    7,
                    current
                )

                return current

        raise ValueError(
            f"Wallet ID not found: {wallet_id}"
        )