import sys

def get_triangle(rows: int) -> list[list[int]]:
    triangle = [[1]]
    for i in range(1, rows):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

def print_triangle(triangle: list[list[int]]):
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python triangle.py <number of rows>")
        sys.exit(1)
    
    try:
        rows = int(sys.argv[1])
        if rows < 0:
            raise ValueError("Number of rows must be non-negative")
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    
    triangle = get_triangle(rows)
    print_triangle(triangle)
