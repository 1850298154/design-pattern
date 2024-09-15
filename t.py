import re
import os

class CodeBlocksExtractor:
    def __init__(self, title:str='', codes:list[str]=[]):
        self.title = title
        self.codes = codes

def extract_title_code_pairs(md_text):
    """Extract titles and code blocks from Markdown text."""
    title_code_pairs = []
    p_prefix = r'(?m)'  # (?m) 是 re.MULTILINE 的 inline flag，确保 ^ 和 $ 匹配每行的开始和结束。
    p_prefix = r''  
    p1 = r'(^(#{6,6})\s+([^\n]+))' 
    # (?m) 是 re.MULTILINE 的 inline flag，确保 ^ 和 $ 匹配每行的开始和结束。
    # ^(#{1,6})\s+([^\n]+) 匹配标题行，其中 ([^\n]+) 确保只匹配标题文本，直到行结束。
    p2 = r'(```py(.*?)```)'
    p = p_prefix + f'{p1}|{p2}'
    p1_group_idx    = 1
    level_group_idx = 2
    title_group_idx = 3
    p2_group_idx    = 4
    code_group_idx  = 5
    # pattern = re.compile(r'(^(#{6,6})\s+(.*))|(```py(.*?)```)', re.DOTALL | re.MULTILINE)
    # pattern = re.compile(p, re.DOTALL )#| re.MULTILINE) # 两种方式可以使用
    pattern = re.compile(p, re.DOTALL | re.MULTILINE)
    # current_title = None
    cbe_list:list[CodeBlocksExtractor] = []
    for match in pattern.finditer(md_text):
        if match.group(p1_group_idx):  # Title
            level = len(match.group(level_group_idx)) 
            title = match.group(title_group_idx).strip()
            if level == 6:  # Modify based on the level of title you're interested in
                # current_title = title
                cbe = CodeBlocksExtractor(title, [])
                cbe_list.append(cbe)
                # cbe.title = title
        elif match.group(p2_group_idx):  # Code block
            # if current_title:
            code = match.group(code_group_idx).strip()
            # title_code_pairs.append((current_title, code))
            # current_title = None  # Reset title for next code block
            cbe.codes.append(code)
    # print('Title-Code Pairs')
    # print(title_code_pairs, sep='\n')
    print('cbe_list')
    for cbe in cbe_list:
        print('-'*10)
        print(cbe.title)
        print('len', len(cbe.codes))
        for i, code in enumerate(cbe.codes):
            print(i, ':',code[:10])
        # print(cbe.codes, sep='\n')
    return cbe_list

def save_code_blocks_to_files(dirname, cbe_list:list[CodeBlocksExtractor]):
    """Save each code block to a .py file with the title as the file name."""
    # for title, code in cbe_list:
    for cbe in cbe_list:
        title   = cbe.title 
        codes    = cbe.codes
        for i, code in enumerate(codes):
            processed_title = title.replace(' ', '_')  # Create a valid file name
            suffix = '_'+str(i+1) if len(codes) > 1 else ''
            file_name = f".\\{dirname}\\{processed_title}{suffix}.py"
            # os.makedirs(dirname, exist_ok=True)
            os.makedirs(os.path.dirname(file_name), exist_ok=True) 
            # os.makedirs(os.path.dirname(file_path), exist_ok=True) if not os.path.exists(file_path) else open(file_path, 'w').close()
            with open(file_name, 'w', encoding='utf-8') as file:
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
    
    cbe_list = extract_title_code_pairs(md_text)
    file_name, file_extension = get_file_name_8_file_extension(md_file_path)
    save_code_blocks_to_files(dirname=file_name, cbe_list=cbe_list)

if __name__ == "__main__":
    md_file_path = '3.创建型模式.md'  # Change to your Markdown file path
    md_file_path = '4.结构型模式.md'  # Change to your Markdown file path
    md_file_path = '5.行为型模式.md'  # Change to your Markdown file path
    main(md_file_path)
