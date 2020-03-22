import re
content0 = "2020-03-19 12:00"
content1 = "2020-04-16 13:00"
content2 = "2020-07-25 17:50"
pattern = re.compile('\d{2}:\d{2}')
res0 = re.sub(pattern,"",content0)
res1 = re.sub(pattern,"",content1)
res2 = re.sub(pattern,"",content2)
print(res0,res1,res2)