from final_homework.app.utils import google_sheets
from final_homework.app.models.Order import Order

data = google_sheets.main()


for row in data:
    print(data)

