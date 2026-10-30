# Отчёт · Проверка типов: Pylance и mypy

**Студент:** Товстенко Оскар, группа 9/2-РПО-25/1

## 1. Подготовка

![Расширения Python и Pylance](img/py-01-extensions.png)

![.vscode/settings.json с режимом basic, интерпретатор .venv внизу окна](img/py-02-settings.png)

## 2. Проверка в редакторе

```python
from app.utils.formatter import format_kopeks, format_title

title = format_title(40)
price = format_kopeks("1250")
```

![Подчёркнутые аргументы в proba.py](img/py-03-squiggle.png)

![Сообщение Pylance над первым неверным аргументом](img/py-04-hover.png)

Разбор сообщения:

| Часть сообщения | Что означает |
|---|---|
| `Argument of type "Literal[40]"` | Передано конкретное число 40, это частный случай int |
| `cannot be assigned to parameter "text" of type "str"` | Параметр text ждёт строку, число туда не подходит |
| `Pylance(reportArgumentType)` | Сообщение дал Pylance по правилу о неверном типе аргумента |

![Панель Problems](img/py-05-problems.png)

## 3. Проверка в терминале

```text
proba.py:3: error: Argument 1 to "format_title" has incompatible type "int"; expected "str"  [arg-type]
proba.py:4: error: Argument 1 to "format_kopeks" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

![Терминал: mypy proba.py](img/py-06-mypy-errors.png)

```text
Success: no issues found in 1 source file
```

## 4. Проект без аннотаций

| Этап | Итог `mypy app` |
|---|---|
| исходно | Found 17 errors in 10 files (checked 15 source files) |
| после `utils` | Found 12 errors in 7 files (checked 15 source files) |
| после `domain` | Found 8 errors in 5 files (checked 15 source files) |
| после `services` | Found 1 error in 1 file (checked 15 source files) |
| после `ui` | Success: no issues found in 15 source files |

Модуль до и после — `app/utils/text.py`:

```python
def _squash_spaces(value):
    return " ".join(value.split())


def normalize_name(name):
    return _squash_spaces(name).title()
```

```python
def _squash_spaces(value: str) -> str:
    return " ".join(value.split())


def normalize_name(name: str) -> str:
    return _squash_spaces(name).title()
```

```text
Success: no issues found in 15 source files
............                                                             [100%]
12 passed in 0.08s
=========== Смена 30.10.2026 ===========
Петрова Анна                  2 480,50 ₽
Иванов Пётр                   1 685,00 ₽
Сидоров Илья                    772,00 ₽
=========== Итого 4 937,50 ₽ ===========
```

![Итоговая проверка: Success, тесты, отчёт 4 937,50 ₽](img/py-07-final.png)

## 5. Выводы

Pylance подчёркивает неверный аргумент сразу в редакторе, mypy печатает ту же ошибку в терминале: какой тип пришёл и какой записан в аннотации. Неожиданным было, что функция без параметров кроме self получает отдельную формулировку «нет аннотации результата», а не «нет аннотации вообще». Проверка не видит данные из файла: если в CSV вместо числа окажется слово, `int(...)` упадёт уже при запуске, и ни Pylance, ни mypy об этом не предупредят.
