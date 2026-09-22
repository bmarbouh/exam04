def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = []
    
    for i in range(dim):
        grid.append(['.'] * dim)
        
    for row, col in stars:
        if 0 <= row < dim and 0 <= col < dim:
            grid[row][col] = '*'
    
    result = []
    
    for row in grid:
        result.append(''.join(row))
    
    return result

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
print(constellation_mapper([], 2))
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
print(constellation_mapper([(0, 0), (5, 5)], 3))
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))