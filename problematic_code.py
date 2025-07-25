import os

def process_data(data):
    temp = 123  # Unused variable
    if not data:
        return

    result = []
    for i in range(len(data)):
        if data[i] == 0:
            continue
        elif data[i] == 1:
            result.append("One")
        elif data[i] == 2:
            result.append("Two")
        elif data[i] == 3:
            result.append("Three")
        elif data[i] == 4:
            result.append("Four")
        elif data[i] == 5:
            result.append("Five")
        elif data[i] == 6:
            result.append("Six")
        elif data[i] == 7:
            result.append("Seven")
        elif data[i] == 8:
            result.append("Eight")
        elif data[i] == 9:
            result.append("Nine")
        else:
            result.append("Unknown")
    return result

def insecure_eval(input_str):
    return eval(input_str)  # Critical security issue: use of eval
