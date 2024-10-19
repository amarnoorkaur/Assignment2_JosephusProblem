def josephus_formula(n):
    # Calculate Josephus winning position using the mathematical formula
    largest_power_of_two = 1 << (n.bit_length() - 1)  # Find the largest power of 2 less than or equal to n
    l = n - largest_power_of_two  # Difference to adjust
    winning_position = 2 * l + 1  # Formula for winning position
    return winning_position

def binary_rotation(n):
    # Calculate the winner using binary rotation
    binary_str = bin(n)[2:]  # Binary representation without '0b'
    rotated_binary_str = binary_str[1:] + binary_str[0]  # Left rotate the binary string
    rotated_decimal = int(rotated_binary_str, 2)  # Convert back to decimal
    return rotated_decimal

def test_josephus_solution(n):
    # Testing function to compare both methods
    winner_formula = josephus_formula(n)
    winner_binary = binary_rotation(n)
    
    print(f"Testing n = {n}")
    print(f"Josephus Formula Winner: {winner_formula}")
    print(f"Binary Rotation Winner: {winner_binary}")
    print("-" * 40)

# Sample tests to ensure correctness
test_josephus_solution(7)  # Expected result: 7
test_josephus_solution(41)  # Expected result: 19
test_josephus_solution(100)  # Expected result: 73