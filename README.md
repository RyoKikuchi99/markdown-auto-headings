# Markdown Auto Headings

## Overview
This program adds specific prefix and number automatically to a markdown document due to the depth of headings.

## Usage
```python
generate_auto_headings(
    markdown_text: str,
    prefix: str,
    delimiter: str,
    heading_start_pos: int):
```

The input text is defined as follows:

```python
input_text = (
    "# Introduction\n"
    "## Section 1\n"
    "### Subsection 1.1\n"
    "## Section 2\n"
    "### Subsection 2.1\n"
    "### Subsection 2.2\n"
)
```

Call ```generate_auto_headings``` like this:
```python
output = generate_auto_headings(input_text, 'A', '-', 1)
print(output)
```

The output text shall be:
```shell
# [A-1] Introduction
## [A-1-1] Section 1
### [A-1-1-1] Subsection 1.1
## [A-1-2] Section 2
### [A-1-2-1] Subsection 2.1
### [A-1-2-2] Subsection 2.2
```
