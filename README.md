# Touchdown

A convenient CLI tool and python module to parse Markdown



### How to use CLI?

I didn't feel this project was worthy enough to upload to a global registry. So instead here are steps to clone the project and bind to a terminal command
```bash
# clone into your bin directory
$ git clone https://github.com/11/touchdown.git /usr/bin/
```

Alias the `td` command to run the `touchdown.__main__.py` file inside your `.bashrc` (or `.bash_profile`)
```bash
alias td="python3 /usr/bin/touchdown/__main__.py"
```


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

