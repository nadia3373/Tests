import math

class Calculator:
    @staticmethod
    def calculation(first_operand, second_operand, operator):
        if operator == '+':
            return first_operand + second_operand
        elif operator == '-':
            return first_operand - second_operand
        elif operator == '*':
            return first_operand * second_operand
        elif operator == '/':
            if second_operand != 0:
                return first_operand / second_operand
            else:
                raise ArithmeticError("Division by zero is not possible")
        else:
            raise ValueError(f"Unexpected value operator: {operator}")

    @staticmethod
    def square_root_extraction(num):
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        elif num == 0:
            return 0
        elif math.isinf(num):
            raise ValueError("Cannot calculate square root of infinity")
        elif math.isnan(num):
            raise ValueError("Cannot calculate square root of NaN")
        
        return math.sqrt(num)

    @staticmethod
    def calculating_discount(purchase_amount, discount_amount):
        return purchase_amount - (purchase_amount * discount_amount / 100)
