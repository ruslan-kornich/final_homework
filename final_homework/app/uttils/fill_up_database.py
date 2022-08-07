from final_homework.app.models.Order import Order


def fill_up_database_values():
    for order in [12121, 1212, 1555, 115]:
        Order.objects.get_or_create(
            order=order,
            description=f"Order number {order}",
        )
