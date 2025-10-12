# Week 2 Learning Notes - Python Functions, Modules & Data Analysis

**Dates:** Oct 13 – Oct 19, 2025  
**Status:** In Progress  
**Focus:** Python functions, modules, file I/O, CSV data analysis

---

## 📁 Project Structure

```
week-2/
├── main.py                    # Week 2 demo & entry point
├── note.md                    # This file - learning documentation
├── src/                       # Main source code package
│   ├── __init__.py           # Package-level imports & metadata
│   ├── file_handlers/        # File I/O module (renamed from 'readers')
│   │   ├── __init__.py       # File handler module exports
│   │   ├── json_handler.py   # JSON read/write with type hints
│   │   └── csv_handler.py    # CSV read/write with DictReader
│   └── analyzers/            # Data analysis module
│       ├── __init__.py       # Analyzer module exports
│       └── csv_analyzer.py   # (TODO) Statistical analysis functions
├── tests/                    # Unit tests directory
│   ├── __init__.py           # Test package
│   ├── test_json_reader.py   # JSON functionality tests
│   └── test_csv_analyzer.py  # (TODO) CSV analyzer tests
└── data/                     # Sample data files
    ├── sample.json           # Test JSON data
    ├── sample.csv            # Employee data for analysis
    └── output/               # Generated files directory
```

---

## 🎯 Week 2 Goals & Progress

### ✅ Completed
- [x] **Refactored Week 1 code into professional module structure**
- [x] **Created proper Python packages with `__init__.py` files**
- [x] **Organized code into logical modules (readers, analyzers)**
- [x] **Set up clean import structure and namespacing**
- [x] **Migrated all functionality from Week 1 successfully**

### 🔄 In Progress
- [ ] **Build CSV summarizer (avg, min, max, median)**
- [ ] **Create main.py demo showcasing Week 2 functionality**
- [ ] **Add unit tests for new analyzer module**

### 📋 Todo
- [ ] **Practice LeetCode Easy problems in Python**
- [ ] **Explore additional Python built-in functions**
- [ ] **Add data validation and error handling to analyzer**

---

## 🏗️ Technical Architecture

### **Package Organization Philosophy**
- **`src/`** - All source code isolated from tests and data
- **`file_handlers/`** - File I/O operations (JSON, CSV) - renamed from 'readers' to better reflect bidirectional operations
- **`analyzers/`** - Data processing and statistical functions
- **`tests/`** - Comprehensive unit testing
- **`data/`** - Sample files and output directory

### **Import Strategy**
```python
# Package-level imports in src/__init__.py
from .file_handlers.json_handler import read_json_file, write_json_file
from .file_handlers.csv_handler import read_csv_as_dicts, write_csv_from_dicts

# Usage from main.py:
from src import read_csv_as_dicts, write_json_file
```

### **Module Design Principles**
- **Single Responsibility:** Each module has one clear purpose
- **Type Safety:** Modern Python type hints throughout
- **Error Handling:** Comprehensive exception handling
- **Documentation:** Clear docstrings and comments
- **Testability:** Functions designed for easy unit testing

---

## 💡 Key Learning Points

### **Python Module System**
- **`__init__.py`** files make directories into Python packages
- **Relative imports** (`.readers.json_reader`) vs absolute imports
- **`__all__`** controls what gets exported from modules
- **Namespace management** prevents naming conflicts

### **Professional Code Organization**
- **Separation of concerns** - I/O vs analysis vs testing
- **Consistent naming conventions** (snake_case for functions/files)
- **Clear directory structure** following Python best practices
- **Version control friendly** structure

### **From Week 1 to Week 2 Evolution**
```
Week 1: Individual scripts with embedded tests
Week 2: Professional package with modular architecture

Before: json_reader.py (standalone file)
After:  src/readers/json_reader.py (part of organized package)
```

---

## 📊 Sample Data Analysis

### **Employee Dataset (sample.csv)**
```csv
name,role,experience,salary,location
Abhi,Backend Developer,10,95000,Mumbai
Riya,AI Engineer,3,75000,Bangalore
John,Full Stack Developer,5,80000,Delhi
Sarah,Data Scientist,7,90000,Hyderabad
Mike,DevOps Engineer,4,70000,Pune
```

### **Analysis Goals (Mini-task)**
- **Average salary** across all employees
- **Min/Max experience** levels
- **Median salary** calculation
- **Statistics by role** or location
- **Data validation** and error handling

---

## 🧪 Testing Strategy

### **Test Organization**
- **Unit tests** for each module separately
- **Integration tests** for module interactions
- **Data validation tests** for edge cases
- **Performance tests** for large datasets

### **Test Coverage Goals**
- ✅ JSON reader/writer functions
- ✅ CSV reader/writer functions  
- 🔄 CSV analyzer statistical functions
- 🔄 Error handling scenarios
- 🔄 Edge cases (empty files, invalid data)

---

## 🚀 Next Steps

1. **Implement CSV Analyzer** 
   - Statistical functions (mean, median, mode)
   - Data filtering and grouping
   - Report generation

2. **Create main.py Demo**
   - Showcase all Week 2 functionality
   - Interactive examples with sample data
   - Professional output formatting

3. **Add Advanced Features**
   - Configuration files for analysis parameters
   - Multiple output formats (JSON, CSV, reports)
   - Data visualization preparation

4. **LeetCode Practice**
   - File I/O related problems
   - Data structure manipulation
   - Algorithm practice in Python

---

## 📈 Skills Developed

### **Week 1 → Week 2 Growth**
- **Basic Python** → **Professional Python architecture**
- **Individual functions** → **Modular package design**
- **Simple I/O** → **Comprehensive data processing**
- **Basic testing** → **Professional test organization**

### **New Concepts Mastered**
- Python package structure and imports
- Module organization best practices  
- Namespace management
- Professional code architecture
- Scalable project structure

---

*Updated: Oct 13, 2025*  
*Next Update: After CSV analyzer implementation*