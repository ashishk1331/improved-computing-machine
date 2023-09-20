def factorial(n, map):
    if n < 2:
        return n
    
    if n in map:
        return map[n]

    result = factorial(n-1, map) + factorial(n-2, map)

    map[n] = result

    return result


print(f"""
Hello world.
Factorial of 25 is {factorial(25, {})}
""")