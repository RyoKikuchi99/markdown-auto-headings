import re


def generate_auto_headings(
        markdown_text: str,
        prefix: str,
        delimiter: str,
        heading_start_pos: int):

    # Split the markdown text into lines
    lines = markdown_text.split("\n")

    # Initialize the header number stack
    header_num_stack = [0]

    # Iterate over the lines
    for i in range(len(lines)):
        line = lines[i]

        # Check if the line is a header
        match = check_header(heading_start_pos, line)
        if match:
            # Get the header level and text
            header_level, header_text = get_header(match)

            # Normalize length of header number by the number of '#'
            # which starts to count heading
            len_header_num_stack = normalize_header_length(
                header_num_stack,
                heading_start_pos)

            # Update the header number stack
            header_num_stack, len_header_num_stack = update_header_num_stack(
                header_num_stack, len_header_num_stack, header_level)

            # Increment the header number
            header_num_stack[-1] += 1

            # Construct the new header text
            new_header_text = construct_new_header_text(
                header_num_stack,
                header_text,
                prefix,
                delimiter)

            # Replace the line with the new header text
            lines[i] = "#" * header_level + " " + new_header_text

    # Join the lines back together
    return "\n".join(lines)


def construct_new_header_text(
        header_num_stack: list[int],
        header_text: str,
        prefix: str,
        delimiter: str):
    header_number_str = prefix + delimiter +\
        delimiter.join(str(x) for x in header_num_stack)
    return f"[{header_number_str}] {header_text}"


def update_header_num_stack(
        header_num_stack: list[int],
        len_header_num_stack: int,
        header_level: int):

    while len_header_num_stack < header_level:
        header_num_stack.append(0)
        len_header_num_stack += 1
    while len_header_num_stack > header_level:
        header_num_stack.pop()
        len_header_num_stack -= 1

    return header_num_stack, len_header_num_stack


def normalize_header_length(
        header_num_stack: list[int],
        heading_start_pos: int):
    return len(header_num_stack) + heading_start_pos - 1


def check_header(heading_start_pos: int, line: str):
    return re.match(r"^(#{%d,}+)\s+(.*)$" % heading_start_pos, line)


def get_header(match: re.Match[str]):
    # Get the header level and text
    header_level = len(match.group(1))
    header_text = match.group(2)
    text_removed_bracket = remove_text_inside_brackets(header_text)
    return header_level, text_removed_bracket


def remove_text_inside_brackets(text: str):
    return (re.sub(r'\[.*?\]\s*', "", text))


def read_markdown_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_markdown_file(file_path: str, text: str):
    with open(file_path, "w", encoding="utf-8") as f:
        return f.write(text)


if __name__ == '__main__':
    # Pefix for heading e.g. "A-1-1", "ABCD-1-1"
    prefix = 'A'
    # Delimiter in text
    delimiter = '-'
    # The number of '#' which starts to count heading
    heading_start_pos = 1

    file_path_input = 'input.md'
    file_path_output = 'output.md'

    text = read_markdown_file(file_path_input)
    text_modified = generate_auto_headings(
        text,
        prefix,
        delimiter,
        heading_start_pos)
    write_markdown_file(file_path_output, text_modified)
