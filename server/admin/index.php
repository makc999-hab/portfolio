<?php
// Модерация отзывов: вход по паролю, публикация / скрытие / удаление.
declare(strict_types=1);
require __DIR__ . '/../api/lib.php';

header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('X-Robots-Tag: noindex, nofollow');
header('Cache-Control: no-store');

session_set_cookie_params([
    'lifetime' => 0, 'path' => '/admin/', 'secure' => !empty($_SERVER['HTTPS']),
    'httponly' => true, 'samesite' => 'Strict',
]);
session_start();

function h(string $s): string { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8'); }

if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(16));
$csrf = $_SESSION['csrf'];
$msg = '';

// Вход: не больше 5 неудачных попыток за 15 минут с одного адреса
if (isset($_POST['password'])) {
    $me = client_hash();
    $now = time();
    $blocked = data_update(FAILS_FILE, function (array $f) use ($me, $now) {
        $f[$me] = array_values(array_filter($f[$me] ?? [], fn($t) => $t > $now - 900));
        return [$f, count($f[$me]) >= 5];
    });
    if ($blocked) {
        $msg = 'Слишком много попыток. Подождите 15 минут.';
    } elseif (password_verify((string)$_POST['password'], ADMIN_HASH)) {
        session_regenerate_id(true);
        $_SESSION['admin'] = true;
        header('Location: ./');
        exit;
    } else {
        data_update(FAILS_FILE, function (array $f) use ($me, $now) { $f[$me][] = $now; return [$f, null]; });
        sleep(1);
        $msg = 'Неверный пароль.';
    }
}

if (isset($_GET['logout'])) {
    $_SESSION = [];
    session_destroy();
    header('Location: ./');
    exit;
}

$authed = !empty($_SESSION['admin']);

if ($authed && isset($_POST['action'], $_POST['id'])) {
    if (!hash_equals($csrf, (string)($_POST['csrf'] ?? ''))) {
        http_response_code(400);
        exit('CSRF');
    }
    $id = (string)$_POST['id'];
    $action = (string)$_POST['action'];
    data_update(REVIEWS_FILE, function (array $all) use ($id, $action) {
        foreach ($all as $i => $r) {
            if ($r['id'] !== $id) continue;
            if ($action === 'approve') $all[$i]['status'] = 'approved';
            if ($action === 'hide')    $all[$i]['status'] = 'pending';
            if ($action === 'delete')  unset($all[$i]);
        }
        return [array_values($all), null];
    });
    header('Location: ./');
    exit;
}

$PROJECT_NAMES = ['morehleba' => 'Море хлеба', 'vmr' => 'ВМР ТРАНС', 'greymax' => 'GREYMAX', 'calorieai' => 'CalorieAI', 'other' => 'Другое'];
$reviews = $authed ? data_read(REVIEWS_FILE) : [];
usort($reviews, fn($a, $b) => [$a['status'] === 'approved', $b['created']] <=> [$b['status'] === 'approved', $a['created']]);
$pending = count(array_filter($reviews, fn($r) => $r['status'] === 'pending'));
?>
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Отзывы — модерация</title>
<style>
*{box-sizing:border-box}body{font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;background:#f4f4f4;color:#111;margin:0;padding:24px 16px}
.wrap{max-width:760px;margin:0 auto}h1{font-size:24px;margin:0 0 4px}.sub{color:#666;margin-bottom:20px}
.card{background:#fff;border:1px solid #e5e5e5;border-radius:14px;padding:18px;margin-bottom:12px}
.pending{border-color:#f59e0b;box-shadow:0 0 0 3px #fef3c7}
.meta{font-size:13px;color:#666;margin-bottom:8px}.badge{display:inline-block;font-size:12px;font-weight:600;border-radius:6px;padding:2px 8px;margin-right:6px}
.b-p{background:#fef3c7;color:#92400e}.b-a{background:#dcfce7;color:#166534}
.text{white-space:pre-wrap;margin:8px 0 14px}.row{display:flex;gap:8px;flex-wrap:wrap}
button{font:600 14px inherit;border-radius:9px;border:1.5px solid #111;padding:8px 14px;cursor:pointer;background:#fff}
.ok{background:#111;color:#fff}.del{border-color:#dc2626;color:#dc2626}
input[type=password]{font:inherit;padding:10px 12px;border:1.5px solid #ccc;border-radius:9px;width:100%;margin:10px 0}
.msg{color:#dc2626}.top{display:flex;justify-content:space-between;align-items:baseline}a{color:#111}
</style>
</head>
<body><div class="wrap">
<?php if (!$authed): ?>
  <div class="card" style="max-width:360px;margin:60px auto">
    <h1>Вход</h1>
    <form method="post"><input type="password" name="password" placeholder="Пароль" autofocus required autocomplete="current-password">
    <button class="ok" type="submit">Войти</button></form>
    <?php if ($msg): ?><p class="msg"><?= h($msg) ?></p><?php endif; ?>
  </div>
<?php else: ?>
  <div class="top"><h1>Отзывы</h1><a href="?logout=1">Выйти</a></div>
  <div class="sub">На проверке: <b><?= $pending ?></b> · всего: <?= count($reviews) ?> · <a href="../reviews.html" target="_blank">страница отзывов</a></div>
  <?php if (!$reviews): ?><div class="card">Отзывов пока нет.</div><?php endif; ?>
  <?php foreach ($reviews as $r): $isP = $r['status'] === 'pending'; ?>
  <div class="card <?= $isP ? 'pending' : '' ?>">
    <div class="meta">
      <span class="badge <?= $isP ? 'b-p' : 'b-a' ?>"><?= $isP ? 'На проверке' : 'Опубликован' ?></span>
      <?= h(date('d.m.Y H:i', strtotime($r['created']))) ?> · <?= h($PROJECT_NAMES[$r['project']] ?? $r['project']) ?> · <?= str_repeat('★', (int)$r['rating']) ?> · <?= h(strtoupper($r['lang'])) ?>
    </div>
    <b><?= h($r['name']) ?></b><?= $r['company'] !== '' ? ' — ' . h($r['company']) : '' ?>
    <div class="text"><?= h($r['text']) ?></div>
    <form method="post" class="row">
      <input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="id" value="<?= h($r['id']) ?>">
      <?php if ($isP): ?><button class="ok" name="action" value="approve">Опубликовать</button>
      <?php else: ?><button name="action" value="hide">Скрыть</button><?php endif; ?>
      <button class="del" name="action" value="delete" onclick="return confirm('Удалить отзыв навсегда?')">Удалить</button>
    </form>
  </div>
  <?php endforeach; ?>
<?php endif; ?>
</div></body></html>
