import re
import os

def extract_title_code_pairs(md_text):
    """Extract titles and code blocks from Markdown text."""
    title_code_pairs = []
    pattern = re.compile(r'(^(#{6,6})\s+(.*))|(```py(.*?)```)', re.DOTALL | re.MULTILINE)
    current_title = None
    for match in pattern.finditer(md_text):
        if match.group(1):  # Title
            level, title = len(match.group(1)), match.group(2).strip()
            if level == 6:  # Modify based on the level of title you're interested in
                current_title = title
        elif match.group(3):  # Code block
            if current_title:
                code = match.group(3).strip()
                title_code_pairs.append((current_title, code))
                current_title = None  # Reset title for next code block
    print('Title-Code Pairs')
    print(title_code_pairs, sep='\n')
    return title_code_pairs

def save_code_blocks_to_files(dirname, title_code_pairs):
    """Save each code block to a .py file with the title as the file name."""
    for title, code in title_code_pairs:
        processed_title = title.replace(' ', '_')  # Create a valid file name
        file_name = f".\\{dirname}\\{processed_title}.py"
        with open(file_name, 'w') as file:
            file.write(code)
        print(f"Saved '{file_name}'")

def get_file_name_8_file_extension(file_path):
    import re
    match = re.match(r'(.+)\.(.+)', file_path)
    if match:
        file_name, file_extension = match.groups()
        print("File Name:", file_name)
        print("File Extension:", file_extension)
    return file_name, file_extension

def main(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
    
    title_code_pairs = extract_title_code_pairs(md_text)
    file_name, file_extension = get_file_name_8_file_extension(md_file_path)
    save_code_blocks_to_files(dirname=file_name, title_code_pairs=title_code_pairs)

if __name__ == "__main__":
    md_file_path = '3.创建型模式.md'  # Change to your Markdown file path
    md_file_path = '4.结构型模式.md'  # Change to your Markdown file path
    main(md_file_path)
