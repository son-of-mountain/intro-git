import re

def rearrange_name(name):

    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

    if result == None:

        return name

