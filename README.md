# Touchdown

A convenient CLI tool and python module to parse Markdown


### Install as Terminal Command

I didn't feel this project was worthy enough to upload to a global registry. So instead here are steps to clone the project and bind to a terminal command
```bash
git clone https://github.com/11/touchdown.git /usr/bin/
```

Alias the `td` command to run the `touchdown` module inside your `.bashrc` (or `.bash_profile` on mac)
```bash
alias td="python3 -m /usr/bin/touchdown/touchdown/"
```

Recompile your bash config to load the `td` command into your terminal session
```bash
source ~/.bashrc    # or ~/.bash_profile if you're on mac
```

From there you can start parsing markdown files
```bash
td blog.md
```

### Terminal Command Examples
```bash
#Parse markdown files into HTML
td --output=html blog.md

# Parse markdown files and pretty print to stdout
td --pretty blog.md

# Parse all markdown files in a diectory
td ../path/to/files/*.md

# Parse all markdown files from one directory, and write the outputs into another directory
td --output=./blogs/ ../path/to/markdown_files/*.md

# Validate markdown syntax - kill process if invalid and log error message
td --strict blog.md
```

### How to use Python Module

Quickly parse Markdown file

```python3
from touchdown import Markdown as Md

blog = Md('path/to/markdown_file.md')
blog.parse()    # default output format is JSON
blog.parse(output='html')    # outputs HTML
blog.parse(output='json', pretty=True)    # outputs JSON and pretty prints it
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

### Why Develop Yet Another Markdown Parser?

The simple answer is there just isn't a Markdown parser that I like. Ideally, I'd like a Markdown parser that has strict parsing rules, can output to several formats (JSON and HTML), hands over full control of the parsing loop to the user, and doesn't come bundled with other packages.

I had enough custom needs that I figured I write it myself. Hopefully you'll find one of these features useful to your own projects.

Happy Coding 👩‍💻
