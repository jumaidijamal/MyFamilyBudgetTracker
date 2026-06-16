from services.parser_service import (
    ParserService
)

cases = [

    """
expense
25000
makan
bca
nasi goreng
    """,

    """
e
Rp25.000
makan
bca
nasi goreng
    """,

    """
14-06-2026
expense
25000
makan
bca
nasi goreng
    """
]

for i, case in enumerate(
        cases,
        start=1
):
    try:

        result = (
            ParserService
            .parse_update(case)
        )

        print(
            f"TEST {i} ✅"
        )

        print(result)

    except Exception as e:

        print(
            f"TEST {i} ❌"
        )

        print(e)