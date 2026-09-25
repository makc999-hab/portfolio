<?php
// GET  — опубликованные отзывы; POST — новый отзыв (уходит на модерацию).
declare(strict_types=1);
require __DIR__ . '/lib.php';

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

if ($method === 'GET') {
    $out = [];
    foreach (data_read(REVIEWS_FILE) as $r) {
        if (($r['status'] ?? '') !== 'approved') continue;
        $out[] = [
            'name'    => $r['name'],
            'company' => $r['company'],
            'project' => $r['project'],
            'rating'  => $r['rating'],
            'text'    => $r['text'],
            'date'    => substr($r['created'], 0, 7),
        ];
    }
    usort($out, fn($a, $b) => strcmp($b['date'], $a['date']));
    json_out(['ok' => true, 'reviews' => $out]);
}

if ($method !== 'POST') json_out(['ok' => false, 'error' => 'method'], 405);

// Запросы только со своего сайта
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && !in_array($origin, ALLOWED_ORIGINS, true)) {
    json_out(['ok' => false, 'error' => 'origin'], 403);
}

$raw = file_get_contents('php://input', false, null, 0, 8192);
$in = json_decode($raw ?: '', true);
if (!is_array($in)) json_out(['ok' => false, 'error' => 'bad_request'], 400);

// Ловушки для ботов: скрытое поле и слишком быстрое заполнение формы.
// Боту отвечаем «успехом», чтобы он не подбирал обход.
if (!empty($in['website']) || (int)($in['elapsed'] ?? 0) < 4000) {
    json_out(['ok' => true]);
}

$name    = clean_text((string)($in['name'] ?? ''), 60);
$company = clean_text((string)($in['company'] ?? ''), 80);
$text    = clean_text((string)($in['text'] ?? ''), 1000);
$project = in_array($in['project'] ?? '', PROJECTS, true) ? $in['project'] : 'other';
$rating  = max(1, min(5, (int)($in['rating'] ?? 5)));
$lang    = ($in['lang'] ?? 'ru') === 'en' ? 'en' : 'ru';

$errors = [];
if (mb_strlen($name) < 2)  $errors[] = 'name';
if (mb_strlen($text) < 20) $errors[] = 'text';
if (($in['consent'] ?? false) !== true) $errors[] = 'consent';
if (preg_match('~https?://|www\.~i', $text . $name . $company)) $errors[] = 'links';
if ($errors) json_out(['ok' => false, 'error' => 'validation', 'fields' => $errors], 422);

// Не больше 3 отзывов в сутки с одного адреса (храним только хэш IP)
$now = time();
$me = client_hash();
$allowed = data_update(RATE_FILE, function (array $rate) use ($now, $me) {
    foreach ($rate as $k => $times) {
        $rate[$k] = array_values(array_filter($times, fn($t) => $t > $now - 86400));
        if (!$rate[$k]) unset($rate[$k]);
    }
    $mine = $rate[$me] ?? [];
    if (count($mine) >= 3) return [$rate, false];
    $mine[] = $now;
    $rate[$me] = $mine;
    return [$rate, true];
});
if (!$allowed) json_out(['ok' => false, 'error' => 'rate'], 429);

data_update(REVIEWS_FILE, function (array $all) use ($name, $company, $text, $project, $rating, $lang, $now) {
    $all[] = [
        'id'         => bin2hex(random_bytes(8)),
        'status'     => 'pending',
        'name'       => $name,
        'company'    => $company,
        'project'    => $project,
        'rating'     => $rating,
        'text'       => $text,
        'lang'       => $lang,
        'created'    => date('c', $now),
        'consent_at' => date('c', $now),
    ];
    return [$all, null];
});

json_out(['ok' => true]);
