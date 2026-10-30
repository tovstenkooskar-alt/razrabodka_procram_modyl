"""Заказы смены: чтение CSV, выручка официантов и сортировка по сумме."""

from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Читает заказы смены из CSV и собирает объекты Order.

    Args:
        path: Путь к файлу смены со столбцами waiter и kopeks.

    Returns:
        Список заказов. Имена официантов приведены к одному виду.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку каждого официанта.

    Args:
        orders: Заказы смены.
        top: Сколько официантов оставить. Ноль означает всех.

    Returns:
        Словарь «имя — сумма в копейках», от большей выручки к меньшей.

    Raises:
        ValueError: Если список заказов пуст.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует заказы по сумме, от большей к меньшей.

    Args:
        orders: Список, который меняется на месте.

    Returns:
        Ничего: тот же список оказывается упорядоченным.
    """
    orders.sort(key=lambda order: -order.kopeks)
