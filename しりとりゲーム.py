while True:
    ward1 = input("１つ目の単語＝")
    if ward1 == "END":
        print("しりとり終了")
        break

    ward2 = input("２つ目の単語＝")
    if ward2 == "END":
        print("しりとり終了")
        break

    if ward1[-1] == ward2[0]:
        if ward2[-1] == 'ん':
            print('ゲームオーバー')
        else:
            print('しりとりOK！')
    else:
        print('しりとりNG！')
