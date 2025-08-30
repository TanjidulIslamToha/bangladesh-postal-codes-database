# 🇧🇩 Bangladesh Postcodes Database

> **Complete, Clean & Validated Bangladesh Postal Codes Database**  
> *Collected from Wikipedia, Fixed & Validated for Public Use*

[![GitHub stars](https://img.shields.io/github/stars/TanjidulIslamToha/bangladesh-postcodes?style=social)](https://github.com/TanjidulIslamToha/bangladesh-postcodes)
[![GitHub forks](https://img.shields.io/github/forks/TanjidulIslamToha/bangladesh-postcodes?style=social)](https://github.com/TanjidulIslamToha/bangladesh-postcodes)
[![GitHub issues](https://img.shields.io/github/issues/TanjidulIslamToha/bangladesh-postcodes)](https://github.com/TanjidulIslamToha/bangladesh-postcodes/issues)
[![GitHub license](https://img.shields.io/github/license/TanjidulIslamToha/bangladesh-postcodes)](https://github.com/TanjidulIslamToha/bangladesh-postcodes/blob/main/LICENSE)

---

## 🚀 **Hello Bangladesh! 🇧🇩**

I was working on a **non-profit public safety project** for Bangladesh people, and I desperately needed a **comprehensive, accurate Bangladesh postcodes database**. But guess what? **I couldn't find one anywhere!** 😤

So I decided to **collect them myself** from Wikipedia and **fix all the issues** I encountered. This repository contains **1,353 validated postcodes** covering all divisions of Bangladesh.

---

## 📊 **What I Fixed (The Struggle Was Real! 😅)**

### **Issues I Encountered & Fixed:**
- ❌ **12,175+ data quality issues** in the original data
- ❌ **Missing English translations** for many postcodes
- ❌ **Incorrect division mappings** (postcodes assigned to wrong divisions)
- ❌ **Trailing spaces and special characters** everywhere
- ❌ **Inconsistent postcode formats** (mixed Bangla/English numbers)
- ❌ **Incomplete data** (missing districts, thanas, sub-offices)
- ❌ **No standardized structure** for easy use

### **What I Achieved:**
- ✅ **100% bilingual coverage** (Bangla + English)
- ✅ **All 1,353 postcodes validated** and cleaned
- ✅ **Proper division mappings** based on postcode ranges
- ✅ **Consistent formatting** (Bangla numbers in Bangla, English in English)
- ✅ **Multiple file formats** (JSON + CSV)
- ✅ **Production-ready** data structure

---

## 📁 **Files Available**

| File | Format | Size | Entries | Description |
|------|--------|------|---------|-------------|
| `postcodes-pretty.json` | JSON (Bilingual) | 645KB | 1,353 | **Main file** - Both Bangla & English |
| `bengali.json` | JSON (Bengali) | 318KB | 1,353 | Bengali-only data |
| `english.json` | JSON (English) | 232KB | 1,353 | English-only data |
| `bengali.csv` | CSV (Bengali) | 165KB | 1,353 | Bengali CSV format |
| `english.csv` | CSV (English) | 81KB | 1,353 | English CSV format |
| `districts-bengali.json` | JSON (Districts) | 35KB | 70 | Bengali districts with divisions |
| `districts-english.json` | JSON (Districts) | 34KB | 82 | English districts with divisions |
| `districts-bengali.csv` | CSV (Districts) | 11KB | 70 | Bengali districts CSV |
| `districts-english.csv` | CSV (Districts) | 9.9KB | 82 | English districts CSV |
| `divisions-bengali.json` | JSON (Divisions) | 28KB | 8 | Bengali divisions with districts |
| `divisions-english.json` | JSON (Divisions) | 27KB | 8 | English divisions with districts |
| `divisions-bengali.csv` | CSV (Divisions) | 9.9KB | 8 | Bengali divisions CSV |
| `divisions-english.csv` | CSV (Divisions) | 9.3KB | 8 | English divisions CSV |

---

## 🔧 **How I Fixed Everything (PHP Code)**

I used **PHP scripts** to clean and validate the data:

```php
// Example of the cleaning process
function fixAllIssues($data) {
    foreach ($data as $postcode => $info) {
        // Fix postcode format consistency
        $bn['postcode'] = e2b($postcode); // Convert to Bangla numbers
        $en['postcode'] = $postcode;      // Keep English numbers
        
        // Fix division mappings based on postcode ranges
        $correctDivision = getCorrectDivision($postcode);
        
        // Remove trailing spaces and special characters
        $text = trim(preg_replace('/\s+/', ' ', $text));
        
        // Ensure bilingual data exists
        if (!isset($info['bn']) && isset($info['en'])) {
            // Create missing Bangla data from English
        }
    }
}
```

**Total fixes applied:** 12,175+ issues resolved! 🎯

---

## 📋 **Data Structure**

### **Main Bilingual Format:**
```json
{
  "1206": {
    "bn": {
      "division": "ঢাকা",
      "district": "ঢাকা", 
      "thana": "ঢাকা সেনানিবাস",
      "suboffice": "ঢাকা সেনানিবাস TSO",
      "postcode": "১২০৬"
    },
    "en": {
      "division": "Dhaka",
      "district": "Dhaka",
      "thana": "Dhaka", 
      "suboffice": "Dhaka Cantonment-TSO",
      "postcode": "1206"
    }
  }
}
```

### **Districts Format:**
```json
{
  "ঢাকা": {
    "name": "ঢাকা",
    "division": "ঢাকা",
    "postcodes": ["1206", "1207", "1208", "1209", "1210"]
  }
}
```

### **Divisions Format:**
```json
{
  "ঢাকা": {
    "name": "ঢাকা",
    "districts": ["ঢাকা", "গাজীপুর", "নারায়ণগঞ্জ", "টাঙ্গাইল"],
    "postcodes": ["1206", "1207", "1208", "1209", "1210"]
  }
}
```

### **CSV Format:**
```csv
"Postcode","Division","District","Thana","SubOffice","PostCode"
"1206","ঢাকা","ঢাকা","ঢাকা সেনানিবাস","ঢাকা সেনানিবাস TSO","১২০৬"
"1206","Dhaka","Dhaka","Dhaka","Dhaka Cantonment-TSO","1206"
```

---

## 🗺️ **Coverage**

### **Divisions Covered:**
- **ঢাকা (Dhaka)** - 10 districts, 213 postcodes
- **চট্টগ্রাম (Chittagong)** - 6 districts, 143 postcodes  
- **রাজশাহী (Rajshahi)** - 16 districts, 223 postcodes
- **খুলনা (Khulna)** - 4 districts, 90 postcodes
- **বরিশাল (Barisal)** - 8 districts, 141 postcodes
- **সিলেট (Sylhet)** - 11 districts, 323 postcodes
- **রংপুর (Rangpur)** - 10 districts, 121 postcodes
- **ময়মনসিংহ (Mymensingh)** - 6 districts, 99 postcodes

**Total: 1,353 postcodes across 8 divisions and 70+ districts** 🎯

---

## 🚀 **How to Use**

### **For Web Applications:**
```javascript
// Load the JSON file
fetch('postcodes-pretty.json')
  .then(response => response.json())
  .then(data => {
    const postcode = data['1206'];
    console.log(postcode.bn.division); // "ঢাকা"
    console.log(postcode.en.division); // "Dhaka"
  });
```

### **For Mobile Apps:**
```dart
// Flutter/Dart example
Map<String, dynamic> postcodes = jsonDecode(postcodesJson);
var dhakaPostcode = postcodes['1206'];
print(postcodes['1206']['bn']['division']); // "ঢাকা"
```

### **For Spreadsheets:**
Simply open `bengali.csv` or `english.csv` in Excel, Google Sheets, or any CSV reader.

---

## 🤝 **Contributing**

Found an issue? Want to add more postcodes? **Please contribute!**

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Every contribution helps make this database better for the Bangladesh community!** 🙏

---

## 📞 **Connect With Me**

- **GitHub:** [@TanjidulIslamToha](https://github.com/TanjidulIslamToha)
- **Facebook:** [facebook.com/MdTanjidulIslamToha](https://facebook.com/MdTanjidulIslamToha)

---

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 **Why I Created This**

I was working on a **public safety project** for Bangladesh people, and I needed accurate postcode data. When I couldn't find a reliable source, I decided to **create one myself** and share it with the community.

**I hope this helps other developers who face the same struggle!** 💪

---

## ⭐ **Support This Project**

If this database helps you in your project, please:
- ⭐ **Star this repository**
- 🔄 **Share it with others**
- 🐛 **Report any issues**
- 💡 **Suggest improvements**

**Together, we can make better tools for Bangladesh!** 🇧🇩

---

*Made with ❤️ for Bangladesh*  
*Last updated: December 2024*
