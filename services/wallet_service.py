import difflib


class WalletService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    def get_all_wallets(self):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Wallets"
            )
        )

        return (
            sheet
            .get_all_records()
        )

    def get_total_balance(
        self
    ):

        total = sum(

            float(
                wallet[
                    "CurrentBalance"
                ]
            )

            for wallet
            in self.get_all_wallets()
        )

        return total

    def get_wallets_by_owner(
        self,
        owner
    ):

        owner = (
            owner
            .lower()
            .strip()
        )

        wallets = []

        for wallet in (
            self.get_all_wallets()
        ):

            if (
                wallet[
                    "Owner"
                ]
                .lower()
                == owner
            ):

                wallets.append(
                    wallet
                )

        return wallets

    def get_wallet(
        self,
        wallet_name
    ):

        wallet_name = (
            wallet_name
            .lower()
            .strip()
        )

        wallets = (
            self
            .get_all_wallets()
        )

        for wallet in wallets:

            if (
                wallet[
                    "WalletName"
                ]
                .lower()
                == wallet_name
            ):
                return wallet

            if (
                wallet[
                    "WalletCode"
                ]
                .lower()
                == wallet_name
            ):
                return wallet

        return None

    def suggest_wallet(
        self,
        wallet_name,
        limit=3
    ):

        wallet_name = (
            wallet_name
            .lower()
            .strip()
        )

        wallets = (
            self
            .get_all_wallets()
        )

        names = []

        for wallet in wallets:

            names.append(
                wallet[
                    "WalletName"
                ].lower()
            )

            names.append(
                wallet[
                    "WalletCode"
                ].lower()
            )

        suggestions = (
            difflib
            .get_close_matches(
                wallet_name,
                names,
                n=limit,
                cutoff=0.3
            )
        )

        return list(
            dict.fromkeys(
                suggestions
            )
        )