import re
content = "Hello 123 4567 World_This is a Regex Demo"
print(len(content))
result = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}",content)
print(result)
print(result.group())#输出匹配内容
print(result.span())#输出值的范围
print('-'*30)
content = "Hello 1234567 World_This is a Regex Demo"
result = re.match('^Hello\s(\d+)\sWorld_This',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())