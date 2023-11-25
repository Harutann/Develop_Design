def validate_username(username):
    return len(username) <= 15 and username.isalnum()

def validate_password(password):
    return 8 <= len(password) <= 20 and password.isalnum()

def register_user(username, password):
    if not validate_username(username):
        return "15文字以内のユーザー名にしてください"

    if not validate_password(password):
        return "8文字以上20文字以下の半角英数字で入力してください"

    # ここでユーザー情報を保存する処理を追加する（例：データベースへの保存）

    return "登録が完了しました！"

def main():
    while True:
        username = input("ユーザー名を入力してください（15文字以内、英数字のみ）: ")
        password = input("パスワードを入力してください（8文字以上20文字以下、半角英数字のみ）: ")

        result = register_user(username, password)
        print(result)

        if result == "登録が完了しました！":
            break

if __name__ == "__main__":
    main()