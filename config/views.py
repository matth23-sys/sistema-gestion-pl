from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone


@login_required
def dashboard(request):
    return render(
        request,
        "dashboard/index.html",
    )


def health_check(request):
    database_status = "ok"

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()
    except Exception:
        database_status = "error"

    status_code = (
        200
        if database_status == "ok"
        else 503
    )

    return JsonResponse(
        {
            "status": (
                "ok"
                if status_code == 200
                else "error"
            ),
            "service":
                "Pro Legacy Management System",
            "database":
                database_status,
            "timestamp":
                timezone.now().isoformat(),
        },
        status=status_code,
    )