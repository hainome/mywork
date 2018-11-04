#coding: utf-8
digit = int(input("何桁？"))
calc_num = input("input number: ")

ans = 0    #一個前の値を格納する
while True:
    
    a = list(calc_num)    #リスト化
    a.sort()
    b = a.copy()
    b.sort(reverse=True)    #aの逆順に並べる
    #0が配列にあった時sort()では一番うしろになってしまうので0があったときにはリストから削除
    
    if '0' in a:
        a.remove("0")
    right = ""   #４つの数字のが最大になるような並び
    left = ""    #４つの数字が最小になるような並び
    for i in a:
        left += i
    for j in b:
        right += j
    if len(b) <= digit - 1:
        right += "0"
    calc_num = str(abs(int(left)-int(right)))
    if calc_num == ans:
        print("Kaprekar Number:", ans)
        break
    ans = calc_num