import re
import os

def extract_code_blocks(md_text):
    """Extract code blocks from Markdown text."""
    code_blocks = []
    for match in re.finditer(r'```py(.*?)```', md_text, re.DOTALL):
        group = match.group(1)
        stripped_group = group.strip()
        code_blocks.append(stripped_group)
        # code_blocks.append(match.group(1).strip())
    print('code_blocks')
    print(code_blocks, sep='\n')
    return code_blocks

def extract_titles(md_text):
    """Extract titles from Markdown text."""
    titles = []
    for match in re.finditer(r'^(#{6,6})\s+(.*)', md_text, re.MULTILINE):
        level, title = len(match.group(1)), match.group(2).strip()
        if level == 6:  # Modify based on the level of title you're interested in
            titles.append(title)
    print('titles')
    print(titles, sep='\n')
    return titles

def save_code_blocks_to_files(dirname, titles:list[str], code_blocks):
    """Save each code block to a .py file with the title as the file name."""
    for title, code in zip(titles, code_blocks):
        processed_title:str = title.replace(' ', '_')  # Create a valid file name
        file_name = f".\{dirname}\{processed_title}.py"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(code)
        print(f"Saved '{file_name}'")

def get_file_name_8_file_extension(file_path):
    import re

    # file_path = 'xx.md'
    match = re.match(r'(.+)\.(.+)', file_path)
    if match:
        file_name, file_extension = match.groups()
        print("File Name:", file_name)
        print("File Extension:", file_extension)
    return file_name, file_extension

def main(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
    
    titles = extract_titles(md_text)
    code_blocks = extract_code_blocks(md_text)
    file_name, file_extension = get_file_name_8_file_extension(md_file_path)
    print(len(titles) , len(code_blocks))
    if len(titles) != len(code_blocks):
        print("Warning: Number of titles and code blocks do not match!")
        return
    
    save_code_blocks_to_files(dirname=file_name, titles=titles, code_blocks=code_blocks)

if __name__ == "__main__":
    md_file_path = '3.创建型模式.md'  # Change to your Markdown file path
    # md_file_path = '4.结构型模式.md'  # Change to your Markdown file path
    main(md_file_path)
