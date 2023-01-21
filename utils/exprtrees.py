class Operand():
    def __init__(self, value: int):
        self._val = value

    def to_string(self, depth: int=0):
        return ("  " * depth) + str(self._val)

    def evaluate(self):
        return self._val

class BinaryOperator():
    def __init__(self, left, right):
        self._left = left
        self._right = right
        self._string = "."

    def to_string(self, depth: int=0) -> str:
        return self._right.to_string(depth=depth + 1) + "\n" + \
               ("  " * depth) + self._string + "\n" + \
               self._left.to_string(depth=depth + 1)

    def evaluate(self):
        return self

class Add(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self._string = "+"

    def evaluate(self):
        return self._left.evaluate() + self._right.evaluate()

class Sub(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self._string = "-"
        
    def evaluate(self):
        return self._left.evaluate() - self._right.evaluate()

class Mul(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self._string = "*"
        
    def evaluate(self):
        return self._left.evaluate() * self._right.evaluate()

class Div(BinaryOperator):
    def __init__(self, left, right):
        super().__init__(left, right)
        self._string = "/"
        
    def evaluate(self):
        return self._left.evaluate() / self._right.evaluate()


# The following methods are derived from Homework 5 of the 2017 W&M
# course "CSCI 241: Data Structures", taught by Jim Deverick.

def infix_to_postfix(infix_expression: str) -> str:
    """
    Returns the postfix representation of `infix_expression`. Only single-
    digit operands are supported. The unary '-' operator is not supported.
    """
    
    # Pre-processing step to handle operator precedence; see <en.wikipedia.org/wiki/Operator-precedence_parser#Alternative_methods>
    infix_expression = '(((' + \
        infix_expression.replace('(', '(((')   \
                        .replace(')', ')))')   \
                        .replace('+', '))+((') \
                        .replace('-', '))-((') \
                        .replace('*', ')*(')   \
                        .replace('/', ')/(') + ')))'
    result = ''
    oper_stack = []
    for sym in infix_expression:
        if sym in '0123456789':
            result += sym
        elif sym in '+-*/(':
            oper_stack.append(sym)
        elif sym == ')':
            while True:
                p = oper_stack.pop()
                if p == '(':
                    break
                result += p
    while oper_stack:
        result += oper_stack.pop()
    return result

def postfix_to_tree(expression: str) -> BinaryOperator:
    stack = []
    for sym in expression:
        if sym in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if sym == "+":
                op = Add
            elif sym == "-":
                op = Sub
            elif sym == "*":
                op = Mul
            else:
                op = Div
            stack.append(op(left, right))
        elif sym in "0123456789":
            stack.append(Operand(int(sym)))
        else:
            raise ValueError(f"unrecognized symbol '{sym}'")
    return stack.pop()


if __name__ == "__main__":
    expressions = [
        "(4 * (1 + 3)) / 2",
        "4 * (3 + 1 / 2)",
        "4 * (2 + 3) - 1",
        "3 * 4 * (2 + 1)"]
    for infix in expressions:
        postfix = infix_to_postfix(infix)
        expr = postfix_to_tree(postfix)
        print()
        print(infix)
        print(postfix)
        print(expr.to_string())
        print("==>", expr.evaluate())
    # print(infix_to_postfix("((1 + 2) + (3 + 4))"))