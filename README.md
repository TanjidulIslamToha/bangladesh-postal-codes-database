# Bangladesh Postcodes Database

A comprehensive database of Bangladesh postal codes with bilingual support (Bengali and English).

## 📁 Files

### Main Data Files
- **`postcodes-pretty.json`** - Main formatted JSON file with bilingual postcode data
- **`postcodes-english.json`** - English-only postcode data
- **`postcodes-bengali.json`** - Bengali-only postcode data

### CSV Files
- **`postcodes-english.csv`** - English postcode data in CSV format
- **`postcodes-bengali.csv`** - Bengali postcode data in CSV format

### Administrative Divisions
- **`divisions-english.json`** - English division data
- **`divisions-bengali.json`** - Bengali division data
- **`divisions-english.csv`** - English division data in CSV format
- **`divisions-bengali.csv`** - Bengali division data in CSV format

### Districts
- **`districts-english.json`** - English district data
- **`districts-bengali.json`** - Bengali district data
- **`districts-english.csv`** - English district data in CSV format
- **`districts-bengali.csv`** - Bengali district data in CSV format

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

- **Total Postcodes**: 1,353
- **Divisions**: 8
- **Districts**: 64
- **Format**: JSON and CSV
- **Encoding**: UTF-8

## 🔧 Data Quality

✅ **Verified and Cleaned**:
- All language keys consistently ordered (`bn` before `en`)
- No mixed-language entries
- No missing fields or sections
- No empty or null values
- Proper Bengali spelling throughout
- Accurate English transliterations

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

**Last Updated**: December 2024  
**Total Records**: 1,353 postcodes  
**Data Format**: JSON & CSV  
**Language Support**: Bengali & English
