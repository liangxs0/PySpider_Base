import re
content = "Extra stings Hello 12345 World_This a Regex Demo Extra stings"
result = re.match("Hello.*?(\d+).*?Demo",content)#不从头开始匹配 match匹配失败
print(result)

result = re.search("Hello.*?(\d+).*?Demo",content)
print(result.group(1))