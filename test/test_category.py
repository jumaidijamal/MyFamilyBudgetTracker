from config import *
from services.sheet_service import (
    SheetService
)
from services.category_service import (
    CategoryService
)

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

category_service = (
    CategoryService(
        sheet_service
    )
)

print(
    category_service.get_category(
        "makan"
    )
)

print(
    category_service
    .suggest_category(
        "mkn"
    )
)