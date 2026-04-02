def is_valid(s:str) -> bool:
    # 关于堆栈的应用：括号匹配问题
    # 类似问题都可以用一个字典进行匹配
    bracket_map = {')':'(', '}':'{', ']':'['}
    stack = [] # 假设堆栈是一个列表
    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else '#'
            # 看 bracket_map[char] 是否等于 top
            if bracket_map[char] != top:
                return False
            else:
                stack.append(char)