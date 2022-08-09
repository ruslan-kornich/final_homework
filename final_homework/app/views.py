from app.utils import google_sheets
from django.http import HttpResponse

from app.models.Order import Order


# Create your views here.
def upload_data(request):
    data = google_sheets.main()
    for row in data:
        print(row)
        try:
            created = Order.objects.get_or_create(
                id=row[0],
                order_number=row[1],
                cost_usd=row[2],
                delivery_time=row[3],
            )
        except:
            pass
    return HttpResponse('Done!')
