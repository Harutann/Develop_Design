<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>

    <?php
    function validate_username($username) {
        return strlen($username) <= 15 && ctype_alnum($username);
    }

    function validate_password($password) {
        return strlen($password) >= 8 && strlen($password) <= 20 && ctype_alnum($password);
    }

    function register_user($username, $password) {
        if (!validate_username($username)) {
            return "15文字以内のユーザー名にしてください";
        }

        if (!validate_password($password)) {
            return "8文字以上20文字以下の半角英数字で入力してください";
        }

        // ここでユーザー情報を保存する処理を追加する（例：データベースへの保存）

        return "登録が完了しました！";
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $input_username = $_POST["username"];
        $input_password = $_POST["password"];

        $result = register_user($input_username, $input_password);
        echo "<p>$result</p>";
    }
    ?>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <p>
            <label for="username">ユーザー名:</label>
            <input type="text" id="username" name="username" maxlength="15"><br>
        </p>
        <p>
            <label for="password">パスワード:</label>
            <input type="password" id="password" name="password" minlength="8" maxlength="20"><br>
        </p>
        <p>
            <input type="submit" value="登録">
        </p>
    </form>
</body>
</html>