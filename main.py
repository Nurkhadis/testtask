import base64
import json

def serialize(numbers):
    serialized_data = json.dumps(numbers)
    encoded_data = base64.b64encode(serialized_data.encode()).decode()
    return f"S{encoded_data}"

def deserialize(serialized_string):
    if serialized_string[0] != 'S':
        raise ValueError("Invalid serialized string")

    encoded_data = serialized_string[1:]
    decoded_data = base64.b64decode(encoded_data).decode()
    numbers = json.loads(decoded_data)
    return numbers

# Тесты
tests = [
    [1, 2, 3],
    list(range(1, 51)),
    list(range(1, 101)),
    list(range(1, 501)),
    list(range(1, 1001)),
    [1] * 1000,
    list(range(10, 100, 10)),
    list(range(100, 1000, 100)),
    list(range(111, 1000, 3))
]

for test in tests:
    serialized = serialize(test)
    deserialized = deserialize(serialized)
    compression_ratio = len(serialized) / len(str(test))

    print(f"Original: {test}")
    print(f"Serialized: {serialized}")
    print(f"Deserialized: {deserialized}")
    print(f"Compression ratio: {compression_ratio:.2%}")
    print("="*30)
