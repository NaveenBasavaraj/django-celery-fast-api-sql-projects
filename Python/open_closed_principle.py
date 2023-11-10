from enum import Enum 

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# Open closed principle --> OPEN FOR EXTENSION, CLOSED FOR MODIFICATION

# LEts say we have below class with filter by color
# If in the future we add a filter to filter by size
# then we violate open close principle

class ProductFilter:
    def filter_by_color(self,products,color):
        for p in products:
            if p.color == color: yield p
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
            
    def filter_by_size_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p
    

class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color
    
    def is_s