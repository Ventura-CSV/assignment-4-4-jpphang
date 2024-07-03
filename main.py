def main():

    numbers = []
    
    for i in range(5):
        num = float(input(f'enter number {i+1}:'))
        numbers.append(num)
        
    for num in numbers:
        if num < numbers:
            minval = num
        if num > numbers:
            maxval = num
            
    print("all input numbers:", numbers)
    print(maxval, minval)

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
