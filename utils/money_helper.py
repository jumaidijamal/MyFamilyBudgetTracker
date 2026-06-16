class MoneyHelper:

    @staticmethod
    def format_rupiah(
        amount
    ):
        return (
            "Rp{:,.0f}"
            .format(amount)
            .replace(",", ".")
        )