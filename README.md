# Touchdown

A CLI and Python module to parse Markdown and Mdx

### Table of Contents
1. [Install](#install)
2. [CLI](#cli)
3. [Auto Sanitization](#auto-sanitization)
3. [Touchdown's Python Library](#touchdowns-python-library)
4. [Markdown Specification](#markdown-specification)


### Install
```
pip install git+https://github.com/11/touchdown@main
```

### CLI 
Touchdown has the capability to parse Markdown files into `HTML`, or into an alternative web-friendly `JSON` format. This alternative `JSON` format is useful for non-static websites, creating your own website build tools, or in situations where markup is asynchronously added to a page.

```bash
# Parse Markdown files into HTML
touchdown blog.md
touchdown --output=HTML blog.md

# Write HTML output to file
touchdown blog.md > blog.html

# Parse Markdown to JSON
touchdown --output=JSON blog.md 
touchdown --output=JSON blog.md > blog.json

# Write HTML output to file
touchdown --output=JSON blog.md > blog.json
```

### Auto Sanitization
Touchdown will automatically sanatize your Markdown. This in turn means that syntax errors are raised while parsing. 

As an example, if you were to try parse the following markdown:
```markdown
* This should is bold
```

In this scenario, Touchdown would throw an error because special characters (bold, italic, strikethrough, math, code, etc.) require a closing character. When an error occurs, Touchdown will print an error message to stderror
```
MarkdownSyntaxError - "File example.md": line 1
  `*` does not have a matching closing character
```

### Touchdown's Python Library
Touchdown is also a python module that you can use in your own projects.
```python3
from pathlib import Path
from touchdown import (
    to_html, 
    to_dict, 
    to_json,
    MarkdownSyntaxError,
)

blog = Path('./blogs/blog.md')
try:
    blog_html = to_html(blog) # parses blod.md into a string of HTML
    blog_dict = to_dict(blog) # parses blog.md into a web-friendly dictionary format
    blog_json = to_json(blog) # parses blog.md into a web-friendly dictionary format, but then returns the result as a JSON string
except MarkdownSyntaxError as md_err:
    print(md_err)
```

### Custom Parsing
As it is common in programs that parse text, Touchdown creates an intermediate format of the Markdown it parses. This intermediate format takes on the structure of an abstract syntax tree. This abstract syntax tree was designed to be easily parsable by anyone wanting to more control over the parsing process. 

```python3
from pathlib import Path
from touchdown import (
    to_ast,
    MarkdownSyntaxError,
)

blog = Path('./blogs/blog.md')
try:
    ast = to_ast(blog)
    
    # the abstract syntax tree object is designed to be iterable.
    # this was a design choice so users could easily iterate through
    # each node in the tree tree without having to understand the details
    # of the abstract syntax tree structure
    for token in ast:
        if token['type'] == 'header':
            token['type'] == 'paragraph'
            token['tag'] = 'p'
except MarkdownSyntaxError as md_err:
    print(md_error)
```

### Markdown Specification
Touchdown's Markdown syntax comes in 2 flavors depending on the file extension you use with your Markdown:
1. `.md`: If you use the `.md` extension, Touchdown will support the [following spec](https://github.com/11/touchdown/link-to-md-spec.md)
2. `.mdx`: If you use the `.mdx` extension, Touchdown will use its custom [extended syntax spec](https://github.com/11/touchdown/link-to-mdx-spec.md)

