<?php

// Input JSON file
$jsonFile = 'postcodes-pretty.json';

// Output SQL file
$sqlFile = 'postal_codes.sql';

// Read JSON
$jsonData = file_get_contents($jsonFile);
$data = json_decode($jsonData, true);

if (!$data) {
    die("Invalid JSON file\n");
}

// Start SQL
$sql = "-- Auto-generated SQL file\n";
$sql .= "-- Table: postal_codes\n\n";

$sql .= "DROP TABLE IF EXISTS `postal_codes`;\n";
$sql .= "CREATE TABLE `postal_codes` (\n";
$sql .= "  `id` INT AUTO_INCREMENT PRIMARY KEY,\n";
$sql .= "  `postal_code` VARCHAR(10) NOT NULL,\n";
$sql .= "  `division_en` VARCHAR(100),\n";
$sql .= "  `district_en` VARCHAR(100),\n";
$sql .= "  `thana_en` VARCHAR(100),\n";
$sql .= "  `suboffice_en` VARCHAR(150),\n";
$sql .= "  `division_bn` VARCHAR(100),\n";
$sql .= "  `district_bn` VARCHAR(100),\n";
$sql .= "  `thana_bn` VARCHAR(100),\n";
$sql .= "  `suboffice_bn` VARCHAR(150),\n";
$sql .= "  UNIQUE KEY `postal_code_unique` (`postal_code`)\n";
$sql .= ") CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n\n";

$sql .= "INSERT INTO `postal_codes`
(`postal_code`, `division_en`, `district_en`, `thana_en`, `suboffice_en`,
 `division_bn`, `district_bn`, `thana_bn`, `suboffice_bn`)
VALUES\n";

$values = [];

foreach ($data as $code => $entry) {
    $en = $entry['en'];
    $bn = $entry['bn'];

    $values[] = sprintf(
        "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')",
        addslashes($code),
        addslashes($en['division']),
        addslashes($en['district']),
        addslashes($en['thana']),
        addslashes($en['suboffice']),
        addslashes($bn['division']),
        addslashes($bn['district']),
        addslashes($bn['thana']),
        addslashes($bn['suboffice'])
    );
}

$sql .= implode(",\n", $values) . ";\n";

// Write SQL file
file_put_contents($sqlFile, $sql);

echo "SQL file generated successfully: {$sqlFile}\n";
