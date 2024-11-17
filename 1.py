# TODO решите задачу
import json
import decimal


def task(filepath)-> float:
    with open(filepath, 'r') as f:
        data = json.load(f)

    total_sum = decimal.Decimal(0)
    for item in data:
        score = decimal.Decimal(item['score'])
        weight = decimal.Decimal(item['weight'])
        total_sum += score * weight

    return total_sum.quantize(decimal.Decimal("0.001"))


# Example usage with input.json
input_sum = task('input.json')
print(input_sum)


