import json

def make_caption(description_arr):
    description = []
    count = 0

    for line in description_arr:
        j = len(line)

        if (count + j) < 500:

            description.append(f'{line}')
            count = count + j
    print(count)
    description_result = "\n\n".join(description)

    return description_result
