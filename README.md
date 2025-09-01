# Bangladesh Postcodes Database

A comprehensive database of Bangladesh postal codes with bilingual support (Bengali and English).

## 📁 Files

### Main Data File (root)
- **`postcodes-pretty.json`** — Pretty, bilingual JSON (cleaned and validated). Keep this at the project root.

### Variations (generated)
All variations are under `variations/`.

- **`variations/bn/`**
  - `postcodes-bn.json` — Bengali-only JSON
  - `postcodes-bn.csv` — Bengali-only CSV
- **`variations/en/`**
  - `postcodes-en.json` — English-only JSON
  - `postcodes-en.csv` — English-only CSV
- **`variations/ranges/`**
  - `district_code_ranges.csv` — District code ranges (inclusive)
- **`variations/summary/`**
  - `counts_by_division.csv`
  - `counts_by_district.csv`
  - `counts_by_thana.csv`
 - **`variations/divisions/`** — One folder per division, each containing:
   - `division-<slug>.json` (combined bn+en for that division)
   - `division-<slug>.csv`
 - **`variations/districts/`** — One folder per district, each containing:
   - `district-<slug>.json` (combined bn+en for that district)
   - `district-<slug>.csv`
 - **`variations/flat/`**
   - `postcodes-flat.csv` — Whole dataset as a single CSV (bn+en columns)
 - **`variations/index/`**
   - `division_index_en.json`, `district_index_en.json`
   - `thana_index_en.json`, `suboffice_index_en.json`
   - `thana_index_bn.json`, `suboffice_index_bn.json`
 - **`variations/unique/`**
   - `unique_thanas_en.csv`, `unique_thanas_bn.csv`
   - `unique_suboffices_en.csv`, `unique_suboffices_bn.csv`
 - **`variations/min/`**
   - `postcodes-pretty.min.json` — Minified JSON

### Administrative Divisions
- (merged into main JSON; separate division files removed)

### Districts
- (merged into main JSON; separate district files removed)

## 📊 Data Structure

### Main JSON Format (`postcodes-pretty.json`)

Each postcode entry follows this structure:

```json
{
  "1236": {
    "bn": {
      "division": "ঢাকা",
      "district": "ঢাকা", 
      "thana": "যাত্রাবাড়ী",
      "suboffice": "ধানিয়া টিএসও",
      "postcode": "১২৩৬"
    },
    "en": {
      "division": "Dhaka",
      "district": "Dhaka",
      "thana": "Jatrabari",
      "suboffice": "Dhania TSO",
      "postcode": 1236
    }
  }
}
```

### Fields Description

| Field | Description |
|-------|-------------|
| `division` | Administrative division (বিভাগ) |
| `district` | District (জেলা) |
| `thana` | Police station/Upazila (থানা/উপজেলা) |
| `suboffice` | Sub post office (উপ-ডাকঘর) |
| `postcode` | Postal code (পোস্ট কোড) |

## 🌍 Language Support

- **Bengali (`bn`)**: Full Bengali text with proper spelling
- **English (`en`)**: Full English text with correct transliteration

## 📈 Statistics

- **Total Postcodes**: 1,347
- **Divisions**: 8
- **Districts**: 64
- **Format**: JSON and CSV
- **Encoding**: UTF-8

## 🔧 Data Quality

✅ **Verified and Cleaned**:
- All `bn` fields aligned to the official Wikipedia listing (script-verified)
- English `district` aligned to authoritative postal code ranges provided
- Consistent key ordering (`bn` then `en`), UTF-8, no null/empty fields
- Correct Bengali spellings and English transliterations

## 📋 Usage Examples

### JavaScript/Node.js
```javascript
const fs = require('fs');
const postcodes = JSON.parse(fs.readFileSync('postcodes-pretty.json', 'utf8'));

// Get postcode data
const postcode1236 = postcodes['1236'];
console.log(postcode1236.bn.division); // "ঢাকা"
console.log(postcode1236.en.district); // "Dhaka"
```

### Python
```python
import json

with open('postcodes-pretty.json', 'r', encoding='utf-8') as f:
    postcodes = json.load(f)

# Get postcode data
postcode_1236 = postcodes['1236']
print(postcode_1236['bn']['division'])  # "ঢাকা"
print(postcode_1236['en']['district'])  # "Dhaka"
```

### PHP
```php
$postcodes = json_decode(file_get_contents('postcodes-pretty.json'), true);

// Get postcode data
$postcode_1236 = $postcodes['1236'];
echo $postcode_1236['bn']['division']; // "ঢাকা"
echo $postcode_1236['en']['district']; // "Dhaka"
```

## 🗺️ Administrative Structure

### Divisions (বিভাগ)
1. **ঢাকা** (Dhaka)
2. **চট্টগ্রাম** (Chittagong)
3. **রাজশাহী** (Rajshahi)
4. **খুলনা** (Khulna)
5. **বরিশাল** (Barisal)
6. **সিলেট** (Sylhet)
7. **রংপুর** (Rangpur)
8. **ময়মনসিংহ** (Mymensingh)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Data accuracy and consistency
- Proper Bengali spelling
- Correct English transliterations
- UTF-8 encoding for all files

## 📞 Support

For questions or issues, please open an issue on the project repository.

## 🔄 Updates

This database is regularly updated to maintain accuracy and completeness of Bangladesh postal information.

---

**Last Updated**: September 2025  
**Total Records**: 1,347 postcodes  
**Data Format**: JSON  
**Language Support**: Bengali & English

## 📚 Sources
- Wikipedia: Bangladesh postal codes (Bengali listing) — used to verify all bn fields
- District code ranges (user-provided reference) — used to align en.district to ranges

## 🔄 Generate Variations
To regenerate the variations after any change to `postcodes-pretty.json`:

```bash
python generate_variations.py
```

Outputs will be placed under the `variations/` folder as documented above.
