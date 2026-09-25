#!/bin/sh
# Генерирует server-secret/config.php с новым паролем админки. Пароль печатается один раз.
set -e
cd "$(dirname "$0")"
mkdir -p server-secret
PASS=$(python3 -c "import secrets,string;a=string.ascii_letters+string.digits;print(''.join(secrets.choice(a) for _ in range(16)))")
HASH=$(php -r 'echo password_hash($argv[1], PASSWORD_DEFAULT);' "$PASS")
SALT=$(python3 -c "import secrets;print(secrets.token_hex(16))")
cat > server-secret/config.php <<PHP
<?php
const ADMIN_HASH = '$HASH';
const SALT = '$SALT';
const ALLOWED_ORIGINS = ['https://maxperepelitsa.store', 'http://maxperepelitsa.store', 'https://www.maxperepelitsa.store', 'http://localhost:8099'];
PHP
chmod 600 server-secret/config.php
echo "$PASS" > server-secret/admin-password.txt
chmod 600 server-secret/admin-password.txt
echo "Пароль админки сохранён в server-secret/admin-password.txt"
