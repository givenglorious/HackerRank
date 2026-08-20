regex_pattern = r"[,.]"	# Do not delete 'r'.
#https://docs.python.org/3/howto/regex.html

import re
print("\n".join(re.split(regex_pattern, input())))