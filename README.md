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

Here are some examples:
```bash
# parse markdown files into HTML
td --output=html blog.md


# parse markdown files and pretty print to stdout
td --pretty blog.md


# parse all markdown files in a diectory
td ../path/to/files/*.md


# parse all markdown files from a directory, and write outputs into another directory
# NOTE: all the output files will have the same names
#   - Ex: ../path/to/markdown_files/first_blog.md => ./blogs/first_blog.json
td --output=./blogs/ ../path/to/markdown_files/*.md


# kill process if an error occurs
td --failfast blog.md


# strictly validate markdown syntax and kill process if invalid
td --strict blog.md
```

For more info here's the usage text
```
usage: td [-h] [-d DESTINATION] [-o {json,html}] [-v] [-f] [-s] [-p] Files [Files ...]

Parse markdown files

positional arguments:
  Files                 Set of files that will parsed

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        Output directory
  -o {json,html}, --output {json,html}
                        Specify output format (default: json)
  -v, --verbose         Log time it took to parse each file (default: false)
  -f, --failfast        Kill process if an error occurs (default: false)
  -s, --strict          Kill process if invalid markdown syntax (default:
                        false)
  -p, --pretty          Format output
```

### How to use Python module

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

### Why develop yet another Markdown parser?

The simple answer is there just isn't a Markdown parser that I like. Ideally, I'd like a Markdown parser that has strict parsing rules, can output to several formats (JSON and HTML), hands over full control of the parsing loop to the user, and doesn't come bundled with other packages.

I had enough custom needs that I figured I write it myself. Hopefully you'll find one of these features useful to your own projects.

Happy Coding 👩‍💻
