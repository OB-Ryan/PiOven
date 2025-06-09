TEMP_FILE = "temperature.log"
RED = "\033[0;31m"
NO_COLOR = "\033[0m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"


def analyze_temp():
    '''
    Analyze the temperature log. Find the lowest, highest, and average temperatures
    
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

                raw_temperature = float(temp_value[start_index:end_index])
                running_total += raw_temperature
                if raw_temperature > highest_temp:
                    highest_temp = raw_temperature
                elif raw_temperature < lowest_temp:
                    lowest_temp = raw_temperature
                iterations += 1
        
        average_temp = running_total / iterations
        print(f'Analysis for {iterations} samples:')
        print(f'{BLUE}Lowest temperature{NO_COLOR}:     {round(lowest_temp, 2)}\'C')
        print(f'{YELLOW}Average temperature{NO_COLOR}:    {round(average_temp, 2)}\'C')
        print(f'{RED}Highest temperature{NO_COLOR}:    {round(highest_temp, 2)}\'C')
    except Exception as e:
        print(f'Error analyzing {TEMP_FILE}: {e}')


def main():
    analyze_temp()

if __name__ == '__main__':
    main()