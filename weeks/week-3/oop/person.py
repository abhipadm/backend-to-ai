
from datetime import date


class Person:

    # Constructor - runs when creating a new person
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    # Method to introduce the person
    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    # Method to celebrate birthday
    def have_birthday(self) -> str:
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."


class PersonWithProperties:
    # Class variable to track total people created
    total_people = 0
    species = "Homo sapiens"
    
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        # Increment class variable when new person is created
        PersonWithProperties.total_people += 1

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if new_name:
            self._name = new_name
        else:
            raise ValueError("Name cannot be empty")

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative")
        
    @property
    def birth_year(self) -> int:
        current_year = date.today().year
        return current_year - self._age
    
    # Instance method
    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def have_birthday(self) -> str:
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."
    
    # CLASS METHODS - use @classmethod decorator
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        """Alternative constructor - create Person from birth year"""
        age = date.today().year - birth_year
        return cls(name, age)  # cls() creates new instance of the class
    
    @classmethod
    def from_string(cls, person_string: str):
        """Create person from string format 'Name,Age'"""
        try:
            name, age_str = person_string.split(',')
            return cls(name.strip(), int(age_str.strip()))
        except ValueError:
            raise ValueError("Invalid format. Use 'Name,Age' format")
    
    @classmethod
    def get_population(cls) -> int:
        """Get total number of people created"""
        return cls.total_people
    
    @classmethod
    def get_species(cls) -> str:
        """Get species information"""
        return cls.species
    
    @classmethod
    def create_batch(cls, people_data: list):
        """Create multiple people from list of tuples [(name, age), ...]"""
        return [cls(name, age) for name, age in people_data]
    
    # STATIC METHODS - use @staticmethod decorator
    @staticmethod
    def is_adult(age: int) -> bool:
        """Check if age qualifies as adult (utility function)"""
        return age >= 18
    
    @staticmethod
    def is_senior(age: int) -> bool:
        """Check if age qualifies as senior citizen"""
        return age >= 65
    
    @staticmethod
    def calculate_age_from_birth_year(birth_year: int) -> int:
        """Calculate current age from birth year"""
        return date.today().year - birth_year
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate if name meets requirements"""
        return bool(name and name.strip() and len(name.strip()) >= 2)



if __name__ == "__main__":
    print("testing class person")
    # Create objects (instances)
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    # Use the methods
    print(person1.introduce())
    print(person2.introduce())
    print(person1.have_birthday())

    # Testing PersonWithProperties
    print("\n" + "="*50)
    print("TESTING PersonWithProperties with Decorators")
    print("="*50)
    
    # Regular constructor
    person3 = PersonWithProperties("Charlie", 28)
    print(f"Person 3: {person3.introduce()}")
    print(f"Birth Year: {person3.birth_year}")
    
    # Test property validation
    try:
        person3.age = -5  # This should raise an error
    except ValueError as ve:
        print(f"❌ Age validation error: {ve}")  
    
    try:
        person3.name = ""  # This should raise an error
    except ValueError as ve:
        print(f"❌ Name validation error: {ve}")
    
    print(f"\n📊 Population after person3: {PersonWithProperties.get_population()}")
    
    # CLASS METHODS TESTING
    print("\n🏭 Testing @classmethod decorators:")
    
    # Alternative constructor from birth year
    person4 = PersonWithProperties.from_birth_year("Diana", 1995)
    print(f"Person 4 (from birth year): {person4.introduce()}")
    
    # Create from string
    person5 = PersonWithProperties.from_string("Edward, 35")
    print(f"Person 5 (from string): {person5.introduce()}")
    
    # Batch creation
    people_data = [("Frank", 40), ("Grace", 22), ("Henry", 55)]
    batch_people = PersonWithProperties.create_batch(people_data)
    print(f"Batch created: {len(batch_people)} people")
    for person in batch_people:
        print(f"  - {person.introduce()}")
    
    # Class information
    print(f"\n🌍 Species: {PersonWithProperties.get_species()}")
    print(f"📊 Total population: {PersonWithProperties.get_population()}")
    
    # STATIC METHODS TESTING
    print("\n🔧 Testing @staticmethod decorators:")
    ages_to_test = [15, 18, 25, 65, 80]
    
    for age in ages_to_test:
        adult = PersonWithProperties.is_adult(age)
        senior = PersonWithProperties.is_senior(age)
        print(f"Age {age}: Adult={adult}, Senior={senior}")
    
    # Utility functions
    calculated_age = PersonWithProperties.calculate_age_from_birth_year(1990)
    print(f"\nCalculated age for 1990 birth year: {calculated_age}")
    
    # Name validation
    test_names = ["John", "A", "", "  ", "Mary Jane"]
    for name in test_names:
        valid = PersonWithProperties.validate_name(name)
        print(f"Name '{name}': Valid={valid}")
    
    print(f"\n🎉 Final population count: {PersonWithProperties.get_population()}")
