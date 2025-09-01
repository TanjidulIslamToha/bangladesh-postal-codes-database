#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import os
from typing import Dict, List, Tuple

WORKDIR = os.path.dirname(os.path.abspath(__file__))
SRC_JSON = os.path.join(WORKDIR, "postcodes-pretty.json")

OUT_DIR = os.path.join(WORKDIR, "variations")
BN_DIR = os.path.join(OUT_DIR, "bn")
EN_DIR = os.path.join(OUT_DIR, "en")
RANGES_DIR = os.path.join(OUT_DIR, "ranges")
SUMMARY_DIR = os.path.join(OUT_DIR, "summary")
DIVISIONS_DIR = os.path.join(OUT_DIR, "divisions")
DISTRICTS_DIR = os.path.join(OUT_DIR, "districts")
FLAT_DIR = os.path.join(OUT_DIR, "flat")
INDEX_DIR = os.path.join(OUT_DIR, "index")
UNIQUE_DIR = os.path.join(OUT_DIR, "unique")
MIN_DIR = os.path.join(OUT_DIR, "min")

# District code ranges (inclusive) same as previously validated
RANGES: List[Tuple[int, int, str]] = [
    (1000, 1399, "Dhaka"), (1400, 1499, "Narayanganj"), (1500, 1599, "Munshiganj"), (1600, 1699, "Narsingdi"), (1700, 1799, "Gazipur"), (1800, 1899, "Manikganj"), (1900, 1999, "Tangail"), (2300, 2399, "Kishoreganj"),
    (2000, 2099, "Jamalpur"), (2100, 2199, "Sherpur"), (2200, 2299, "Mymensingh"), (2400, 2499, "Netrokona"),
    (3000, 3099, "Sunamganj"), (3100, 3199, "Sylhet"), (3200, 3299, "Moulvibazar"), (3300, 3399, "Habiganj"),
    (3400, 3499, "Brahmanbaria"), (3500, 3599, "Cumilla"), (3600, 3699, "Chandpur"), (3700, 3799, "Lakshmipur"), (3800, 3899, "Noakhali"), (3900, 3999, "Feni"),
    (4000, 4399, "Chittagong"), (4400, 4499, "Khagrachhari"), (4500, 4599, "Rangamati"), (4600, 4699, "Bandarban"), (4700, 4799, "Cox's Bazar"),
    (5000, 5099, "Panchagarh"), (5100, 5199, "Thakurgaon"), (5200, 5299, "Dinajpur"), (5300, 5399, "Nilphamari"), (5400, 5499, "Rangpur"), (5500, 5599, "Lalmonirhat"), (5600, 5699, "Kurigram"), (5700, 5799, "Gaibandha"),
    (5800, 5899, "Bogura"), (5900, 5999, "Joypurhat"), (6000, 6299, "Rajshahi"), (6300, 6399, "Chapai Nawabganj"), (6400, 6499, "Natore"), (6500, 6599, "Naogaon"), (6600, 6699, "Pabna"), (6700, 6799, "Sirajganj"),
    (7000, 7099, "Kushtia"), (7100, 7199, "Meherpur"), (7200, 7299, "Chuadanga"), (7300, 7399, "Jhenaidah"), (7400, 7499, "Jashore"), (7500, 7599, "Narail"), (7600, 7699, "Magura"), (9000, 9299, "Khulna"), (9300, 9399, "Bagerhat"), (9400, 9499, "Satkhira"),
    (8200, 8299, "Barisal"), (8300, 8399, "Bhola"), (8400, 8499, "Jhalokati"), (8500, 8599, "Pirojpur"), (8600, 8699, "Patuakhali"), (8700, 8799, "Barguna"),
]


def read_data() -> Dict[str, dict]:
    with open(SRC_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_csv(path: str, rows: List[List[str]], header: List[str]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_dirs() -> None:
    for d in (
        OUT_DIR, BN_DIR, EN_DIR, RANGES_DIR, SUMMARY_DIR,
        DIVISIONS_DIR, DISTRICTS_DIR, FLAT_DIR, INDEX_DIR, UNIQUE_DIR, MIN_DIR,
    ):
        os.makedirs(d, exist_ok=True)


def build_bn(data: Dict[str, dict]) -> Tuple[Dict[str, dict], List[List[str]]]:
    bn_json: Dict[str, dict] = {}
    bn_csv: List[List[str]] = []
    for code, obj in data.items():
        bn = obj.get("bn", {})
        bn_json[code] = bn
        bn_csv.append([
            code,
            bn.get("division", ""),
            bn.get("district", ""),
            bn.get("thana", ""),
            bn.get("suboffice", ""),
            bn.get("postcode", ""),
        ])
    return bn_json, bn_csv


def build_en(data: Dict[str, dict]) -> Tuple[Dict[str, dict], List[List[str]]]:
    en_json: Dict[str, dict] = {}
    en_csv: List[List[str]] = []
    for code, obj in data.items():
        en = obj.get("en", {})
        en_json[code] = en
        en_csv.append([
            code,
            en.get("division", ""),
            en.get("district", ""),
            en.get("thana", ""),
            en.get("suboffice", ""),
            str(en.get("postcode", "")),
        ])
    return en_json, en_csv


def build_ranges_csv() -> List[List[str]]:
    rows: List[List[str]] = []
    for start, end, district in RANGES:
        rows.append([str(start), str(end), district])
    return rows


def build_summaries(data: Dict[str, dict]) -> Tuple[List[List[str]], List[List[str]], List[List[str]]]:
    # counts per division (en), district (en), thana (en)
    from collections import Counter
    div_c = Counter()
    dis_c = Counter()
    thana_c = Counter()
    for code, obj in data.items():
        en = obj.get("en", {})
        div_c[en.get("division", "")] += 1
        dis_c[en.get("district", "")] += 1
        thana_c[en.get("thana", "")] += 1
    div_rows = [[k, str(v)] for k, v in sorted(div_c.items())]
    dis_rows = [[k, str(v)] for k, v in sorted(dis_c.items())]
    th_rows = [[k, str(v)] for k, v in sorted(thana_c.items())]
    return div_rows, dis_rows, th_rows


def slugify(name: str) -> str:
    import re
    s = name.strip().lower()
    s = s.replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "_"


def build_division_splits(data: Dict[str, dict]) -> None:
    # combined JSON/CSV per division (using English division name for folder/file naming)
    from collections import defaultdict
    div_to_codes = defaultdict(list)
    for code, obj in data.items():
        en = obj.get("en", {})
        div = en.get("division", "").strip()
        if div:
            div_to_codes[div].append(code)

    for div, codes in div_to_codes.items():
        codes_sorted = sorted(codes, key=lambda c: int(c))
        slug = slugify(div)
        target_dir = os.path.join(DIVISIONS_DIR, slug)
        os.makedirs(target_dir, exist_ok=True)

        # JSON (combined)
        combined = {code: data[code] for code in codes_sorted}
        write_json(os.path.join(target_dir, f"division-{slug}.json"), combined)

        # CSV (combined)
        rows: List[List[str]] = []
        for code in codes_sorted:
            obj = data[code]
            bn = obj.get("bn", {})
            en = obj.get("en", {})
            rows.append([
                code,
                bn.get("division", ""), bn.get("district", ""), bn.get("thana", ""), bn.get("suboffice", ""), bn.get("postcode", ""),
                en.get("division", ""), en.get("district", ""), en.get("thana", ""), en.get("suboffice", ""), str(en.get("postcode", "")),
            ])
        write_csv(
            os.path.join(target_dir, f"division-{slug}.csv"),
            rows,
            [
                "postcode",
                "bn_division", "bn_district", "bn_thana", "bn_suboffice", "bn_postcode",
                "en_division", "en_district", "en_thana", "en_suboffice", "en_postcode",
            ],
        )


def build_district_splits(data: Dict[str, dict]) -> None:
    # combined JSON/CSV per district (English district name for naming)
    from collections import defaultdict
    dis_to_codes = defaultdict(list)
    for code, obj in data.items():
        en = obj.get("en", {})
        dis = en.get("district", "").strip()
        if dis:
            dis_to_codes[dis].append(code)

    for dis, codes in dis_to_codes.items():
        codes_sorted = sorted(codes, key=lambda c: int(c))
        slug = slugify(dis)
        target_dir = os.path.join(DISTRICTS_DIR, slug)
        os.makedirs(target_dir, exist_ok=True)

        combined = {code: data[code] for code in codes_sorted}
        write_json(os.path.join(target_dir, f"district-{slug}.json"), combined)

        rows: List[List[str]] = []
        for code in codes_sorted:
            obj = data[code]
            bn = obj.get("bn", {})
            en = obj.get("en", {})
            rows.append([
                code,
                bn.get("division", ""), bn.get("district", ""), bn.get("thana", ""), bn.get("suboffice", ""), bn.get("postcode", ""),
                en.get("division", ""), en.get("district", ""), en.get("thana", ""), en.get("suboffice", ""), str(en.get("postcode", "")),
            ])
        write_csv(
            os.path.join(target_dir, f"district-{slug}.csv"),
            rows,
            [
                "postcode",
                "bn_division", "bn_district", "bn_thana", "bn_suboffice", "bn_postcode",
                "en_division", "en_district", "en_thana", "en_suboffice", "en_postcode",
            ],
        )


def build_flat_files(data: Dict[str, dict]) -> None:
    # Flat CSV with both bn & en columns for all postcodes
    rows: List[List[str]] = []
    for code in sorted(data.keys(), key=lambda c: int(c)):
        obj = data[code]
        bn = obj.get("bn", {})
        en = obj.get("en", {})
        rows.append([
            code,
            bn.get("division", ""), bn.get("district", ""), bn.get("thana", ""), bn.get("suboffice", ""), bn.get("postcode", ""),
            en.get("division", ""), en.get("district", ""), en.get("thana", ""), en.get("suboffice", ""), str(en.get("postcode", "")),
        ])
    write_csv(
        os.path.join(FLAT_DIR, "postcodes-flat.csv"),
        rows,
        [
            "postcode",
            "bn_division", "bn_district", "bn_thana", "bn_suboffice", "bn_postcode",
            "en_division", "en_district", "en_thana", "en_suboffice", "en_postcode",
        ],
    )


def build_indexes_and_unique(data: Dict[str, dict]) -> None:
    from collections import defaultdict
    # Indexes mapping name -> list of postcodes
    div_index_en: Dict[str, List[int]] = defaultdict(list)
    dis_index_en: Dict[str, List[int]] = defaultdict(list)
    th_index_en: Dict[str, List[int]] = defaultdict(list)
    so_index_en: Dict[str, List[int]] = defaultdict(list)
    th_index_bn: Dict[str, List[int]] = defaultdict(list)
    so_index_bn: Dict[str, List[int]] = defaultdict(list)

    unique_th_en = set()
    unique_th_bn = set()
    unique_so_en = set()
    unique_so_bn = set()

    for code in sorted(data.keys(), key=lambda c: int(c)):
        obj = data[code]
        bn = obj.get("bn", {})
        en = obj.get("en", {})
        c = int(code)
        div_index_en[en.get("division", "")].append(c)
        dis_index_en[en.get("district", "")].append(c)
        th_index_en[en.get("thana", "")].append(c)
        so_index_en[en.get("suboffice", "")].append(c)
        th_index_bn[bn.get("thana", "")].append(c)
        so_index_bn[bn.get("suboffice", "")].append(c)
        if en.get("thana"): unique_th_en.add(en.get("thana"))
        if bn.get("thana"): unique_th_bn.add(bn.get("thana"))
        if en.get("suboffice"): unique_so_en.add(en.get("suboffice"))
        if bn.get("suboffice"): unique_so_bn.add(bn.get("suboffice"))

    def write_index_json(name: str, index: Dict[str, List[int]]):
        # sort lists
        sorted_index = {k: sorted(v) for k, v in index.items() if k}
        write_json(os.path.join(INDEX_DIR, name), sorted_index)

    write_index_json("division_index_en.json", div_index_en)
    write_index_json("district_index_en.json", dis_index_en)
    write_index_json("thana_index_en.json", th_index_en)
    write_index_json("suboffice_index_en.json", so_index_en)
    write_index_json("thana_index_bn.json", th_index_bn)
    write_index_json("suboffice_index_bn.json", so_index_bn)

    # Unique CSVs
    write_csv(os.path.join(UNIQUE_DIR, "unique_thanas_en.csv"), [[s] for s in sorted(unique_th_en)], ["thana_en"])
    write_csv(os.path.join(UNIQUE_DIR, "unique_thanas_bn.csv"), [[s] for s in sorted(unique_th_bn)], ["thana_bn"])
    write_csv(os.path.join(UNIQUE_DIR, "unique_suboffices_en.csv"), [[s] for s in sorted(unique_so_en)], ["suboffice_en"])
    write_csv(os.path.join(UNIQUE_DIR, "unique_suboffices_bn.csv"), [[s] for s in sorted(unique_so_bn)], ["suboffice_bn"])


def build_minified(data: Dict[str, dict]) -> None:
    # Minified JSON for production bundling
    path = os.path.join(MIN_DIR, "postcodes-pretty.min.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")


def main() -> None:
    ensure_dirs()
    data = read_data()

    # BN
    bn_json, bn_csv = build_bn(data)
    write_json(os.path.join(BN_DIR, "postcodes-bn.json"), bn_json)
    write_csv(os.path.join(BN_DIR, "postcodes-bn.csv"), bn_csv, ["postcode", "division", "district", "thana", "suboffice", "postcode_bn"])

    # EN
    en_json, en_csv = build_en(data)
    write_json(os.path.join(EN_DIR, "postcodes-en.json"), en_json)
    write_csv(os.path.join(EN_DIR, "postcodes-en.csv"), en_csv, ["postcode", "division", "district", "thana", "suboffice", "postcode_num"])

    # Ranges CSV
    write_csv(os.path.join(RANGES_DIR, "district_code_ranges.csv"), build_ranges_csv(), ["start", "end", "district"])

    # Summaries
    div_rows, dis_rows, th_rows = build_summaries(data)
    write_csv(os.path.join(SUMMARY_DIR, "counts_by_division.csv"), div_rows, ["division", "count"])
    write_csv(os.path.join(SUMMARY_DIR, "counts_by_district.csv"), dis_rows, ["district", "count"])
    write_csv(os.path.join(SUMMARY_DIR, "counts_by_thana.csv"), th_rows, ["thana", "count"])

    # Splits by division and district (combined bn+en)
    build_division_splits(data)
    build_district_splits(data)

    # Flat CSV
    build_flat_files(data)

    # Indexes and unique lists
    build_indexes_and_unique(data)

    # Minified JSON
    build_minified(data)

    print("Generated variations under 'variations' folder.")


if __name__ == "__main__":
    main()
