def string_compression(input_string: str):

    compressed_string = 0

    count = 1

    for i in range(len(input_string)):
        if input_string[i+1] == input_string[i]:
            count += 1
        else:
            compressed_string += input_string[i] + str(count)
            count = 1
    
    compressed_string += input_string[i] + str(count)

    if len(compressed_string) < len(input_string):
        return compressed_string
    else:    
        return input_string