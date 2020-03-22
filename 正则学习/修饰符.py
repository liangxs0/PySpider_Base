import re

content = '''hello 1234567 World_This 
is a Regex Demo
'''
result = re.match("^he.*?(\d+).*?Demo$",content,re.S)
print(result.group(1))