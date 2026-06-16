from datetime import datetime


class DateHelper:

    FORMATS = [
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%d.%m.%Y"
    ]

    @classmethod
    def parse_date(cls, text):

        text = text.strip()

        for fmt in cls.FORMATS:
            try:
                return datetime.strptime(
                    text,
                    fmt
                ).date()
            except ValueError:
                pass

        raise ValueError(
            f"Invalid date format: {text}"
        )