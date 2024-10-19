def josephus_formula(n):
    # Using bit-shifting to find largest power of 2 <= n
    max_power_of_two = 1 << (n.bit_length() - 1)  # One-liner hack
    l = n - max_power_of_two  # Leftover people after filling the circle
    return 2 * l + 1  # Direct formula: safe spot after adjustments

def binary_rotation(n):
    # Binary approach: rotate the leftmost bit to the end, quick and dirty
    binary_str = bin(n)[2:]  # Stripping '0b' from binary
    rotated_binary_str = binary_str[1:] + binary_str[0]  # Rotate bits, nothing fancy
    return int(rotated_binary_str, 2)  # Convert back to decimal

# A quick and simple test function to compare the two methods
def test_josephus_methods(n):
    print(f"\nFor n = {n}:")
    
    # Call the formula method
    formula_winner = josephus_formula(n)
    print(f"Formula-based Winner: {formula_winner}")

    # Call the binary rotation method
    binary_winner = binary_rotation(n)
    print(f"Binary-based Winner: {binary_winner}")

    # Double check both are the same, or something’s wrong
    assert formula_winner == binary_winner, "Mismatch! Something went wrong!"

# Running a few test cases, because why not?
for n in [7, 41, 100]:
    test_josephus_methods(n)