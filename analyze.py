TEMP_FILE = "temperture.log"
RED = "\033[0;31m"
NO_COLOR = "\033[0m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"


def analyze_temp():
    '''
    Analyze the temperture log. Find the lowest, highest, and average tempertures
    
    '''
    running_total = 0
    iterations = 0
    highest_temp = 0
    lowest_temp = 10000

    try:
        with open(TEMP_FILE) as temp_file:
            for temp_value in temp_file:
                start_index = temp_value.find('=') + 1
                end_index = temp_value.find('\'')
                if start_index == -1 or end_index == -1:
                    continue

                raw_temperture = float(temp_value[start_index:end_index])
                running_total += raw_temperture
                if raw_temperture > highest_temp:
                    highest_temp = raw_temperture
                elif raw_temperture < lowest_temp:
                    lowest_temp = raw_temperture
                iterations += 1
        
        average_temp = running_total / iterations
        print(f'Analysis for {iterations} samples:')
        print(f'{BLUE}Lowest Temperture{NO_COLOR}:     {round(lowest_temp, 2)}\'C')
        print(f'{YELLOW}Average Temperture{NO_COLOR}:    {round(average_temp, 2)}\'C')
        print(f'{RED}Highest Temperture{NO_COLOR}:    {round(highest_temp, 2)}\'C')
    except Exception as e:
        print(f'Error analyzing {TEMP_FILE}: {e}')


def main():
    analyze_temp()

if __name__ == '__main__':
    main()