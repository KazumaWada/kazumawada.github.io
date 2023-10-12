import sys

# 最小数をユーザーに入力させる
min_number = int(input("Enter the minimum number: "))
# サーバースクリプトに最小数を送信
# '\n'で改行しており、それがデータが区切られているとサーバーが理解している.
sys.stdout.buffer.write(str(min_number).encode() + b'\n')
sys.stdout.buffer.flush()

# 最大数をユーザーに入力させる
max_number = int(input("Enter the maximum number: "))
# サーバースクリプトに最大数を送信
sys.stdout.buffer.write(str(max_number).encode() + b'\n')
sys.stdout.buffer.flush()

# サーバースクリプトからのメッセージを表示
# サーバーに送った情報の結果が返ってくる。
while True:
    message = sys.stdin.buffer.readline().decode()
    # 4番目(4行目)に"correct"と入力されていたら、
    # .stripは、correct\n"->"correct"に直している
    if message.strip() == "correct":
        print("Congratulations! You guessed the number.")
        break

    print(message, end="")

    # サーバーへ送信
    guess_number_input = int(input("Enter the guess number: "))
    sys.stdout.buffer.write(str(guess_number_input).encode() + b'\n')
    sys.stdout.buffer.flush()
