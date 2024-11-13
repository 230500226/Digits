import sympy as sp
import re
import matplotlib.pyplot as plt

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

def evaluate_expression(expression, symbols, values):
    # Create a dictionary mapping symbols to their values
    symbol_values = {symbols[i]: values[i] for i in range(len(symbols))}
    
    # Substitute the values into the expression
    evaluated_expr = expression.subs(symbol_values)
    
    # Convert the evaluated expression to an integer (0 or 1)
    if evaluated_expr == sp.true:
        return 1
    elif evaluated_expr == sp.false:
        return 0
    else:
        # Convert the evaluated expression to a boolean and then to an integer
        return int(bool(evaluated_expr))

def main():
    print("Enter the simplified boolean expression using symbols A to Z.")
    expression_str = input("Enter your simplified boolean expression: ")
    
    # Define symbols A to Z
    symbols = {chr(i): sp.symbols(chr(i)) for i in range(65, 91)}
    
    # Parse the expression
    try:
        expression = sp.sympify(expression_str, locals=symbols)
    except sp.SympifyError:
        print("Invalid expression. Please try again.")
        return
    
    # Extract the symbols used in the expression
    used_symbols = sorted(expression.free_symbols, key=lambda x: str(x))
    
    print(f"Symbols used in the expression: {', '.join(map(str, used_symbols))}")
    
    num_cycles = int(input("Enter the number of cycles: "))
    
    # Initialize lists to store the results
    results = []
    
    for cycle in range(num_cycles):
        print(f"Cycle {cycle + 1}:")
        values = []
        for symbol in used_symbols:
            while True:
                try:
                    value = int(input(f"Enter the value for {symbol} (0 or 1): "))
                    if value in [0, 1]:
                        values.append(value)
                        break
                    else:
                        print("Please enter 0 or 1.")
                except ValueError:
                    print("Invalid input. Please enter 0 or 1.")
        
        result = evaluate_expression(expression, used_symbols, values)
        results.append(result)
    
    # Plot the results
    plt.plot(range(1, num_cycles + 1), results, marker='o')
    plt.xlabel('Cycle')
    plt.ylabel('Expression Result')
    plt.title('Boolean Expression Evaluation')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()