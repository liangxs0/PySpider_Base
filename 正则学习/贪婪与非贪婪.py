import re

content = "hello 12345 World_This is a Regex Demo"

result = re.match("^he.*(\d+).*Demo$",content)
#贪婪匹配导致he.*匹配了多得数字，只留了一个5给\d
print(result)
print(result.group(1))
#非贪婪匹配
res = re.match("^he.*?(\d+).*o$",content)
print(res)
print(res.group(1))