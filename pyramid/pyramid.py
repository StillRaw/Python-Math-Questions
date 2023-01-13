import math

def read_file(file_name=str):
    """Read .txt file. Clear lines. Create a list of lines."""
    with open(file_name, "r") as f:
        lines_raw=(f.readlines())
        lines = [i.replace("\n","").split(" ") for i in lines_raw]

        return lines

def prime_number(number=int):
    """Test whether it is divisible only up to the square root of the number."""
    if number > 1:
        floor_number= math.floor(number**0.5)
        for i in range(2,floor_number):
            if (number % i == 0):
                return False
        else:
            return True
    else:
        return False

def decide_max_number(lines,max_numbers=[],selected_index=0):
    """Create a list of max-non-prime number of desired interval of line."""
    for i in lines:
        max_number_of_line = int(max(lines[lines.index(i)][selected_index:selected_index+2]))#max number
        min_number_of_line = int(min(lines[lines.index(i)][selected_index:selected_index+2]))#min number

        if not prime_number(max_number_of_line):
            max_numbers.append(max_number_of_line)
            selected_index=lines[lines.index(i)].index(str(max_number_of_line))
        else:
            max_numbers.append(min_number_of_line)
            selected_index=lines[lines.index(i)].index(str(min_number_of_line))    
    return max_numbers

def sum_max_num(max_numbers):
    """Sum all max numbers."""
    result = sum(max_numbers)
    print(result)
    return result

if __name__ == "__main__":
    file_name="pyramid.txt"
    lines=read_file(file_name)
    max_numbers=decide_max_number(lines)
    sum_max_num(max_numbers)