from datetime import datetime

def generate_transaction_id(
    sheet
):

    today = (
        datetime.now()
        .strftime(
            "%Y%m%d"
        )
    )

    rows = (
        sheet
        .get_all_records()
    )

    count = 0

    for row in rows:

        trx_id = (
            row[
                "TransactionID"
            ]
        )

        if (
            trx_id
            .startswith(
                f"TRX{today}"
            )
        ):
            count += 1

    sequence = (
        str(
            count + 1
        )
        .zfill(4)
    )

    return (
        f"TRX{today}"
        f"{sequence}"
    )