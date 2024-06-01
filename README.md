Print Ultra - это Python-библиотека для печати текста с различными стилями и форматированием. Библиотека использует `colorama` для цветного вывода текста и позволяет добавлять рамки вокруг текста.

## Установка

Перед использованием необходимо установить библиотеку `colorama`. Вы можете установить её с помощью pip:

```bash
pip install colorama
```

## Использование

### Импорт и инициализация

Для начала импортируйте и инициализируйте `colorama`:

```python
from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)
```

### Функция `print_ultra`

Функция `print_ultra` позволяет печатать текст с различными стилями и форматированием.

#### Сигнатура функции

```python
def print_ultra(text, color=Fore.WHITE, bgcolor=Back.BLACK, style=Style.NORMAL, border=False):
    """
    Параметры:
    text (str): Текст для печати.
    color (str): Цвет текста. Использует цветовые константы из colorama.Fore.
    bgcolor (str): Цвет фона. Использует цветовые константы из colorama.Back.
    style (str): Стиль текста. Использует стилевые константы из colorama.Style.
    border (bool): Если True, добавляет рамку вокруг текста.
    """
```

#### Параметры

- `text` (str): Текст для печати.
- `color` (str): Цвет текста. Использует цветовые константы из `colorama.Fore`. По умолчанию `Fore.WHITE`.
- `bgcolor` (str): Цвет фона. Использует цветовые константы из `colorama.Back`. По умолчанию `Back.BLACK`.
- `style` (str): Стиль текста. Использует стилевые константы из `colorama.Style`. По умолчанию `Style.NORMAL`.
- `border` (bool): Если `True`, добавляет рамку вокруг текста. По умолчанию `False`.

#### Примеры использования

```python
# Простой цветной текст с рамкой
print_ultra("Hello, World!", color=Fore.RED, bgcolor=Back.YELLOW, style=Style.BRIGHT, border=True)

# Текст с цветом и стилем без рамки
print_ultra("Python is awesome!", color=Fore.GREEN, style=Style.DIM)

# Цветной текст с фоном и рамкой
print_ultra("Print Ultra", color=Fore.CYAN, bgcolor=Back.MAGENTA, border=True)
```

## Лицензия

Этот проект лицензируется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).
