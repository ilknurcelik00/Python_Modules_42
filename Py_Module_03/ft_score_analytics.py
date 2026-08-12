import sys

print("=== Player Score Analytics ===")
n = len(sys.argv)
total = 0
for i in range(1,n):
    print(f"Scores processed: [{sys.argv[i]}",end=", ")
    total = sum(sys.argv[i])
print("]")
    
print(f"Total Players: {n-1}")
print(f"Total score: {total}")
print(f"Avarage score: {total / n-1}")
