import argparse
import json
from parser import ConfigParser


def main():
    parser = argparse.ArgumentParser(description="CLI для обработки учебного конфигурационного языка")
    parser.add_argument("file", type=str, help="Путь к входному файлу конфигурации")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            content = file.read()
            config_parser = ConfigParser()
            result = config_parser.parse(content)
            print("Результат обработки:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.file}' не найден.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
