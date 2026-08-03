import random

# 同じイベントが重複して入っているリスト
#（ランダム生成なので、本番でも10回中数回は確実にこうなります）
events_list = [
    ("bob", "run"),    # 0番目
    ("alice", "eat"),  # 1番目
    ("bob", "run")     # 2番目
]

print("--- リアルな不具合の再現開始 ---")

# 1. 2番目の ("bob", "run") が選ばれたと仮定します
list_remain = events_list[2]
print(f"1. ランダムに選ばれた要素: {list_remain} (本当は2番目を処理したい)")

# 2. removeを実行すると「0番目」が消える
events_list.remove(list_remain)
print(f"2. remove後のリストの中身: {events_list}")

# 3. 本番のコードはここから for ループで次の要素（2回目）を処理します
# 2回目：また2番目の ("bob", "run") が選ばれたと仮定します
list_remain = events_list[1]# 要素が減ったので現在の2番目はインデックス1
print(f"3. 次にランダムに選ばれた要素: {list_remain}")

# 4. もう一度 removeを実行すると、また「現在の先頭(0番目)」を探して消します
events_list.remove(list_remain)
print(f"4. 2回目のremove後のリスト: {events_list}")

# 🚨 ここで注目！！
# 本来なら2回処理したのでリストの残りは1つのはずですが、
# 「処理したはずのデータ」と「消えたデータ」のズレが原因で、
# ループの判定が狂い、ここから無限ループに突入します。

while events_list:
    # 3回目以降、残ったデータに対してremoveを繰り返すと...
    try:
        list_remain = random.choice(events_list)
        events_list.remove(list_remain)
        print(f"ループ中... 残りリスト: {events_list}")
    except ValueError:
        # 存在しない場所を消そうとしてエラーが出たり、
        # 条件が噛み合わずにwhileが一生終わらなくなります
        print("🚨 エラーが発生するか、無限にループが回り続けます")
        break
