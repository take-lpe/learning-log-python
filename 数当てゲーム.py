import random

print("数字を当ててください（1～100）")

while True:

    Answer_num = random.randint(1, 100)

    count = 1
    while True :
        print(f"現在{count}回目の挑戦！")

        try:
            Input_num = int(input("数字を入力してください。"))
        except ValueError:
            print("数字ではない入力です。")
            continue

        if Answer_num == Input_num:
            print(f"正解！{count}回で正解しました。")
            break
        elif Answer_num > Input_num:
            print("目標より小さいです。")
            count += 1
        elif Answer_num < Input_num:
            print("目標より大きいです。")
            count += 1

    New_game = input("再挑戦しますか？Y/N").strip().upper()

    if New_game == "Y":
        continue
    else:
        print("GAMEOVER")
        break