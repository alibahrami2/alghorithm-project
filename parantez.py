def is_valid(s : str) -> bool:
    stack = []

    for char in s:
        if char == "(" or char == "[" or char == "{" :
            stack.append(char)

        elif char == ")" and stack and stack[-1] == "(":
            stack.pop()
        
        elif char == "]" and stack and stack[-1] == "[":
            stack.pop()

        elif char == "}" and stack and stack[-1] == "{":
            stack.pop()

        else:
            return False

    return len(stack) == 0

print(is_valid("()"))

        