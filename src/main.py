import markdown as md


file = md.Markdown('../tests/test_header.md')
file.parse()
print(file)
