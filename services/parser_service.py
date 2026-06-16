from datetime import date

from utils.date_helper import DateHelper
from utils.text_helper import TextHelper
from utils.type_helper import TypeHelper


class ParserService:

    @staticmethod
    def parse_update(text):

        lines = [
            x.strip()
            for x in text.splitlines()
            if x.strip()
        ]

        # Remove command if exists
        if (
            lines
            and lines[0].startswith("/")
        ):
            lines.pop(0)

        if len(lines) == 5:

            trx_date = date.today()

            trx_type = lines[0]
            amount = lines[1]
            category = lines[2]
            wallet = lines[3]
            description = lines[4]

        elif len(lines) == 6:

            trx_date = DateHelper.parse_date(
                lines[0]
            )

            trx_type = lines[1]
            amount = lines[2]
            category = lines[3]
            wallet = lines[4]
            description = lines[5]

        else:
            raise ValueError(
                """
Invalid format.

Example:

expense
25000
makan
bca
nasi goreng
                """
            )

        return {

            "date":
                trx_date,

            "type":
                TypeHelper.normalize(
                    trx_type
                ),

            "amount":
                TextHelper.clean_amount(
                    amount
                ),

            "category":
                category.lower().strip(),

            "wallet":
                wallet.lower().strip(),

            "description":
                description.strip()
        }