# Touchdown

A convenient CLI tool and python module to parse Markdown

### How to use CLI?

Parse markdown into JSON format
```bash
td --format=json  blog.md
td -f=json blog.md

# The default output format is JSON
td blog.md 
```

Parse markdown to HTML format
```bash
td --format=html blog.md
td -f=html blog.md
```


### How to use Python module

Quickly parse Markdown file

```python3
from touchdown import Markdown as MD

blog = MD('path/to/markdown_file.md')
print(blog.parse()) # output's JSON 
```

Customize the Markdown parsing 
```python3
from touchdown import Markdown as MD

blog = MD('path/to/markdown_file.md')

headers = []
for symbol in blog:
    if symbol['token'] == 'header':
       headers.append(symbol)
```

