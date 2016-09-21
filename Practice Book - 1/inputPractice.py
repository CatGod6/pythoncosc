with open("hello.txt", "r") as my_input_file , open("hi.txt" , "w") as my_output :
    for line in my_input_file.readlines() :
        my_output.write(line)

# Remidner pages 122-141 of Book 1 Cover reading and writing data to a file in VAST detail

