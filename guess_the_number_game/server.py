import sys
import random

# 最小数と最大数をユーザーから受け取る
# 送信される順番で判断して読み取っている
min_number = int(sys.stdin.buffer.readline().decode())
max_number = int(sys.stdin.buffer.readline().decode())

# 乱数を生成
random_number = random.randint(min_number, max_number)

# デバッグ用: 生成された乱数を表示(stderrはerrorを特定する関数)
# Generated random number: 5 or error message
print("Generated random number:", random_number, file=sys.stderr)

# ユーザーの入力を待ち、当てるまでループ
while True:
    # 3番目に入力された値として判断されている。
    user_guess = int(sys.stdin.buffer.readline().decode())
    # 正解だったら、"correct"とファイルに入力
    if user_guess == random_number:
        # 4番目に入力されている
        sys.stdout.buffer.write("correct\n".encode())
        sys.stdout.buffer.flush()
        break
