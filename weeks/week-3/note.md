# Week 3 Learning Notes - Python OOP & NumPy Fundamentals

**Dates:** Oct 20 – Oct 26, 2025  
**Status:** 🚀 Ready to Start  
**Focus:** Object-Oriented Programming, NumPy arrays, vector operations, exception handling

---

## 📁 Project Structure

```
week-3/
├── main.py                    # Week 3 demo & OOP showcase
├── note.md                    # This file - learning documentation
├── oop/                       # Object-Oriented Programming practice
│   ├── __init__.py           # Package initialization
│   ├── classes_basics.py     # Class definitions and methods
│   ├── inheritance.py        # Inheritance and polymorphism  
│   ├── exceptions.py         # Custom exceptions and error handling
│   └── employee_system.py    # Complete OOP example
├── numpy_practice/           # NumPy learning and exercises
│   ├── __init__.py           # NumPy package
│   ├── arrays_basics.py      # Array creation and manipulation
│   ├── vector_operations.py  # Mathematical operations
│   ├── data_analysis.py      # Statistical operations
│   └── mini_task.py          # Week 3 mini-task implementation
├── tests/                    # Unit tests for Week 3
│   ├── __init__.py           # Test package
│   ├── test_oop_classes.py   # OOP functionality tests
│   └── test_numpy_ops.py     # NumPy operations tests
└── data/                     # Sample data for NumPy practice
    ├── sample_data.csv       # Numerical datasets
    └── vectors.json          # Vector data for operations
```

---

## 🎯 Week 3 Goals & Progress

### **🎓 Learning Objectives:**
- **Master Python OOP concepts** (classes, inheritance, polymorphism)
- **Exception handling** and custom error types
- **NumPy fundamentals** (arrays, operations, broadcasting)
- **Vector mathematics** with Python
- **Data manipulation** patterns for ML preparation

### ✅ Completed


### 🔄 In Progress


### 📋 Todo
- [ ] **Python Classes & Objects**
  - Class definition and instantiation
  - Instance methods and attributes
  - Class methods and static methods
  - Property decorators (@property)

- [ ] **Inheritance & Polymorphism**
  - Single and multiple inheritance
  - Method overriding and super()
  - Abstract base classes
  - Composition vs inheritance

- [ ] **Exception Handling**
  - Try/except/finally blocks
  - Custom exception classes
  - Exception hierarchy
  - Best practices for error handling

- [ ] **NumPy Fundamentals**
  - Array creation and indexing
  - Shape manipulation and broadcasting
  - Mathematical operations
  - Statistical functions

- [ ] **Mini-Task: Vector Operations System**
  - Vector class with OOP principles
  - NumPy-powered mathematical operations
  - Exception handling for invalid operations
  - Unit tests for all functionality
- [ ] **Advanced NumPy features**
- [ ] **Performance comparison: Python lists vs NumPy arrays**
- [ ] **Prepare for Week 4: Pandas integration**

---

## 🏗️ Technical Architecture

### **OOP Design Principles**
- **Encapsulation:** Hide internal implementation details
- **Inheritance:** Reuse code through parent-child relationships
- **Polymorphism:** Same interface, different implementations
- **Abstraction:** Simplify complex systems with clear interfaces

### **NumPy Integration Strategy**
```python
# Combining OOP with NumPy for powerful data structures
class DataAnalyzer:
    def __init__(self, data: np.ndarray):
        self._data = data
    
    def calculate_statistics(self) -> dict:
        return {
            'mean': np.mean(self._data),
            'std': np.std(self._data),
            'min': np.min(self._data),
            'max': np.max(self._data)
        }
```

### **Exception Strategy**
```python
class InvalidVectorOperation(Exception):
    """Custom exception for vector operations"""
    def __init__(self, message: str, vector_size: int):
        self.vector_size = vector_size
        super().__init__(f"Vector operation error: {message} (size: {vector_size})")
```

---

## 💡 Key Learning Points

### **From Week 2 to Week 3 Evolution**
```
Week 2: Function-based programming with modules
Week 3: Object-oriented programming with data structures

Before: Functions that operate on data
After:  Objects that encapsulate data and behavior
```

### **OOP Benefits for AI/ML**
- **Data Models:** Classes for datasets, models, pipelines
- **Reusability:** Inherit from base model classes
- **Maintainability:** Encapsulated ML components
- **Testing:** Isolated object testing

### **NumPy Advantages**
- **Performance:** C-optimized operations
- **Memory Efficiency:** Contiguous arrays
- **Broadcasting:** Automatic shape handling  
- **Vectorization:** Eliminate explicit loops

---

## 🧪 Testing Strategy

### **OOP Testing Patterns**
- **Unit tests** for individual class methods
- **Integration tests** for class interactions
- **Inheritance tests** for polymorphic behavior
- **Exception tests** for error handling

### **NumPy Testing Patterns**
- **Array equality** tests with np.testing.assert_array_equal
- **Numerical precision** tests for floating-point operations
- **Shape validation** tests for broadcasting
- **Performance benchmarks** vs pure Python

### **Test Coverage Goals**
- [ ] Class instantiation and method calls
- [ ] Inheritance and method overriding
- [ ] Exception raising and handling
- [ ] NumPy array operations and mathematical functions
- [ ] Vector operations mini-task functionality

---

## 📊 Week 3 Mini-Task: Vector Operations System

### **Objective:**
Build a comprehensive vector mathematics system combining OOP and NumPy.

### **Requirements:**
1. **Vector Class (OOP)**
   - Initialize with NumPy array
   - Vector addition, subtraction, multiplication
   - Dot product and cross product operations
   - Magnitude and normalization methods

2. **Exception Handling**
   - Custom exceptions for dimension mismatches
   - Invalid operation handling
   - Input validation with meaningful error messages

3. **NumPy Integration**
   - Leverage NumPy for all mathematical operations
   - Performance comparison with pure Python implementation
   - Broadcasting for different vector sizes where applicable

4. **Testing Suite**
   - Comprehensive unit tests
   - Edge case handling
   - Performance benchmarks

### **Example Usage:**
```python
# Create vectors
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Operations
result = v1 + v2           # Vector addition
dot_product = v1.dot(v2)   # Dot product
magnitude = v1.magnitude() # Vector magnitude
normalized = v1.normalize() # Unit vector

# Exception handling
try:
    v3 = Vector([1, 2])
    invalid_result = v1 + v3  # Different dimensions
except InvalidVectorOperation as e:
    print(f"Error: {e}")
```

---

## 🔗 Building on Week 2 Skills

### **Code Organization Evolution**
```python
# Week 2: Module-based functions
from file_handlers import read_csv_as_dicts

# Week 3: Class-based objects  
class DataProcessor:
    def __init__(self, file_handler):
        self.handler = file_handler
```

### **Error Handling Progression**
```python
# Week 2: Function-level error handling
def analyse_csv_data(data, column):
    if not data:
        return None

# Week 3: Object-level exception handling
class DataAnalyzer:
    def analyze(self, data):
        if not data:
            raise EmptyDataError("No data provided for analysis")
```

---

## 🚀 Success Metrics

### **Technical Proficiency**
- [ ] Create classes with proper encapsulation
- [ ] Implement inheritance hierarchies
- [ ] Handle exceptions gracefully
- [ ] Perform vector operations with NumPy
- [ ] Write comprehensive unit tests

### **Understanding Depth**
- [ ] Explain when to use OOP vs functional programming
- [ ] Compare NumPy performance vs pure Python
- [ ] Design exception hierarchies
- [ ] Apply SOLID principles in class design

### **Project Quality**
- [ ] Clean, documented code with type hints
- [ ] Comprehensive test coverage
- [ ] Professional error handling
- [ ] Optimized NumPy operations

---

## 📈 Skills Development Trajectory

### **Week 2 → Week 3 Growth**
- **Functions** → **Classes and Objects**
- **Module organization** → **OOP design patterns**
- **Basic error handling** → **Custom exceptions**
- **List operations** → **NumPy array operations**
- **Statistical analysis** → **Vector mathematics**

### **Preparation for Week 4**
- **NumPy arrays** → **Pandas DataFrames**
- **Vector operations** → **Data manipulation**
- **Class design** → **Data pipeline architecture**
- **Mathematical operations** → **Data visualization**

---

*Created: Oct 26, 2025*  
*Next Update: After OOP basics implementation*