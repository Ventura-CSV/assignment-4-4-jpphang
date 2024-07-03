def main():

    numbers = []
    
    for i in range(5):
        num = float(input(f'enter number {i+1}:'))
        numbers.append(num)
        
    for num in numbers:
        if num < minval:
            minval = num
        if num > maxval:
            maxval = num
            
    print("all input numbers:", numbers)
    print(maxval, minval)

    print(*numbers)
    print(maxval, minval)

    return numbers, maxval, minval


if __name__ == '__main__':
    main()
