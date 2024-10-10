class DayOne: 

    def read_file(self, filename): 
        with open(filename, 'r') as file: 
            lines = file.readlines() 
        return lines
    
    def __get_first_num__(self, val): 
        num_char = 'z'
        for char in val: 
            try: 
                int(char)
                num_char = char
                break
            except:
                continue
        return num_char
        
    def get_total(self, val_list): 
        total = 0
        for val in val_list:
            val_1 = self.__get_first_num__(val)
            val_2 = self.__get_first_num__(val[::-1])

            num = val_1 + val_2
            total += int(num)

        return(total)
    
day_one = DayOne()

example_filename = "day_1_example_input.txt"
example_lines = day_one.read_file(example_filename)
example_total = day_one.get_total(example_lines)

print("Example total: \t", example_total)

input_filename = "day_1_input.txt"
input_lines = day_one.read_file(input_filename)
input_total = day_one.get_total(input_lines)

print("Input total: \t", input_total)