from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)

def print_ultra(text, color=Fore.WHITE, bgcolor=Back.BLACK, style=Style.NORMAL, border=False):
    """
    Функция для печати текста с различными стилями и форматированием.

    Параметры:
    text (str): Текст для печати.
    color (str): Цвет текста. Использует цветовые константы из colorama.Fore.
    bgcolor (str): Цвет фона. Использует цветовые константы из colorama.Back.
    style (str): Стиль текста. Использует стилевые константы из colorama.Style.
    border (bool): Если True, добавляет рамку вокруг текста.
    """
    # Создание рамки, если она необходима
    if border:
        border_top_bottom = '+' + '-' * (len(text) + 2) + '+'
        border_middle = f"| {text} |"
        print(color + bgcolor + style + border_top_bottom)
        print(color + bgcolor + style + border_middle)
        print(color + bgcolor + style + border_top_bottom)
    else:
        print(color + bgcolor + style + text)

# Примеры использования
print_ultra("Hello, World!", color=Fore.RED, bgcolor=Back.YELLOW, style=Style.BRIGHT, border=True)
print_ultra("Python is awesome!", color=Fore.GREEN, style=Style.DIM)
print_ultra("Print Ultra", color=Fore.CYAN, bgcolor=Back.MAGENTA, border=True)
