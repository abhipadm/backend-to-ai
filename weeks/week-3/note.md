# Week 3 Learning Notes - Python OOP & NumPy Fundamentals

**Dates:** Feb 04 – Feb 10, 2026  
**Status:** 🔄 In Progress (75% Complete)  
**Focus:** Object-Oriented Programming, NumPy arrays, vector operations, exception handling

---

## 📁 Project Structure

```
week-3/
├── main.py                    # Week 3 demo & OOP showcase
├── note.md                    # This file - learning documentation
├── oop/                       # Object-Oriented Programming practice
│   ├── person.py             # ✅ Complete Person class with properties
│   └── context_manager_demo.py # ✅ Context manager implementation
├── numpy_demos/              # NumPy learning and exercises
│   ├── __init__.py           # NumPy package
│   └── vector_ops.py         # ✅ Complete vector operations (20 tests)
└── tests/                    # Unit tests for Week 3
    ├── __init__.py           # Test package
    └── test_vector_ops.py    # ✅ 20/20 tests passing!
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

#### **Python OOP (Person Class)**
- [x] Class definition with `__init__` constructor
- [x] InComplete Week 3 documentation**
- [ ] **Create main.py demo showcasing all learnings**


### 📋 Todo  
- [ ] **Review and practice OOP inheritance concepts** (optional deepening)
- [ ] **Explore NumPy broadcasting** (optional advanced topic)
- [ ] **Week 4 preparation: Pandas basics
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

## 🧮 NumPy Vector Operations - Complete Learning Guide

### **What Are Vectors?**

A **vector** is simply a list of numbers. In ML/AI, vectors represent:
- **Features** of data (e.g., [height, weight, age])
- **Word embeddings** (e.g., "king" → [0.2, 0.5, -0.3, ...])
- **Model weights** and parameters
- **Data points** in space

```python
# Example: A person's features
person = np.array([175, 70, 30])  # height(cm), weight(kg), age
# This is a 3-dimensional vector
```

### **Why NumPy Instead of Python Lists?**

```python
# Python list (slow) - requires loop
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [list1[i] + list2[i] for i in range(len(list1))]

# NumPy (fast, vectorized) - no loop!
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
result = v1 + v2  # 10-100x faster! ⚡
```

**NumPy is 10-100x faster** because it's written in C and uses vectorized operations.

---

### **Vector Operations & Their ML Applications**

#### **1. Vector Addition** (`v1 + v2`)
```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = [5, 7, 9]  # Element-wise: [1+4, 2+5, 3+6]
```
**ML Use:** Combining features, updating model weights

#### **2. Vector Subtraction** (`v1 - v2`)
```python
v1 = [5, 7, 9]
v2 = [1, 2, 3]
result = [4, 5, 6]  # Difference between data points
```
**ML Use:** Calculating errors, finding differences

#### **3. Scalar Multiplication** (`vector * scalar`)
```python
v = [1, 2, 3]
result = [3, 6, 9]  # Scale entire vector
```
**ML Use:** Learning rate adjustment, scaling features

#### **4. Dot Product** ⭐ (Most Important!)
```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = 1*4 + 2*5 + 3*6 = 32  # Multiply corresponding elements and sum
```

**Why it matters:**
- **Similarity measure**: High dot product = vectors point in similar direction
- **Neural networks**: Every neuron computes dot products!
- **Predictions**: `output = weights · input`

**Example in Neural Networks:**
```python
weights = [0.5, 0.3, 0.2]  # Model weights
inputs = [10, 20, 30]       # Your data
prediction = np.dot(weights, inputs)  # = 17 (this is what neurons do!)
```

#### **5. Magnitude (Length of Vector)**
```python
v = [3, 4]
magnitude = √(3² + 4²) = 5
```
**ML Use:** Distance measurement, normalization, understanding vector "strength"

#### **6. Normalization** (Make magnitude = 1)
```python
v = [3, 4]
magnitude = 5
normalized = [3/5, 4/5] = [0.6, 0.8]  # Now length = 1
```
**Why it matters:**
- **Put all features on same scale** (age vs salary vs height)
- **Required for many ML algorithms**
- **Word embeddings are normalized**

**Example:**
```python
# Before normalization
person1 = [175, 70000]  # height(cm), salary($) - salary dominates!

# After normalization - both features equally important
person1_norm = normalize(person1)  # Fair comparison
```

#### **7. Cosine Similarity** ⭐ (Measures angle between vectors)
```python
v1 = [1, 2, 3]
v2 = [2, 4, 6]  # Same direction as v1
cosine_sim = dot(v1, v2) / (magnitude(v1) * magnitude(v2))
            = 1.0  # Perfectly similar!
```

**Returns:** -1 (opposite) to +1 (identical)

**Why it matters:**
- **Text similarity**: "king" vs "queen"
- **Recommendation systems**: Similar users/products
- **Duplicate detection**

**Real Example:**
```python
# Word embeddings
king = [0.5, 0.8, 0.2]
queen = [0.6, 0.7, 0.3]  # Similar to king
car = [-0.3, 0.1, -0.5]  # Different

cosine_similarity(king, queen)  # ≈ 0.95 (very similar!)
cosine_similarity(king, car)    # ≈ 0.10 (not similar)
```

#### **8. Euclidean Distance** (Distance between points)
```python
point1 = [0, 0]
point2 = [3, 4]
distance = √((3-0)² + (4-0)²) = 5
```
**ML Use:** K-Nearest Neighbors (KNN), clustering (K-means), anomaly detection

**Example - KNN:**
```python
# Find closest customer to recommend similar products
new_customer = [25, 50000]  # age, income
customer1 = [24, 48000]  # distance = close → recommend what they like!
customer2 = [60, 100000]  # distance = far
```

#### **9. Element-wise Multiply** (Hadamard Product)
```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = [1*4, 2*5, 3*6] = [4, 10, 18]  # Different from dot product!
```
**ML Use:** Feature gating in neural networks, attention mechanisms, masking

#### **10. Mean Vector**
```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]
v3 = [7, 8, 9]
mean = [4, 5, 6]  # Average of each position
```
**ML Use:** Finding centroids in clustering, averaging embeddings

#### **11. Vector Statistics**
```python
v = [1, 2, 3, 4, 5]
stats = {
    'mean': 3.0,      # Average
    'median': 3.0,    # Middle value
    'std': 1.41,      # How spread out
    'min': 1, 'max': 5
}
```
**ML Use:** Understanding data distribution, feature analysis

---

### **How This Connects to AI/ML**

#### **Neural Network Example:**
```python
# Simple neuron computation
inputs = np.array([1.0, 2.0, 3.0])     # Your data
weights = np.array([0.5, 0.3, 0.2])    # Learned parameters
bias = 0.1

# This is what EVERY neuron does:
output = np.dot(inputs, weights) + bias  # Dot product!
# = 1.0*0.5 + 2.0*0.3 + 3.0*0.2 + 0.1 = 1.8
```

#### **Text Similarity Example:**
```python
# Word embeddings (simplified)
doc1 = np.array([0.5, 0.8, 0.2])   # "machine learning"
doc2 = np.array([0.6, 0.7, 0.3])   # "artificial intelligence"  
doc3 = np.array([-0.3, 0.1, -0.5]) # "cooking recipes"

# Find similar documents
sim = cosine_similarity(doc1, doc2)  # High similarity!
# This is how search engines work!
```

---

### **Real-World Applications**

| Operation | AI/ML Application |
|-----------|-------------------|
| **Dot Product** | Neural network layers, predictions |
| **Cosine Similarity** | Recommendation systems, text search, RAG |
| **Euclidean Distance** | KNN, clustering, anomaly detection |
| **Normalization** | Feature scaling, embeddings |
| **Magnitude** | Regularization, vector strength |

---

### **Key Takeaways** 🎯

1. **Vectors = Data** in ML (everything becomes numbers)
2. **Dot product = similarity/prediction** (most used operation)
3. **Cosine similarity** finds similar items (text, embeddings)
4. **Distance** measures how far apart things are
5. **Normalization** puts everything on same scale

**When you see:**
- "Neural network" → Think: lots of dot products
- "Embeddings" → Think: vectors representing words/images
- "Similarity" → Think: cosine similarity or distance
- "Features" → Think: vectors of numbers

---

## 🏗️ Technical Architecture

### **OOP Design Principles**
- **Encapsulation:** Hide internal implementation details
- **Inheritance:** Reuse code through parent-child relationships
- **Polymorphism:** Same interface, different implementations
- **Abstraction:** Simplify complex systems with clear interfaces

### **Professional Code Structure**
```python
class VectorOperations:
    """
    Professional structure:
    - Static methods (no instance needed)
    - Type hints (clear expectations)
    - Comprehensive docstrings
    - Error handling
    """
    
    @staticmethod
    def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
        # Check dimensions match
        if v1.shape != v2.shape:
            raise ValueError("Dimensions must match")
        return np.dot(v1, v2)
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

## � Object-Oriented Programming Fundamentals

### **1. Classes and Objects**

#### **Python Implementation**
```python
class Person:
    # Class attribute (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
        self._private_id = id(self)  # Convention: _ for "private"
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    @property
    def private_id(self):
        return self._private_id

# Usage
person1 = Person("Alice", 25)
person2 = Person.from_birth_year("Bob", 1990)
print(person1.introduce())  # "Hi, I'm Alice, 25 years old"
print(Person.is_adult(16))  # False
```

#### **.NET (C#) Comparison**
```csharp
public class Person 
{
    // Static field (shared by all instances)
    public static string Species = "Homo sapiens";
    
    // Instance fields
    public string Name { get; set; }
    public int Age { get; set; }
    private int _privateId;
    
    // Constructor
    public Person(string name, int age) 
    {
        Name = name;
        Age = age;
        _privateId = GetHashCode();
    }
    
    // Instance method
    public string Introduce() 
    {
        return $"Hi, I'm {Name}, {Age} years old";
    }
    
    // Static method
    public static bool IsAdult(int age) 
    {
        return age >= 18;
    }
    
    // Property
    public int PrivateId => _privateId;
}
```

**Key Differences:**
- **Python**: `self` parameter, `@property` decorator
- **.NET**: `this` implicit, automatic properties
- **Python**: Duck typing, dynamic
- **.NET**: Strong typing, compile-time checking

### **2. Constructors and Destructors**

#### **Python Constructor (`__init__`)**
```python
class DatabaseConnection:
    def __init__(self, host, database, user=None):
        self.host = host
        self.database = database
        self.user = user or "default_user"
        self.connection = None
        print(f"🔌 DB Connection object created for {database}")
        self._connect()
    
    def _connect(self):
        # Simulate connection
        self.connection = f"Connected to {self.host}/{self.database}"
        print(f"✅ Connected to database")

# Multiple ways to initialize
db1 = DatabaseConnection("localhost", "myapp")
db2 = DatabaseConnection("remote.com", "prod", "admin")
```

#### **Python Destructor (`__del__`) - Rarely Used**
```python
class ResourceManager:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.resource = f"Resource: {resource_name}"
        print(f"🚀 {resource_name} acquired")
    
    def __del__(self):
        print(f"💀 {self.resource_name} released")
        # DON'T rely on this for critical cleanup!

# Example
resource = ResourceManager("File Handle")
del resource  # Forces destructor call
```

#### **.NET Constructor/Destructor**
```csharp
public class DatabaseConnection 
{
    private string host;
    private string database;
    private string connection;
    
    // Constructor
    public DatabaseConnection(string host, string database, string user = "default_user") 
    {
        this.host = host;
        this.database = database;
        Console.WriteLine($"🔌 DB Connection created for {database}");
        Connect();
    }
    
    // Finalizer/Destructor
    ~DatabaseConnection() 
    {
        Console.WriteLine("💀 DB Connection finalized");
        Disconnect();
    }
    
    // IDisposable for deterministic cleanup
    public void Dispose() 
    {
        Console.WriteLine("🔧 DB Connection disposed");
        Disconnect();
        GC.SuppressFinalize(this);
    }
}
```

**Key Differences:**
- **Python**: Only one `__init__`, use default parameters
- **.NET**: Multiple constructors, constructor chaining
- **Python**: `__del__` unreliable timing
- **.NET**: Finalizer + IDisposable pattern

### **2.5. Method Types: self vs cls vs static**

#### **Understanding `self`, `cls`, and `@staticmethod`**

| Parameter | What it refers to | When used | Access to |
|-----------|------------------|-----------|-----------|
| **`self`** | Current **instance** | Instance methods | Instance & class variables |
| **`cls`** | The **class** itself | Class methods (`@classmethod`) | Class variables only |
| **None** | No reference | Static methods (`@staticmethod`) | No class/instance access |

#### **Python Method Types Examples**
```python
from datetime import date

class Person:
    total_people = 0  # Class variable
    species = "Homo sapiens"
    
    def __init__(self, name: str, age: int):
        self.name = name  # Instance variable
        self.age = age
        Person.total_people += 1
    
    # Instance method - uses self
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    # Class method - uses cls
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        """Alternative constructor using birth year"""
        age = date.today().year - birth_year
        return cls(name, age)  # cls() creates new instance
    
    @classmethod
    def get_population(cls):
        """Access class variables"""
        return cls.total_people
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static method - no self or cls
    @staticmethod
    def is_adult(age: int) -> bool:
        """Utility function - doesn't need class or instance"""
        return age >= 18
    
    @staticmethod
    def calculate_age_from_birth_year(birth_year: int) -> int:
        return date.today().year - birth_year

# Usage Examples
person1 = Person("Alice", 25)                    # Regular constructor
person2 = Person.from_birth_year("Bob", 1995)    # Class method constructor

print(person1.introduce())           # Instance method
print(Person.get_population())       # Class method - 2
print(Person.is_adult(16))          # Static method - False
print(Person.calculate_age_from_birth_year(1990))  # Static method - 35
```

#### **Why Use `cls` Instead of Class Name?**

**1. Inheritance Flexibility:**
```python
class Animal:
    @classmethod
    def create_baby(cls, name):
        print(f"Creating {cls.__name__} baby")
        return cls(name)  # Works with any subclass!

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.species = "Dog"

class Cat(Animal):
    def __init__(self, name):
        self.name = name  
        self.species = "Cat"

# cls automatically uses the correct subclass
puppy = Dog.create_baby("Rex")     # Creates Dog instance - "Creating Dog baby"
kitten = Cat.create_baby("Fluffy") # Creates Cat instance - "Creating Cat baby"

print(type(puppy).__name__)   # Dog
print(type(kitten).__name__)  # Cat
```

**2. Class Variable Management:**
```python
class Counter:
    count = 0  # Class variable shared by all instances
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1  # or cls.count += 1 in class method
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def reset_count(cls):
        cls.count = 0
    
    @classmethod
    def create_batch(cls, names: list):
        """Create multiple instances"""
        return [cls(name) for name in names]

# Usage
counters = Counter.create_batch(["A", "B", "C"])
print(Counter.get_count())  # 3
Counter.reset_count()
print(Counter.get_count())  # 0
```

#### **.NET Comparison**
```csharp
public class Person 
{
    public static int TotalPeople = 0;  // Class variable
    public string Name { get; set; }
    public int Age { get; set; }
    
    // Regular constructor
    public Person(string name, int age) 
    {
        Name = name;
        Age = age;
        TotalPeople++;
    }
    
    // Static method (like Python @staticmethod)
    public static bool IsAdult(int age) 
    {
        return age >= 18;
    }
    
    // Static factory method (like Python @classmethod)
    public static Person FromBirthYear(string name, int birthYear) 
    {
        int age = DateTime.Now.Year - birthYear;
        return new Person(name, age);  // Explicit class name
    }
    
    // Instance method
    public string Introduce() 
    {
        return $"Hi, I'm {Name}, {Age} years old";
    }
}
```

**Python vs .NET Method Comparison:**

| Python | .NET | Purpose |
|--------|------|---------|
| `def method(self):` | `public void Method()` | Instance method |
| `@classmethod def method(cls):` | `public static Type Method()` | Class/factory method |
| `@staticmethod def method():` | `public static void Method()` | Utility function |
| `cls(args)` | `new ClassName(args)` | Create instance |
| `cls.class_var` | `ClassName.StaticField` | Access class data |

#### **Key Learning Points: When to Use Each Method Type**

**🎯 Decision Tree for Method Types:**

```
Do you need access to instance data (self.name, self.age)?
├─ YES → Use Instance Method (def method(self):)
└─ NO → Do you need access to class data or create instances?
    ├─ YES → Use Class Method (@classmethod def method(cls):)
    └─ NO → Use Static Method (@staticmethod def method():)
```

**📋 Practical Guidelines:**

| Method Type | When to Use | Examples | Access |
|-------------|-------------|----------|---------|
| **Instance Method** | Need specific object data | `introduce()`, `have_birthday()` | ✅ `self.attribute` ✅ `cls.class_var` |
| **Class Method** | Alternative constructors, class operations | `from_birth_year()`, `get_population()` | ❌ No `self` ✅ `cls.class_var` |
| **Static Method** | Utility functions related to class | `is_adult()`, `validate_name()` | ❌ No `self` ❌ No `cls` |

**🚀 Real-World Use Cases:**

**Instance Methods:**
```python
def introduce(self):           # Needs self.name, self.age
def calculate_bmi(self):       # Needs self.weight, self.height
def save_to_database(self):    # Needs all instance data
```

**Class Methods:**
```python
@classmethod
def from_json(cls, json_data):        # Alternative constructor
@classmethod 
def get_all_instances(cls):           # Access class-level data
@classmethod
def create_default(cls):              # Factory method
```

**Static Methods:**
```python
@staticmethod
def validate_email(email):            # Utility - no class/instance needed
@staticmethod
def parse_date_string(date_str):      # Helper function
@staticmethod
def calculate_distance(p1, p2):      # Mathematical utility
```

**❌ Common Mistakes to Avoid:**

1. **Using `@staticmethod` when you need class data:**
   ```python
   # WRONG - can't access class variables
   @staticmethod
   def get_population():
       return PersonWithProperties.total_people  # Hard-coded class name
   
   # RIGHT - use @classmethod
   @classmethod
   def get_population(cls):
       return cls.total_people  # Flexible with inheritance
   ```

2. **Using instance method for utilities:**
   ```python
   # WRONG - doesn't need instance data
   def is_adult(self, age):
       return age >= 18
   
   # RIGHT - use @staticmethod
   @staticmethod
   def is_adult(age):
       return age >= 18
   ```

3. **Hardcoding class names in class methods:**
   ```python
   # WRONG - breaks inheritance
   @classmethod
   def create_child(cls, name):
       return Person(name, 0)  # Always creates Person
   
   # RIGHT - use cls for flexibility
   @classmethod
   def create_child(cls, name):
       return cls(name, 0)  # Creates instance of calling class
   ```

**🏆 Best Practices:**

- **Use `cls` instead of hardcoded class names** for inheritance flexibility
- **Group related static methods with the class** they belong to conceptually
- **Use class methods for alternative constructors** (factory pattern)
- **Keep static methods simple** - no complex logic requiring class context
- **Document the purpose** of each method type clearly

**💡 Memory Aid:**
- **`self`** = "I need MY data" (instance method)
- **`cls`** = "I work with OUR class" (class method)  
- **No parameter** = "I'm independent" (static method)

### **3. Context Managers (Python's Resource Management)**

#### **Manual Context Manager Implementation**
```python
class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"📂 Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"📂 Closing {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"❌ Exception in context: {exc_type.__name__}: {exc_val}")
        
        return False  # Don't suppress exceptions

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
# File automatically closed here
```

#### **Context Manager with contextlib (Simpler)**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(operation_name):
    print(f"⏱️ Starting {operation_name}")
    start_time = time.time()
    try:
        yield start_time  # This value is available in 'as' clause
    finally:
        end_time = time.time()
        print(f"⏱️ {operation_name} took {end_time - start_time:.2f} seconds")

# Usage
with timer("Data processing") as start:
    time.sleep(1)
    print(f"Operation started at {start}")
```

#### **Database Context Manager Example**
```python
class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection
        self.transaction = None
    
    def __enter__(self):
        print("🔄 Starting database transaction")
        self.transaction = self.connection.begin_transaction()
        return self.transaction
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("✅ Committing transaction")
            self.transaction.commit()
        else:
            print(f"❌ Rolling back transaction due to: {exc_val}")
            self.transaction.rollback()
        return False

# Usage
with DatabaseTransaction(db_connection) as transaction:
    # Database operations
    transaction.execute("INSERT INTO users ...")
    transaction.execute("UPDATE profiles ...")
# Transaction automatically committed or rolled back
```

#### **.NET using Statement (Similar Concept)**
```csharp
// .NET's using statement (similar to Python's with)
using (var connection = new SqlConnection(connectionString))
{
    connection.Open();
    // Use connection
} // Dispose() automatically called

// Custom IDisposable
public class TimedOperation : IDisposable 
{
    private DateTime startTime;
    private string operationName;
    
    public TimedOperation(string name) 
    {
        operationName = name;
        startTime = DateTime.Now;
        Console.WriteLine($"⏱️ Starting {name}");
    }
    
    public void Dispose() 
    {
        var elapsed = DateTime.Now - startTime;
        Console.WriteLine($"⏱️ {operationName} took {elapsed.TotalSeconds:F2} seconds");
    }
}
```

### **4. Advanced Context Manager Patterns**

#### **Multi-Resource Manager**
```python
from contextlib import ExitStack

class MultiResourceManager:
    def __init__(self):
        self.resources = []
    
    def __enter__(self):
        self.stack = ExitStack().__enter__()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.stack.__exit__(exc_type, exc_val, exc_tb)
    
    def add_resource(self, resource):
        return self.stack.enter_context(resource)

# Usage
with MultiResourceManager() as manager:
    file1 = manager.add_resource(open("file1.txt"))
    file2 = manager.add_resource(open("file2.txt"))
    db = manager.add_resource(DatabaseConnection("localhost", "mydb"))
# All resources automatically closed
```

#### **Conditional Context Manager**
```python
from contextlib import nullcontext

def get_file_context(filename, should_open=True):
    if should_open:
        return open(filename, 'w')
    else:
        return nullcontext()

# Usage - same code works whether file is opened or not
with get_file_context("output.txt", should_save=True) as f:
    if f:
        f.write("Data to save")
```

### **5. Practical Examples and Best Practices**

#### **Example: Logger with Context Management**
```python
import logging
from contextlib import contextmanager

class ApplicationLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
    
    @contextmanager
    def operation_context(self, operation_name):
        self.logger.info(f"🚀 Starting {operation_name}")
        start_time = time.time()
        try:
            yield self.logger
        except Exception as e:
            self.logger.error(f"❌ {operation_name} failed: {e}")
            raise
        else:
            elapsed = time.time() - start_time
            self.logger.info(f"✅ {operation_name} completed in {elapsed:.2f}s")

# Usage
app_logger = ApplicationLogger("MyApp")
with app_logger.operation_context("Data Processing") as logger:
    logger.info("Processing step 1")
    # Do work
    logger.info("Processing step 2")
```

**Best Practices:**
1. **Use context managers for resource management** (files, connections, locks)
2. **Prefer `contextlib.contextmanager` for simple cases**
3. **Always return `False` from `__exit__` unless you want to suppress exceptions**
4. **Use `ExitStack` for managing multiple resources**
5. **Don't rely on `__del__` for cleanup - use context managers instead**

---

## �💡 Key Learning Points

### **From Week 2 to Week 3 Evolution**
```
Week 2: Function-based programming with modules
Week 3: Object-oriented programming with data structures

Before: Functions that operate on data
After:  Objects that encapsulate data and behavior
```

### **OOP vs .NET Comparison Summary**

| Concept | Python | .NET (C#) |
|---------|--------|-----------|
| **Constructor** | `__init__(self, ...)` | `ClassName(...)` |
| **Destructor** | `__del__(self)` (unreliable) | `~ClassName()` (finalizer) |
| **Resource Cleanup** | Context managers (`with`) | `IDisposable` + `using` |
| **Access Modifiers** | Convention (`_private`) | `private`, `protected`, `public` |
| **Properties** | `@property` decorator | `{ get; set; }` syntax |
| **Static Methods** | `@staticmethod` | `static` keyword |
| **Class Methods** | `@classmethod` | Static methods with class reference |
| **Multiple Constructors** | Default parameters | Method overloading |
| **Resource Management** | `__enter__`/`__exit__` | `IDisposable.Dispose()` |

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