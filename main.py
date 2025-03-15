import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    x = [random.uniform(*bound) for bound in bounds]
    best_value = func(x)
    
    for _ in range(iterations):
        new_x = [xi + random.uniform(-0.1, 0.1) for xi in x]
        new_x = [max(bounds[i][0], min(bounds[i][1], new_x[i])) for i in range(len(bounds))]
        new_value = func(new_x)
        
        if new_value < best_value:
            x, best_value = new_x, new_value
        
        if abs(new_value - best_value) < epsilon:
            break
    
    return x, best_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_x = [random.uniform(*bound) for bound in bounds]
    best_value = func(best_x)
    
    for _ in range(iterations):
        new_x = [random.uniform(*bound) for bound in bounds]
        new_value = func(new_x)
        
        if new_value < best_value:
            best_x, best_value = new_x, new_value
        
        if abs(new_value - best_value) < epsilon:
            break
    
    return best_x, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    x = [random.uniform(*bound) for bound in bounds]
    best_x, best_value = x, func(x)
    
    for _ in range(iterations):
        new_x = [xi + random.uniform(-0.1, 0.1) for xi in x]
        new_x = [max(bounds[i][0], min(bounds[i][1], new_x[i])) for i in range(len(bounds))]
        new_value = func(new_x)
        
        if new_value < best_value or random.random() < math.exp((best_value - new_value) / temp):
            x, best_value = new_x, new_value
        
        temp *= cooling_rate
        
        if temp < epsilon:
            break
    
    return x, best_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]
    
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)
    
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)
    
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)