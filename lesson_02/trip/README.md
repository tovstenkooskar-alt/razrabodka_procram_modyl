Программа считает расходы за поездку и печатает отчёт: сколько записей, сколько потрачено всего и какая средняя трата.

## Как запустить

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py trip.py
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 trip.py
```

## Что печатает

```text
ОТЧЁТ ПО ПОЕЗДКЕ
--------------------------------
записей: 10
всего потрачено: 7900 ₽
средняя трата: 790.00 ₽
```

Заголовок «ОТЧЁТ ПО ПОЕЗДКЕ» выделен жирным зелёным через библиотеку Rich.
