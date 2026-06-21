from fastapi import (
    APIRouter,
    Request
)

from fastapi.responses import (
    HTMLResponse
)

from fastapi.templating import (
    Jinja2Templates
)

from config import (
    SPREADSHEET_ID
)

from services.dashboard_service import (
    DashboardService
)

router = APIRouter()

templates = Jinja2Templates(
    directory="web/templates"
)

dashboard = DashboardService(
    SPREADSHEET_ID
)


@router.get(
    "/api/dashboard/summary"
)
def summary(

    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None
):

    return dashboard.get_summary(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type
    )


@router.get(
    "/api/dashboard/category"
)
def category(
    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None
):
    return dashboard.expense_by_category(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type
    )


@router.get(
    "/api/dashboard/user"
)
def user_chart(
    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None
):

    return dashboard.expense_by_user(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type
    )


@router.get(
    "/api/dashboard/wallet"
)
def wallet_chart(
    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None
):
    return dashboard.expense_by_wallet(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type
    )


@router.get(
    "/dashboard",
    response_class=HTMLResponse
)
async def dashboard_page(
    request: Request
):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )

@router.get(
    "/api/dashboard/trend"
)
def trend(
    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None,
    mode="daily"
):

    return dashboard.monthly_trend(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type,
        mode=mode
    )

@router.get(
    "/api/dashboard/kpi"
)
def kpi(
    start_date=None,
    end_date=None,
    category=None,
    wallet=None,
    user=None,
    trx_type=None
):
    dashboard.transaction_count(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type
    )
    return {
        
        "transaction_count":
            dashboard.transaction_count(
                start_date,
                end_date,
                category,
                wallet,
                user,
                trx_type
            ),

        "top_category":
            dashboard.top_category(
                start_date,
                end_date,
                category,
                wallet,
                user,
                trx_type
            ),

        "top_user":
            dashboard.top_user(
                start_date,
                end_date,
                category,
                wallet,
                user,
                trx_type
            ),

        "average_expense":
            dashboard.average_expense(
                start_date,
                end_date,
                category,
                wallet,
                user,
                trx_type
            )
    }

@router.get(
    "/api/dashboard/options"
)
def options():

    return dashboard.get_options()

@router.get(
    "/api/dashboard/budget-progress"
)
def budget_progress(
    user=None
):
    return dashboard.budget_progress(
        user=user
    )

@router.get(
    "/api/dashboard/wallet-balance"
)
def wallet_balance(
    user=None
):
    return dashboard.wallet_balance(
        user=user
    )

@router.get(
    "/api/dashboard/transactions"
)
def transactions(
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
    return dashboard.transaction_history(
        start_date=start_date,
        end_date=end_date,
        category=category,
        wallet=wallet,
        user=user,
        trx_type=trx_type,
        page=int(page),
        page_size=int(page_size),
        search=search
    )