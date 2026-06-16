class TypeHelper:

    TYPE_MAP = {

        "e": "expense",
        "exp": "expense",
        "expense": "expense",
        "pengeluaran": "expense",
        "keluar": "expense",

        "i": "income",
        "inc": "income",
        "income": "income",
        "pemasukan": "income",
        "masuk": "income",
        "gaji": "income"
    }

    @classmethod
    def normalize(cls, text):

        text = text.lower().strip()

        if text not in cls.TYPE_MAP:
            raise ValueError(
                f"Unknown transaction type: {text}"
            )

        return cls.TYPE_MAP[text]