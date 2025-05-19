name_list = []
point_list = []

while True:
       try:
           people_num = int(input("何人採点しますか？"))
           break
       except ValueError:
           print("無効な入力です。")
           continue

for i in range(people_num):
    name = input("名前を入力してください。")

    while True:
        try:
            point = int(input("点数を入力してください。"))
            break
        except ValueError:
            print("無効な入力です。")
            continue

    name_list.append(name)
    point_list.append(point)

print("---- 成績一覧 ----")

def get_rank(score):
    if 0 <= score <= 49:
        return "D"
    elif 50 <= score <= 69:
        return "C"
    elif 70 <= score <= 89:
        return "B"
    elif 90 <= score <= 100:
        return "A"
    else:
        return None

for i in range(people_num):
    rank = get_rank(point_list[i])
    if rank:
        print(f"{name_list[i]}さん：{point_list[i]}点->ランク{rank}")
    else:
        print(f"{name_list[i]}さん：無効な点数です。")

average = sum(point_list) / people_num
print(f"平均点は{average:.1f}点")