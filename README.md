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
# The default output format is JSON
td blog.md

# You can specific the format using the `-f` or `--format` option
td -f=json blog.md
td --format=json blog.md
```

Parse markdown to HTML format
```bash
td -f=html blog.md
td --format=html blog.md
```


### How to use Python module

Quickly parse Markdown file

```python3
from touchdown import Markdown as Md

blog = Md('path/to/markdown_file.md')
blog.parse()

print(blog.json)    # writes JSON to stdout
print(blog.html)    # writes HTML to stdout
```

Customize the Markdown parsing
```python3
from touchdown import Markdown as Md

blog = Md('path/to/markdown_file.md')

headers = []
for symbol in blog:
    if symbol['token'] == 'header':
       headers.append(symbol)
```

