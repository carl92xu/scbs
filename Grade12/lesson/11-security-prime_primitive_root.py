def prime_primitive_root(primitive_root, prime):
    results = []
    for power in range(1, 50000*17-1):
        result = (primitive_root ** power) % prime
        results.append(result)
        # print(primitive_root, "**", power, "MOD", prime, "=", result)
    results.sort()
    print(results)


prime_primitive_root(3, 17)
