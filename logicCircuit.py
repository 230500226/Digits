#DOESN'T WORK 
# import sympy as sp
# import re
# import networkx as nx
# import matplotlib.pyplot as plt

# def preprocess_expression(expression):
#     # Add spaces around operators
#     expression = re.sub(r'([&|~^()])', r' \1 ', expression)
#     # Remove multiple spaces
#     expression = re.sub(r'\s+', ' ', expression).strip()
#     return expression

# def simplify_boolean_expression(expression):
#     # Preprocess the expression to ensure correct parsing
#     expression = preprocess_expression(expression)
    
#     # Define symbols A to Z
#     symbols = {chr(i): sp.symbols(chr(i)) for i in range(65, 91)}
    
#     # Parse the expression
#     parsed_expr = sp.sympify(expression, locals=symbols)
    
#     # Simplify the expression
#     simplified_expr = sp.simplify(parsed_expr)
    
#     return simplified_expr

# def create_graph(expression):
#     # Create a directed graph
#     G = nx.DiGraph()
    
#     # Define symbols A to Z
#     symbols = {chr(i): sp.symbols(chr(i)) for i in range(65, 91)}
    
#     # Parse the expression
#     parsed_expr = sp.sympify(expression, locals=symbols)
    
#     # Recursively add nodes and edges to the graph
#     def add_nodes_edges(expr, parent=None):
#         if expr.is_Atom:
#             G.add_node(str(expr))
#             if parent:
#                 G.add_edge(str(expr), parent)
#         else:
#             op = str(expr.func)
#             G.add_node(op)
#             if parent:
#                 G.add_edge(op, parent)
#             for arg in expr.args:
#                 add_nodes_edges(arg, op)
    
#     add_nodes_edges(parsed_expr, "output")
    
#     return G

# # Example usage
# expression = "A & B | ~C"
# simplified_expr = simplify_boolean_expression(expression)
# graph = create_graph(expression)

# # Draw the graph
# pos = nx.spring_layout(graph)
# nx.draw(graph, pos, with_labels=True, arrows=True)
# plt.show()