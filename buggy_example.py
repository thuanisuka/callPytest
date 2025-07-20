# buggy_example.py

def divide(a, b):
    return a / b  # Lỗi chia cho 0 có thể xảy ra

def print_list_items(items):
    for i in range(0, len(items)):
        print(items[i])  # Code smell: không cần dùng chỉ số

def unused_function():
    pass  # Code smell: function được định nghĩa nhưng không dùng

def main():
    divide(10, 0)  # Bug runtime
    print_list_items(["apple", "banana", "cherry"])

main()
