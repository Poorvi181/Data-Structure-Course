
def countdown(n):
    # Base Case
    if n <= 0:
        print("Blast off!")
        return
    
    print(n)
    countdown(n - 1)

countdown(5)