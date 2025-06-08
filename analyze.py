TEMP_FILE = "temperture.log"

def analyze_temp():
    with open(TEMP_FILE) as temp_file:
        running_total = 0
        iterations = 0
        for temp_value in temp_file:
            start_index = temp_value.find('=') + 1
            end_index = temp_value.find('\'')
            raw_temperture = temp_value[start_index:end_index]
            running_total += float(raw_temperture)
            iterations += 1

    average_temp = running_total / iterations
    print(f'Average temperture for {iterations} samples:    {round(average_temp, 2)}\'C')


def main():
    analyze_temp()


if __name__ == '__main__':
    main()