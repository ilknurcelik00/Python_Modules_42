import sys
print("=== Command Quest ===")
n = len(sys.argv)
print("Program name:", sys.argv[0])
if n == 1:
    print("No arguments provided!")
else:
    print("Arguments received:", n-1)

for i in range(1, n):
    print(f"Argument {i}: {sys.argv[i]}")
print("Total arguments:", n, "\n")
