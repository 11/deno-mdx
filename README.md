# Touchdown

A convenient CLI tool and python module to parse Markdown


### Why develop yet another Markdown parser?

The simple answer is there just isn't a Markdown parser that I like. Ideally, I'd like a Markdown parser that has strict parsing rules, can output to several formats (JSON and HTML), hands over full control of the parsing loop to the user, and doesn't come bundled with other packages.

I had enough custom needs that I figured I write it myself. Hopefully you'll find one of these features useful to your own projects.

Happy Coding 👩‍💻

### How to install CLI?

I didn't feel this project was worthy enough to upload to a global registry. So instead here are steps to clone the project and bind to a terminal command
```bash
git clone https://github.com/11/touchdown.git /usr/bin/
```

Alias the `td` command to run the `touchdown.__main__.py` file inside your `.bashrc` (or `.bash_profile` on mac)
```bash
alias td="python3 /usr/bin/touchdown/__main__.py"
```

Recompile your bash config to load the `td` command into your terminal session
```bash
source ~/.bashrc    # or ~/.bash_profile if you're on mac
```

### How to use CLI?

Parse markdown files to JSON or HTML
```bash
# The default output format is JSON
td blog.md    # outputs JSON

# You can be explict about the output format by using the `-o` or `--output` flag
td -o=json blog.md
td --output=json blog.md

# Output HTML by updating the format option
td -o=html blog.md
td --output=html blog.md
```

### How to use Python module

Quickly parse Markdown file

```python3
from touchdown import Markdown as Md

blog = Md('path/to/markdown_file.md')
blog.parse()    # default output format is JSON
blog.parse(output='json')    # outputs JSON
blog.parse(output='html')    # outputs HTML
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

