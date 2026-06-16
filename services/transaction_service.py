from datetime import datetime
from utils.id_generator import (
    generate_transaction_id
)

class TransactionService:

    def __init__(
        self,
        sheet_service,
        balance_service
    ):

        self.sheet_service = (
            sheet_service
        )

        self.balance_service = (
            balance_service
        )

    # ==========================
    # SAVE TRANSACTION
    # ==========================  
    def save_transaction(
        self,
        trx,
        user,
        wallet,
        category
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
        )

        trx_id = (
            generate_transaction_id(
                sheet
            )
        )

        now = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        sheet.append_row(
            [
                trx_id,
                trx["date"].strftime(
                    "%Y-%m-%d"
                ),
                user["UserID"],
                user["DisplayName"],
                trx["type"],
                category[
                    "CategoryID"
                ],
                category[
                    "CategoryName"
                ],
                wallet[
                    "WalletID"
                ],
                wallet[
                    "WalletName"
                ],
                trx["amount"],
                trx["description"],
                "Posted",
                now,
                now
            ]
        )

        new_balance = (
            self.balance_service
            .update_balance(
                wallet[
                    "WalletID"
                ],
                trx["amount"],
                trx["type"]
            )
        )

        return {
            "TransactionID":
                trx_id,

            "NewBalance":
                new_balance
        }

    # ==========================
    # DELETE TRANSACTION
    # ==========================
    def delete_transaction(
        self,
        transaction_id
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
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
                row[
                    "TransactionID"
                ]
                != transaction_id
            ):
                continue

            if (
                row[
                    "Status"
                ]
                .lower()
                != "posted"
            ):

                raise ValueError(
                    "Transaction already deleted."
                )

            wallet_id = (
                row[
                    "WalletID"
                ]
            )

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

            rollback_type = (
                "income"
                if trx_type
                == "expense"
                else "expense"
            )

            new_balance = (
                self.balance_service
                .update_balance(
                    wallet_id,
                    amount,
                    rollback_type
                )
            )

            sheet.update_cell(
                index,
                12,
                "Deleted"
            )

            sheet.update_cell(
                index,
                14,
                datetime.now()
                .isoformat()
            )

            return {

                "TransactionID":
                    transaction_id,

                "NewBalance":
                    new_balance
            }

        raise ValueError(
            "Transaction not found."
        )
    
    # ==========================
    # UNDO TRANSACTION
    # ==========================
    def undo_transaction(
        self,
        transaction_id
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
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
                row[
                    "TransactionID"
                ]
                != transaction_id
            ):
                continue

            if (
                row[
                    "Status"
                ]
                .lower()
                != "deleted"
            ):

                raise ValueError(
                    "Transaction is not deleted."
                )

            wallet_id = (
                row[
                    "WalletID"
                ]
            )

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

            new_balance = (
                self.balance_service
                .update_balance(
                    wallet_id,
                    amount,
                    trx_type
                )
            )

            sheet.update_cell(
                index,
                12,
                "Posted"
            )

            sheet.update_cell(
                index,
                14,
                datetime.now()
                .isoformat()
            )

            return {

                "TransactionID":
                    transaction_id,

                "NewBalance":
                    new_balance
            }

        raise ValueError(
            "Transaction not found."
        )
    
    # ==========================
    # EDIT TRANSACTION
    # ==========================
    def get_transaction(
        self,
        transaction_id
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
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
                row[
                    "TransactionID"
                ]
                == transaction_id
            ):

                return {
                    "RowIndex":
                        index,

                    "Data":
                        row
                }

        return None
    
    # ==========================
    # ROLLBACK TRANSACTION
    # ==========================
    def rollback_transaction(
        self,
        old_transaction
    ):

        wallet_id = (
            old_transaction[
                "WalletID"
            ]
        )

        amount = float(
            old_transaction[
                "Amount"
            ]
        )

        trx_type = (
            old_transaction[
                "Type"
            ]
            .lower()
        )

        rollback_type = (
            "income"
            if trx_type
            == "expense"
            else "expense"
        )

        return (
            self.balance_service
            .update_balance(
                wallet_id,
                amount,
                rollback_type
            )
        )
    
    # ==========================
    # EDIT TRANSACTION
    # ==========================
    def edit_transaction(
        self,
        transaction_id,
        trx,
        wallet,
        category
    ):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Transactions"
            )
        )

        old = (
            self.get_transaction(
                transaction_id
            )
        )

        if old is None:

            raise ValueError(
                "Transaction not found."
            )

        row_index = (
            old[
                "RowIndex"
            ]
        )

        old_data = (
            old[
                "Data"
            ]
        )

        if (
            old_data[
                "Status"
            ]
            .lower()
            != "posted"
        ):

            raise ValueError(
                "Deleted transaction cannot be edited."
            )

        # =====================
        # Rollback old balance
        # =====================

        self.rollback_transaction(
            old_data
        )

        # =====================
        # Apply new balance
        # =====================

        new_balance = (
            self.balance_service
            .update_balance(
                wallet[
                    "WalletID"
                ],
                trx[
                    "amount"
                ],
                trx[
                    "type"
                ]
            )
        )

        # =====================
        # Update Transaction
        # =====================

        sheet.update_cell(
            row_index,
            2,
            str(
                trx[
                    "date"
                ]
            )
        )

        sheet.update_cell(
            row_index,
            5,
            trx[
                "type"
            ]
        )

        sheet.update_cell(
            row_index,
            6,
            category[
                "CategoryID"
            ]
        )

        sheet.update_cell(
            row_index,
            7,
            category[
                "CategoryName"
            ]
        )

        sheet.update_cell(
            row_index,
            8,
            wallet[
                "WalletID"
            ]
        )

        sheet.update_cell(
            row_index,
            9,
            wallet[
                "WalletName"
            ]
        )

        sheet.update_cell(
            row_index,
            10,
            trx[
                "amount"
            ]
        )

        sheet.update_cell(
            row_index,
            11,
            trx[
                "description"
            ]
        )

        sheet.update_cell(
            row_index,
            14,
            datetime.now()
            .isoformat()
        )

        return {

            "TransactionID":
                transaction_id,

            "WalletName":
                wallet[
                    "WalletName"
                ],

            "NewBalance":
                new_balance
        }