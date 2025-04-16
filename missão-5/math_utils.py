def add(a, b): 
    return a + b 
 
def subtract(a, b): 
    return a - b

def multiply(a, b): 
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): 
        raise ValueError("Both arguments must be numbers") 
    return a * b