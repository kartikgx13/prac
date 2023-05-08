def find_first(grammar, symbol):
    first_set = set()

    # Base case: if the symbol is a terminal, add it to the first set
    # so like here the key is the grammar and the values are the production rules
    if symbol not in grammar:
        first_set.add(symbol)
        return first_set

    # Recursive case: symbol is a non-terminal
    for production in grammar[symbol]:
        # Check the first symbol in the production
        first_symbol = production[0]

        # If the first symbol is epsilon, add it to the first set
        if first_symbol == 'ε':
            first_set.add('ε')
        # If the first symbol is a terminal, add it to the first set
        elif first_symbol not in grammar:
            first_set.add(first_symbol)
        # If the first symbol is a non-terminal, find its first set recursively
        else:
            first_set.update(find_first(grammar, first_symbol))

    return first_set


# Example grammar
example_grammar = {
    'S': ['AB', 'BC'],
    'A': ['a', 'ε'],
    'B': ['b'],
    'C': ['c', 'ε']
}

# Compute the first set for each symbol in the grammar
first_sets = {}
for symbol in example_grammar:
    first_sets[symbol] = find_first(example_grammar, symbol)

# Print the first sets
for symbol, first_set in first_sets.items():
    print(f'First({symbol}) = {first_set}')
