import re


class TextHelper:

    @staticmethod
    def clean_amount(text: str) -> float:

        text = text.lower().strip()

        text = text.replace("rp", "")
        text = text.replace("idr", "")
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace(" ", "")

        text = re.sub(
            r"[^\d]",
            "",
            text
        )

        if not text:
            raise ValueError(
                "Amount is invalid."
            )

        return float(text)