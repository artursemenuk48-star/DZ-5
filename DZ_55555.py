import colorama
from colorama import Fore, Back, Style, init

print("=== ІНТРОСПЕКЦІЯ БІБЛІОТЕКИ COLORAMA ===")
print("Тип об'єкта colorama:", type(colorama))
print("Атрибути та методи модуля:", dir(colorama))
print("-" * 50)

init(autoreset=True)

print("=== ДЕМОНСТРАЦІЯ НАЙВАЖЛИВІШИХ АТРИБУТІВ ТА МЕТОДІВ ===")

print(Fore.RED + "Fore.RED — червоний")
print(Fore.GREEN + "Fore.GREEN — робить текст зеленим")
print(Fore.CYAN + "Fore.CYAN — робить текст блакитним")

print(Back.YELLOW + Fore.BLACK + "Back.YELLOW — додає жовтий фон під текстом")

print(Style.BRIGHT + Fore.MAGENTA + "Style.BRIGHT — робить колір тексту яскравим")
print(Style.DIM + "Style.DIM — робить колір тексту тусклим")

print(Fore.RED + "Червоний" + Style.RESET_ALL + " і звичайний текст")
