import difflib


class CategoryService:

    def __init__(
        self,
        sheet_service
    ):
        self.sheet_service = (
            sheet_service
        )

    def get_all_categories(self):

        sheet = (
            self.sheet_service
            .get_sheet(
                "Categories"
            )
        )

        return sheet.get_all_records()

    def get_category(
        self,
        category_name
    ):

        category_name = (
            category_name
            .lower()
            .strip()
        )

        categories = (
            self.get_all_categories()
        )

        for category in categories:

            if (
                category[
                    "CategoryName"
                ]
                .lower()
                == category_name
            ):
                return category

        return None

    def suggest_category(
        self,
        category_name,
        limit=3
    ):

        category_name = (
            category_name
            .lower()
            .strip()
        )

        categories = (
            self.get_all_categories()
        )

        names = [

            category[
                "CategoryName"
            ].lower()

            for category
            in categories
        ]

        suggestions = (
            difflib.get_close_matches(
                category_name,
                names,
                n=limit,
                cutoff=0.3
            )
        )

        return suggestions
    
    def get_category_by_type(
        self,
        category_name,
        trx_type
    ):

        category_name = (
            category_name
            .lower()
            .strip()
        )

        trx_type = (
            trx_type
            .lower()
            .strip()
        )

        categories = (
            self.get_all_categories()
        )

        for category in categories:

            if (
                category[
                    "CategoryName"
                ]
                .lower()
                == category_name
                and
                category[
                    "CategoryType"
                ]
                .lower()
                == trx_type
            ):
                return category

        return None