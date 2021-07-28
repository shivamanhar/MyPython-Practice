line = "This is python programming test;I am try to run code and want to learn-new things"
import re
split_line = re.split(r'[;]', line)
print(split_line)
