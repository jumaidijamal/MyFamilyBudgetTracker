import pandas as pd
import time

from config import EXPENSE_TYPE, INCOME_TYPE, SAVINGS_TYPE
from services.sheet_service import SheetService


class DashboardService:

    def __init__(
        self,
        spreadsheet_id
    ):
        self.sheet = SheetService(
            spreadsheet_id
        )

        self._df_cache = None
        self._last_refresh = 0
        self._cache_seconds = 30

    # ====================================
    # LOAD DATAFRAME
    # ====================================

    def get_transactions_df(self):
        
        now = time.time()

        if (
            self._df_cache is not None
            and
            (
                now
                - self._last_refresh
            )
            < self._cache_seconds
        ):
            return self._df_cache

        records = self.sheet.get_all_records(
            "Transactions"
        )

        df = pd.DataFrame(records)

        if df.empty:
            return df

        df["TransactionDate"] = pd.to_datetime(
            df["TransactionDate"]
        )

        df["Amount"] = (
            pd.to_numeric(
                df["Amount"],
                errors="coerce"
            )
            .fillna(0)
        )

        df["Type"] = (
            df["Type"]
            .astype(str)
            .str.lower()
            .str.strip()
        )

        self._df_cache = df
        self._last_refresh = now
        return df

    # ====================================
    # FILTER
    # ====================================

    def filter_df(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.get_transactions_df()

        if df.empty:
            return df

        if start_date:
            df = df[
                df["TransactionDate"]
                >= pd.to_datetime(start_date)
            ]

        if end_date:
            end_dt = (
                pd.to_datetime(end_date)
                + pd.Timedelta(days=1)
                - pd.Timedelta(seconds=1)
            )

            df = df[
                df["TransactionDate"]
                <= end_dt
            ]

        if trx_type:
            df = (
                df[
                    df["Type"]
                    == trx_type.lower()
                ]
            )

        if category:
            df = (
                df[
                    df["CategoryName"]
                    == category
                ]
            )

        if wallet:
            df = (
                df[
                    df["WalletName"]
                    == wallet
                ]
            )

        if user:
            df = (
                df[
                    df["UserName"]
                    == user
                ]
            )

        return df
    

    # ====================================
    # SUMMARY CARD
    # ====================================

    def get_summary(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            trx_type=trx_type,
            wallet=wallet,
            user=user
        )

        if df.empty:
            return {
                "income": 0,
                "expense": 0,
                "savings": 0,
                "balance": 0
            }

        income = (
            df[
                df["Type"] == INCOME_TYPE
            ]["Amount"]
            .sum()
        )

        expense = (
            df[
                df["Type"] == EXPENSE_TYPE
            ]["Amount"]
            .sum()
        )

        savings = (
            df[
                df["Type"] == SAVINGS_TYPE
            ]["Amount"]
            .sum()
        )

        # silakan ubah sesuai rule project
        balance = (
            income
            - expense
            - savings
        )

        return {
            "income": float(income),
            "expense": float(expense),
            "savings": float(savings),
            "balance": float(balance)
        }

    # ====================================
    # EXPENSE BY CATEGORY
    # ====================================

    def expense_by_category(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=EXPENSE_TYPE
        )

        if df.empty:
            return {
                "labels": [],
                "values": []
            }

        result = (
            df
            .groupby(
                "CategoryName",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
            .head(10)
        )

        return {
            "labels":
                result[
                    "CategoryName"
                ].tolist(),

            "values":
                result[
                    "Amount"
                ].tolist()
        }

    # ====================================
    # EXPENSE BY USER
    # ====================================

    def expense_by_user(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=EXPENSE_TYPE
        )

        if df.empty:
            return {
                "labels": [],
                "values": []
            }

        result = (
            df
            .dropna(
                subset=["UserName"]
            )
            .groupby(
                "UserName",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
        )

        return {
            "labels":
                result[
                    "UserName"
                ].tolist(),

            "values":
                result[
                    "Amount"
                ].tolist()
        }

    # ====================================
    # EXPENSE BY WALLET
    # ====================================

    def expense_by_wallet(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=EXPENSE_TYPE
        )

        if df.empty:
            return {
                "labels": [],
                "values": []
            }

        result = (
            df
            .groupby(
                "WalletName",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
        )

        return {
            "labels":
                result[
                    "WalletName"
                ].tolist(),

            "values":
                result[
                    "Amount"
                ].tolist()
        }
    
    # ====================================
    # TREND CHART
    # ====================================
    def monthly_trend(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None,
        mode="daily"
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user
        )

        if df.empty:
            return {
                "labels": [],
                "income": [],
                "expense": []
            }

        # ==========================
        # GROUP BY PERIOD
        # ==========================

        if mode == "monthly":

            df["Period"] = (
                df["TransactionDate"]
                .dt.strftime("%Y-%m")
            )

        else:

            df["Period"] = (
                df["TransactionDate"]
                .dt.strftime("%Y-%m-%d")
            )

        # ==========================
        # INCOME
        # ==========================

        income_df = (
            df[
                df["Type"] == INCOME_TYPE
            ]
            .groupby("Period", as_index=False)["Amount"]
            .sum()
            .rename(
                columns={
                    "Amount":
                    "Income"
                }
            )
        )

        # ==========================
        # EXPENSE
        # ==========================

        expense_df = (
            df[
                df["Type"]
                == EXPENSE_TYPE
            ]
            .groupby("Period", as_index=False)["Amount"]
            .sum()
            .rename(
                columns={
                    "Amount":
                    "Expense"
                }
            )
        )

        # periods = sorted(
        #     set(income_df.index)
        #     |
        #     set(expense_df.index)
        # )

        # return {
        #     "labels": periods,
        #     "income": [
        #         float(
        #             income_df.get(
        #                 p,
        #                 0
        #             )
        #         )
        #         for p in periods
        #     ],
        #     "expense": [
        #         float(
        #             expense_df.get(
        #                 p,
        #                 0
        #             )
        #         )
        #         for p in periods
        #     ]
        # }
    
        # ==========================
        # MERGE
        # ==========================
        
        result = pd.merge(
            income_df,
            expense_df,
            on="Period",
            how="outer"
        ).fillna(0)

        result = (
            result
            .sort_values("Period")
        )

        return {

            "labels":
                result[
                    "Period"
                ].tolist(),

            "income":
                result[
                    "Income"
                ].tolist(),

            "expense":
                result[
                    "Expense"
                ].tolist()
        }
    
    def transaction_count(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=trx_type
        )

        return len(df)
    
    def top_category(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        data = self.expense_by_category(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=trx_type
        )

        if not data["labels"]:
            return None

        return {

            "name": data["labels"][0],
            "amount": data["values"][0]
        }
    
    def top_user(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        data = self.expense_by_user(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=trx_type
        )

        if not data["labels"]:
            return None

        return {

            "name": data["labels"][0],
            "amount": data["values"][0]
        }
    
    def average_expense(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None
    ):

        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=EXPENSE_TYPE
        )

        if df.empty:
            return 0

        return float(
            df["Amount"].mean()
        )
    
    def get_options(self):

        df = self.get_transactions_df()

        if df.empty:
            return {
                "users": [],
                "wallets": [],
                "categories": [],
                "types": [],
                "years": []
            }

        return {
            "years":
                sorted(
                    df["TransactionDate"]
                    .dt.year
                    .dropna()
                    .unique()
                    .tolist()
                ),

            "users":
                sorted(
                    df["UserName"]
                    .dropna()
                    .unique()
                    .tolist()
                ),

            "wallets":
                sorted(
                    df["WalletName"]
                    .dropna()
                    .unique()
                    .tolist()
                ),

            "categories":
                sorted(
                    df["CategoryName"]
                    .dropna()
                    .unique()
                    .tolist()
                ),

            "types":
                sorted(
                    df["Type"]
                    .dropna()
                    .unique()
                    .tolist()
                )
        }
    
    def budget_progress(
        self,
        user=None
    ):
        budget_records = (
            self.sheet.get_all_records(
                "Budgets"
            )
        )

        budget_df = pd.DataFrame(
            budget_records
        )

        if budget_df.empty:
            return []
        
        budget_df["Amount"] = (
            pd.to_numeric(
                budget_df["Amount"],
                errors="coerce"
            )
            .fillna(0)
        )

        if user:

            budget_df = (
                budget_df[
                    budget_df["UserName"]
                    == user
                ]
            )

        trx_df = self.filter_df(
            user=user,
            trx_type=EXPENSE_TYPE
        )
        result = []

        for _, row in budget_df.iterrows():

            category = (
                row["CategoryName"]
            )

            budget = float(
                row["Amount"]
            )

            spent = (
                trx_df[
                    trx_df["CategoryName"]
                    == category
                ]["Amount"]
                .sum()
            )

            remaining = (
                budget
                - spent
            )

            percentage = 0

            if budget > 0:

                percentage = round(
                    spent
                    /
                    budget
                    *
                    100,
                    0
                )

            result.append(
                {
                    "user":
                        row["UserName"],

                    "category":
                        category,

                    "budget":
                        budget,

                    "spent":
                        float(spent),

                    "remaining":
                        float(remaining),

                    "percentage":
                        min(
                            percentage,
                            100
                        )
                }
            )

        return sorted(
            result,
            key=lambda x:
                x["percentage"],
            reverse=True
        )
    
    def wallet_balance(
        self,
        user=None
    ):
        records = (
            self.sheet.get_all_records(
                "Wallets"
            )
        )

        df = pd.DataFrame(
            records
        )

        if df.empty:
            return []

        df["CurrentBalance"] = (
            pd.to_numeric(
                df["CurrentBalance"],
                errors="coerce"
            )
            .fillna(0)
        )

        if user:

            df = (
                df[
                    df["Owner"]
                    == user
                ]
            )

        result = []

        for _, row in df.iterrows():

            result.append(
                {
                    "wallet_id":
                        row["WalletID"],

                    "wallet_code":
                        row["WalletCode"],

                    "wallet":
                        row["WalletName"],

                    "owner":
                        row["Owner"],

                    "owner_type":
                        row["OwnerType"],

                    "balance":
                        float(
                            row["CurrentBalance"]
                        )
                }
            )

        result = sorted(
            result,
            key=lambda x:
                x["balance"],
            reverse=True
        )

        return result
    
    def transaction_history(
        self,
        start_date=None,
        end_date=None,
        category=None,
        wallet=None,
        user=None,
        trx_type=None,
        page=1,
        page_size=10,
        search=None
    ):
        df = self.filter_df(
            start_date=start_date,
            end_date=end_date,
            category=category,
            wallet=wallet,
            user=user,
            trx_type=trx_type
        )

        if df.empty:
            return {
                "total": 0,
                "page": page,
                "page_size": page_size,
                "rows": []
            }

        if search:

            search = search.lower()

            df = df[
                df["Description"]
                .fillna("")
                .str
                .lower()
                .str
                .contains(search)
                |
                df["CategoryName"]
                .fillna("")
                .str
                .lower()
                .str
                .contains(search)
            ]

        df = df.sort_values(
            by="TransactionDate",
            ascending=False
        )

        total = len(df)

        start_idx = (
            page - 1
        ) * page_size

        end_idx = (
            start_idx
            + page_size
        )

        page_df = (
            df
            .iloc[start_idx:end_idx]
            .copy()
        )

        rows = []

        for _, row in page_df.iterrows():

            rows.append(
                {
                    "transaction_id":
                        row["TransactionID"],

                    "date":
                        row["TransactionDate"]
                        .strftime("%Y-%m-%d"),

                    "user":
                        row["UserName"],

                    "type":
                        row["Type"],

                    "category":
                        row["CategoryName"],

                    "wallet":
                        row["WalletName"],

                    "description":
                        row["Description"],

                    "amount":
                        float(row["Amount"])
                }
            )

        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "rows": rows
        }