import sympy as sp
import re

def preprocess_expression(expression):
    # Add spaces around operators
    expression = re.sub(r'([&|~^()])', r' \1 ', expression)
    # Remove multiple spaces
    expression = re.sub(r'\s+', ' ', expression).strip()
    return expression

def simplify_boolean_expression(expression):
    # Preprocess the expression to ensure correct parsing
    expression = preprocess_expression(expression)
    
    # Define symbols A to Z
    symbols = {chr(i): sp.symbols(chr(i)) for i in range(65, 91)}
    
    # Parse the expression
    parsed_expr = sp.sympify(expression, locals=symbols)
    
    # Simplify the expression
    simplified_expr = sp.simplify_logic(parsed_expr)
    
    return simplified_expr

def main():
    print("Enter a boolean algebra expression using symbols A to Z.")
    print("Use operators: & (AND), | (OR), ~ (NOT), ^ (XOR)")
    print("You can group symbols using parentheses. Example: ~(A & B) | C")
    
    expression = input("Enter your boolean expression: ")
    simplified_expression = simplify_boolean_expression(expression)
    
    print(f"Simplified expression: {simplified_expression}")

if __name__ == "__main__":
    main()