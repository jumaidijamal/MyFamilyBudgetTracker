class ValidationService:

    def __init__(
        self,
        wallet_service,
        category_service
    ):

        self.wallet_service = (
            wallet_service
        )

        self.category_service = (
            category_service
        )

    def validate(
        self,
        trx
    ):

        wallet = (
            self.wallet_service
            .get_wallet(
                trx["wallet"]
            )
        )

        if wallet is None:

            suggestions = (
                self.wallet_service
                .suggest_wallet(
                    trx["wallet"]
                )
            )

            message = (
                f"❌ Wallet "
                f"'{trx['wallet']}' "
                f"tidak ditemukan."
            )

            if suggestions:

                message += (
                    "\n\nApakah "
                    "maksud Anda:\n"
                )

                for s in suggestions:
                    message += (
                        f"• {s}\n"
                    )

            raise ValueError(
                message
            )

        category = (
            self.category_service
            .get_category(
                trx["category"]
            )
        )

        if category is None:

            suggestions = (
                self.category_service
                .suggest_category(
                    trx["category"]
                )
            )

            message = (
                f"❌ Category "
                f"'{trx['category']}' "
                f"tidak ditemukan."
            )

            if suggestions:

                message += (
                    "\n\nApakah "
                    "maksud Anda:\n"
                )

                for s in suggestions:
                    message += (
                        f"• {s}\n"
                    )

            raise ValueError(
                message
            )

        if (
            trx["type"]
            == "expense"
        ):

            balance = float(
                wallet[
                    "CurrentBalance"
                ]
            )

            if (
                trx["amount"]
                > balance
            ):

                raise ValueError(
                    f"""
❌ Saldo
{wallet['WalletName']}
tidak mencukupi.

Saldo:
Rp {balance:,.0f}

Pengeluaran:
Rp {trx['amount']:,.0f}
"""
                )

        return {
            "wallet": wallet,
            "category": category
        }