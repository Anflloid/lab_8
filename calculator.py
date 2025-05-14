class Calculator:
    @staticmethod
    def add(a, b):
        """Додавання двох чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Obydva arhumenty povynni buty chyslamy")
        return a + b

    @staticmethod
    def subtract(a, b):
        """Віднімання двох чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Obydva arhumenty povynni buty chyslamy")
        return a - b

    @staticmethod
    def multiply(a, b):
        """Множення двох чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Obydva arhumenty povynni buty chyslamy")
        return a * b

    @staticmethod
    def divide(a, b):
        """Ділення двох чисел"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("ОObydva arhumenty povynni buty chyslamy")
        if b == 0:
            raise ValueError("Dilennya na nulʹ nemozhlyve")
        return a / b

    @classmethod
    def calculate(cls, a, b, operation):
        """Виконання операції з обробкою помилок"""
        operations = {
            '+': cls.add,
            '-': cls.subtract,
            '*': cls.multiply,
            '/': cls.divide
        }

        if operation not in operations:
            raise ValueError("Nevidoma operatsiya")

        return operations[operation](a, b)