class ConfigParser:
    def __init__(self):
        self.constants = {}  # Словарь для хранения констант
        self.result = {}

    def parse(self, config):
        # Шаг 1: Разбиение конфигурации на отдельные выражения
        statements = config.split(';')
        # Шаг 2: Обработка всех выражений
        for statement in statements:
            statement = statement.strip()
            if statement:
                self._process_statement(statement)

        # Шаг 3: Разрешение значений всех констант
        for name in self.constants:
            self.result[name] = self.constants[name]

        return self.result

    def _process_statement(self, statement):
        # Пример обработки 'x is 42;'
        parts = statement.split('is')
        if len(parts) == 2:
            name = parts[0].strip()
            value = self._parse_value(parts[1].strip())
            self.constants[name] = value
        else:
            raise ValueError(f"Неверное выражение: {statement}")

    def _parse_value(self, value):
        # Обработка значений (констант, массивов, строк и т.д.)
        if value.startswith("array"):
            return self._parse_array(value)
        elif value.startswith('"') and value.endswith('"'):
            return value.strip('"')
        elif value == "true":
            return True
        elif value == "false":
            return False
        elif value.isdigit():
            return int(value)
        elif value.startswith('@'):
            return value[2:-1]
        elif value.startswith("|"):
            # Разрешение уже определенной переменной
            const_name = value[1:-1]
            if const_name in self.constants:
                return self.constants[const_name]
            else:
                raise ValueError(f"Неопределенная константа '{const_name}'")
        return value

    def _parse_array(self, value):
        # Разбор массива
        array_content = value[len("array("):-1]
        items = array_content.split(',')
        return [self._parse_value(item.strip()) for item in items]
