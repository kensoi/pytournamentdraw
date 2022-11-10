"""
Выполнил Прокофьев Андрей Фт-210008
"""
import random
from logger import logger, LogLevel

def get_random(range_value: int)->list:
    """
    Получить список от 1 до N в случайном порядке
    """

    logger.log(LogLevel.INFO.value,
        "Генерация случайного списка...")

    output = [*range(1, range_value+1)]
    output.sort(key=lambda _: random.random()) # перемешиваем

    logger.log(LogLevel.DEBUG.value,
        "Генерация завершена")

    return output


def get_int(text_to_print: str="")->int:
    """
    Получить целое число из терминала
    """

    while True:
        try:
            response = int(input(text_to_print + " >> "))
            logger.log(LogLevel.DEBUG.value,
                "Удачная попытка получить число")
            return response

        except ValueError as exception:
            logger.log(LogLevel.DEBUG.value,
                "Неудачная попытка получить число (ошибка: %s)", str(exception))


def main():
    """
    Главная функция
    """

    logger.log(LogLevel.INFO.value,
        "Начало программы")

    draw_value = get_int("Введите N") # число N

    for key, value in enumerate(get_random(draw_value)):
        print(f"№{key}:\t{value}\t", end="")

        logger.log(LogLevel.INFO.value,
            "Получено число %s", value)

        if key != draw_value - 1:
            input("[Нажмите enter]")

    logger.log(LogLevel.INFO.value,
        "Завершение программы")


if __name__ == "__main__":
    main()
