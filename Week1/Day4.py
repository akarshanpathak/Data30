# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate prime numbers between 1 and 100
primes = [n for n in range(1, 101) if is_prime(n)]

# Print the prime numbers
print("Prime numbers between 1 and 100 are:")
print(primes)

# Save the prime numbers in a file
with open("primes.txt", "w") as file:
    for p in primes:
        file.write(str(p) + "\n")

print("Prime numbers have been saved in 'primes.txt'")
