from lab9_1V_2R import max_wire_length

def test_max_wire_length():
    tests = [
        
        (2, [3, 3, 3], 5.65),
        (100, [1, 1, 1, 1], 300.00),
        (4, [100, 2, 100, 2, 100], 396.32),
        (4, [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26,
             86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2,
             95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34,
             52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51,
             11, 39, 72], 2738.18)
    ]

    for i, (w, heights, expected) in enumerate(tests, 1):
        result = max_wire_length(w, heights)
        assert abs(result - expected) < 0.01, f"❌ Test {i} failed: expected {expected}, got {result}"
        print(f"✅ Test {i} passed: {result} == {expected}")


test_max_wire_length()
