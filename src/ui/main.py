import sys
import os
import configparser

module_kit_path = os.path.join(os.path.dirname(__file__), '..', 'module-kit')
sys.path.insert(0, module_kit_path)

from KitBenchmark import KitBenchmark

CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    '..',
    '..',
    'conf',
    'settings.ini'
)

def load_settings():
    """
    Загружает настройки из conf/settings.ini.
    Если файл отсутствует, программа продолжит работу со значениями по умолчанию.
    """
    config = configparser.ConfigParser()

    try:
        with open(CONFIG_PATH, encoding='utf-8-sig') as f:
            config.read_file(f)
    except FileNotFoundError:
        pass

    return config

settings = load_settings()

def get_setting(section, option, fallback):
    """
    Безопасно получает строковый параметр из settings.ini.
    """
    try:
        value = settings.get(section, option)
        if value == '':
            return fallback
        return value
    except Exception:
        return fallback


def get_int_setting(section, option, fallback):
    """
    Безопасно получает целочисленный параметр из settings.ini.
    """
    try:
        return int(settings.get(section, option))
    except Exception:
        return fallback


def get_bool_setting(section, option, fallback):
    """
    Безопасно получает булев параметр из settings.ini.
    Поддерживает true/false, yes/no, on/off, 1/0.
    """
    try:
        return settings.getboolean(section, option)
    except Exception:
        return fallback

def main():
    # Читаем параметры из settings.ini
    title = get_setting('app', 'title', 'Поиск чисел Кита')
    version = get_setting('app', 'version', '')
    show_version = get_bool_setting('ui', 'show_version', False)

    header = get_setting('ui', 'header', f'========{title}===========')
    message = get_setting('ui', 'message', 'Введите диапазон чисел (минимально от 10):')
    start_label = get_setting('ui', 'start_label', 'Начало')
    end_label = get_setting('ui', 'end_label', 'Конец')
    use_defaults_if_empty = get_bool_setting('ui', 'use_defaults_if_empty', True)

    default_start = get_int_setting('range', 'default_start', 10)
    default_end = get_int_setting('range', 'default_end', 1000)

    # Если нужно, добавляем версию к заголовку
    if show_version and version:
        header = f'{header} v{version}'

    print(header)
    print()
    print(message)

    benchmark = KitBenchmark()

    try:
        start_text = input(f'{start_label}: ')
        end_text = input(f'{end_label}: ')

        # Если пользователь ввёл пустую строку и use_defaults_if_empty=true,
        # используем значения из settings.ini.
        start = int(start_text) if start_text.strip() or not use_defaults_if_empty else default_start
        end = int(end_text) if end_text.strip() or not use_defaults_if_empty else default_end

        print()
        benchmark.Run(start, end)
        print(benchmark.GetResults())
        print()

    except ValueError as e:
        print(f'Ошибка! {e}')

def wait_before_close():
    try:
        input("\nНажмите Enter, чтобы закрыть окно...")
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    try:
        main()
    finally:
        wait_before_close()