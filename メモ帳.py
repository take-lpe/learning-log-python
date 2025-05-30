openfile = "memo.txt"

while True:
    mode = input("write=書く, read=読む:")
    #書き込みモード
    if mode == "write":
            memo = input("書き残したい内容を入力してください。")
            with open(openfile, "a", encoding="UTF-8") as f:
                f.write(memo + "\n")
                print("メモを保存しました。")
    #読むモード
    elif mode == "read":
        with open(openfile, "r", encoding="UTF-8") as f:
            print(f.read())
    else:
        print("モードを正しく選択してください。")
        continue