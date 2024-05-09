
def main():
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1, s2)
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')
    str2 = 'abc123456'
    print(str2[-3:-1])  # 45
    print(str2.center(50, '*'))
    list1 = [1, 3, 5, 7, 100]
    for index, elem in enumerate(list1):
        print(index, elem)




if __name__ == '__main__':
    main()