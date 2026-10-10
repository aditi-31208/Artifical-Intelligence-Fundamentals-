# Map Coloring using CSP and Backtracking

# Step 1: Define the map (CSP variables and constraints)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Step 2: Define available colors
colors = ['Red', 'Green', 'Blue']

# Step 3: Store the color assigned to each region
assignment = {}


# Step 4: Check whether a color can be assigned
def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# Step 5: Backtracking function
def backtrack():
    
    # If all regions are colored, solution is found
    if len(assignment) == len(graph):
        return True

    # Select an uncolored region
    for region in graph:
        if region not in assignment:
            
            # Try each available color
            for color in colors:
                
                # Check whether the color is safe
                if is_safe(region, color):
                    
                    # Assign the color
                    assignment[region] = color
                    
                    # Recursively color the remaining regions
                    if backtrack():
                        return True
                    
                    # If it does not work, remove the color
                    del assignment[region]

            # No color works for this region
            return False


# Step 6: Start the backtracking algorithm
if backtrack():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, "=", color)
else:
    print("No solution exists.")
