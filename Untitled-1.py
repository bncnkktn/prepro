"""measure"""
def main():
    """print measure"""
    long = int(input())
    x = sum(i for i in range(1, long)) 
    print("Sum of Found Number = " + str(x))
main()
