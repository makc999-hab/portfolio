<?php
// Общие функции отзывов: хранение в JSON-файлах с блокировкой.
declare(strict_types=1);

require __DIR__ . '/config.php'; // ADMIN_HASH, SALT, ALLOWED_ORIGINS — не в git

const DATA_DIR     = __DIR__ . '/data';
const REVIEWS_FILE = DATA_DIR . '/reviews.json';
const RATE_FILE    = DATA_DIR . '/rate.json';
const FAILS_FILE   = DATA_DIR . '/admin_fails.json';

const PROJECTS = ['morehleba', 'vmr', 'greymax', 'calorieai', 'other'];

function ensure_data_dir(): void {
    if (!is_dir(DATA_DIR)) {
        mkdir(DATA_DIR, 0700, true);
    }
    $ht = DATA_DIR . '/.htaccess';
    if (!file_exists($ht)) {
        file_put_contents($ht, "<IfModule mod_authz_core.c>\nRequire all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\nDeny from all\n</IfModule>\n");
    }
}

function data_read(string $file): array {
    if (!is_file($file)) return [];
    $fp = fopen($file, 'r');
    if (!$fp) return [];
    flock($fp, LOCK_SH);
    $raw = stream_get_contents($fp);
    flock($fp, LOCK_UN);
    fclose($fp);
    $data = json_decode($raw ?: '[]', true);
    return is_array($data) ? $data : [];
}

/** Атомарно читает файл, передаёт массив в $fn и записывает то, что она вернула. */
function data_update(string $file, callable $fn) {
    ensure_data_dir();
    $fp = fopen($file, 'c+');
    if (!$fp) throw new RuntimeException('cannot open data file');
    flock($fp, LOCK_EX);
    $raw = stream_get_contents($fp);
    $data = json_decode($raw ?: '[]', true);
    if (!is_array($data)) $data = [];
    [$new, $result] = $fn($data);
    ftruncate($fp, 0);
    rewind($fp);
    fwrite($fp, json_encode($new, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
    fflush($fp);
    flock($fp, LOCK_UN);
    fclose($fp);
    return $result;
}

function client_hash(): string {
    return hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . SALT);
}

function clean_text(string $s, int $max): string {
    $s = strip_tags($s);
    $s = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $s) ?? '';
    $s = preg_replace("/\n{3,}/", "\n\n", str_replace("\r", '', $s)) ?? '';
    $s = trim($s);
    return mb_substr($s, 0, $max);
}

function json_out(array $payload, int $code = 200): void {
    http_response_code($code);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    header('X-Content-Type-Options: nosniff');
    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    exit;
}
