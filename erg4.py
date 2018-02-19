conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 80, 'LXXX'], [ 70, 'LXX'], [ 60, 'LX' ], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]
num = input("enter your number: \n")
roman = ''
i = 0
if num > 0 and num<4000:
    while conv[i][0] > num: i+=1
    roman += conv[i][1]
    num -= conv[i][0]
    print roman
elif num>=4000:
    p = num/1000
    while conv[i][0] > p: i+=1
    roman += conv[i][1]
    p -= conv[i][0]
    print "-",roman
    
