def main():

    numbers = []
    
    for i in range(5):
        num = float(input(f'enter number {i+1}:'))
        numbers.append(num)
        


    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
