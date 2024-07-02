def main():

    numbers = []
    
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter 2nd number:"))
    n3 = int(input("Enter 3rd number:"))
    n4 = int(input("Enter 4th number:"))
    n5 = int(input("Enter 5th number:"))
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
