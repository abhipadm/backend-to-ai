"""
NumPy Vector Operations - Week 3 Mini-Task
Demonstrates vector mathematics using NumPy for ML/AI foundations
"""

import numpy as np
from typing import Union, Tuple


class VectorOperations:
    """
    A class implementing various vector operations using NumPy.
    Essential for understanding ML algorithms that work with vectors.
    """
    
    @staticmethod
    def create_vector(elements: list) -> np.ndarray:
        """
        Create a NumPy vector from a list of numbers.
        
        Args:
            elements: List of numbers
            
        Returns:
            NumPy array (vector)
            
        Example:
            >>> v = VectorOperations.create_vector([1, 2, 3])
            >>> print(v)
            [1 2 3]
        """
        return np.array(elements)
    
    @staticmethod
    def vector_add(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        """
        Add two vectors element-wise.
        
        Args:
            v1: First vector
            v2: Second vector
            
        Returns:
            Sum of vectors
            
        Raises:
            ValueError: If vectors have different dimensions
            
        Example:
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([4, 5, 6])
            >>> result = VectorOperations.vector_add(v1, v2)
            >>> print(result)
            [5 7 9]
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        return v1 + v2
    
    @staticmethod
    def vector_subtract(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        """
        Subtract v2 from v1 element-wise.
        
        Args:
            v1: First vector
            v2: Second vector
            
        Returns:
            Difference of vectors (v1 - v2)
            
        Example:
            >>> v1 = np.array([5, 7, 9])
            >>> v2 = np.array([1, 2, 3])
            >>> result = VectorOperations.vector_subtract(v1, v2)
            >>> print(result)
            [4 5 6]
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        return v1 - v2
    
    @staticmethod
    def scalar_multiply(vector: np.ndarray, scalar: Union[int, float]) -> np.ndarray:
        """
        Multiply vector by a scalar (number).
        
        Args:
            vector: Input vector
            scalar: Number to multiply by
            
        Returns:
            Scaled vector
            
        Example:
            >>> v = np.array([1, 2, 3])
            >>> result = VectorOperations.scalar_multiply(v, 3)
            >>> print(result)
            [3 6 9]
        """
        return vector * scalar
    
    @staticmethod
    def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
        """
        Calculate dot product of two vectors.
        Critical for ML: measures similarity between vectors.
        
        Args:
            v1: First vector
            v2: Second vector
            
        Returns:
            Dot product (scalar value)
            
        Example:
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([4, 5, 6])
            >>> result = VectorOperations.dot_product(v1, v2)
            >>> print(result)
            32  # (1*4 + 2*5 + 3*6)
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        return np.dot(v1, v2)
    
    @staticmethod
    def magnitude(vector: np.ndarray) -> float:
        """
        Calculate the magnitude (length) of a vector.
        Also called L2 norm or Euclidean norm.
        
        Args:
            vector: Input vector
            
        Returns:
            Magnitude of the vector
            
        Example:
            >>> v = np.array([3, 4])
            >>> result = VectorOperations.magnitude(v)
            >>> print(result)
            5.0  # sqrt(3^2 + 4^2)
        """
        return np.linalg.norm(vector)
    
    @staticmethod
    def normalize(vector: np.ndarray) -> np.ndarray:
        """
        Normalize a vector to unit length (magnitude = 1).
        Essential for ML: puts all vectors on same scale.
        
        Args:
            vector: Input vector
            
        Returns:
            Normalized vector (unit vector)
            
        Raises:
            ValueError: If vector has zero magnitude
            
        Example:
            >>> v = np.array([3, 4])
            >>> result = VectorOperations.normalize(v)
            >>> print(result)
            [0.6 0.8]  # [3/5, 4/5]
        """
        mag = VectorOperations.magnitude(vector)
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return vector / mag
    
    @staticmethod
    def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
        """
        Calculate cosine similarity between two vectors.
        Very important in ML/NLP: measures how similar two vectors are.
        Returns value between -1 (opposite) and 1 (identical).
        
        Args:
            v1: First vector
            v2: Second vector
            
        Returns:
            Cosine similarity (-1 to 1)
            
        Example:
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([2, 4, 6])  # Same direction
            >>> result = VectorOperations.cosine_similarity(v1, v2)
            >>> print(result)
            1.0  # Perfectly similar
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        
        dot_prod = np.dot(v1, v2)
        mag_v1 = VectorOperations.magnitude(v1)
        mag_v2 = VectorOperations.magnitude(v2)
        
        if mag_v1 == 0 or mag_v2 == 0:
            raise ValueError("Cannot calculate cosine similarity with zero vector")
        
        return dot_prod / (mag_v1 * mag_v2)
    
    @staticmethod
    def element_wise_multiply(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        """
        Multiply vectors element-wise (Hadamard product).
        Different from dot product!
        
        Args:
            v1: First vector
            v2: Second vector
            
        Returns:
            Element-wise product
            
        Example:
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([4, 5, 6])
            >>> result = VectorOperations.element_wise_multiply(v1, v2)
            >>> print(result)
            [4 10 18]  # [1*4, 2*5, 3*6]
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        return v1 * v2
    
    @staticmethod
    def euclidean_distance(v1: np.ndarray, v2: np.ndarray) -> float:
        """
        Calculate Euclidean distance between two vectors.
        Used in clustering, KNN, and many ML algorithms.
        
        Args:
            v1: First vector (point)
            v2: Second vector (point)
            
        Returns:
            Euclidean distance
            
        Example:
            >>> v1 = np.array([0, 0])
            >>> v2 = np.array([3, 4])
            >>> result = VectorOperations.euclidean_distance(v1, v2)
            >>> print(result)
            5.0  # sqrt((3-0)^2 + (4-0)^2)
        """
        if v1.shape != v2.shape:
            raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
        return np.linalg.norm(v1 - v2)
    
    @staticmethod
    def mean_vector(vectors: list) -> np.ndarray:
        """
        Calculate the mean (average) of multiple vectors.
        
        Args:
            vectors: List of NumPy arrays
            
        Returns:
            Mean vector
            
        Example:
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([4, 5, 6])
            >>> v3 = np.array([7, 8, 9])
            >>> result = VectorOperations.mean_vector([v1, v2, v3])
            >>> print(result)
            [4. 5. 6.]
        """
        return np.mean(vectors, axis=0)
    
    @staticmethod
    def vector_statistics(vector: np.ndarray) -> dict:
        """
        Calculate comprehensive statistics for a vector.
        
        Args:
            vector: Input vector
            
        Returns:
            Dictionary with statistical measures
            
        Example:
            >>> v = np.array([1, 2, 3, 4, 5])
            >>> stats = VectorOperations.vector_statistics(v)
            >>> print(stats)
            {'mean': 3.0, 'median': 3.0, 'std': 1.41, ...}
        """
        return {
            'mean': np.mean(vector),
            'median': np.median(vector),
            'std': np.std(vector),
            'var': np.var(vector),
            'min': np.min(vector),
            'max': np.max(vector),
            'sum': np.sum(vector),
            'magnitude': VectorOperations.magnitude(vector)
        }


def demo():
    """
    Demonstration of all vector operations.
    """
    print("=" * 60)
    print("NumPy Vector Operations Demo - Week 3")
    print("=" * 60)
    
    # Create vectors
    print("\n1. Creating Vectors:")
    v1 = VectorOperations.create_vector([1, 2, 3])
    v2 = VectorOperations.create_vector([4, 5, 6])
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    # Basic operations
    print("\n2. Basic Operations:")
    print(f"v1 + v2 = {VectorOperations.vector_add(v1, v2)}")
    print(f"v1 - v2 = {VectorOperations.vector_subtract(v1, v2)}")
    print(f"v1 * 3 = {VectorOperations.scalar_multiply(v1, 3)}")
    print(f"v1 · v2 (dot product) = {VectorOperations.dot_product(v1, v2)}")
    
    # Advanced operations
    print("\n3. Advanced Operations:")
    print(f"|v1| (magnitude) = {VectorOperations.magnitude(v1):.4f}")
    print(f"Normalized v1 = {VectorOperations.normalize(v1)}")
    print(f"Cosine similarity = {VectorOperations.cosine_similarity(v1, v2):.4f}")
    print(f"Euclidean distance = {VectorOperations.euclidean_distance(v1, v2):.4f}")
    
    # Element-wise operations
    print("\n4. Element-wise Operations:")
    print(f"v1 ⊙ v2 (element-wise) = {VectorOperations.element_wise_multiply(v1, v2)}")
    
    # Statistics
    print("\n5. Vector Statistics:")
    v3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    stats = VectorOperations.vector_statistics(v3)
    print(f"Vector: {v3}")
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}")
    
    # Multiple vectors
    print("\n6. Multiple Vector Operations:")
    vectors = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9])
    ]
    mean_vec = VectorOperations.mean_vector(vectors)
    print(f"Mean of {len(vectors)} vectors: {mean_vec}")
    
    print("\n" + "=" * 60)
    print("✅ All operations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
