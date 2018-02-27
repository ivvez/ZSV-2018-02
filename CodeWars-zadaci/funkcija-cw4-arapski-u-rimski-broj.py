#napisi funkciju koja arapski broj pretvara u rimski

abc = list(zip(('I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M'),
                 (1,4,5,9,10,40,50,90,100,400,500,900,1000)))

def solution(num):
    res = ''
    for i in abc[::-1]:
        if i[1] <= num:
            while num - i[1] >= 0:
                num = num - i[1]
                res = res + i[0]
    return res
