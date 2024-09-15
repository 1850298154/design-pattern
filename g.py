import re

text = "abc"
pattern = r"(a(b((c)))|d(e(f)))"
match = re.match(pattern, text)

if match:
    print("Match Group 0:", match.group(0))  # 这是整个匹配的文本
    print("Match Group 1:", match.group(1))  # 第一个主要捕获组 (a(b(c)) 或 d(e(f)))
    print("Match Group 2:", match.group(2))  # 第二个捕获组 (b(c) 或 None)
    print("Match Group 3:", match.group(3))  # 第三个捕获组 (c 或 None)
    print("Match Group 4:", match.group(4))  # 第四个捕获组 (d(e(f)) 或 None)
    print("Match Group 5:", match.group(5))  # 第五个捕获组 (e(f) 或 None)
    print("Match Group 6:", match.group(6))  # 第六个捕获组 (f 或 None)
    # print("Match Group 6:", match.group(7))  # err

text = "def"
pattern = r"(a(b((c)))|d(e(f)))"
match = re.match(pattern, text)

if match:
    print("Match Group 0:", match.group(0))  # 这是整个匹配的文本
    print("Match Group 1:", match.group(1))  # 第一个主要捕获组 (a(b(c)) 或 d(e(f)))
    print("Match Group 2:", match.group(2))  # 第二个捕获组 (b(c) 或 None)
    print("Match Group 3:", match.group(3))  # 第三个捕获组 (c 或 None)
    print("Match Group 4:", match.group(4))  # 第四个捕获组 (d(e(f)) 或 None)
    print("Match Group 5:", match.group(5))  # 第五个捕获组 (e(f) 或 None)
    print("Match Group 6:", match.group(6))  # 第六个捕获组 (f 或 None)
    print("Match Group 6:", match.group(7))  # err
