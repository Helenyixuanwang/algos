def isValid( s):
        my_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        
        for p in s:
            #open brackets
            if p in my_dict.keys():
                stack.append(p)
                print("Sth in the stacks: ",stack)
            #closing brackets or other signs
            else:
                #empty stack
                if not stack:
                    print(f"Stack is empty now..., but there are still characters or closing brackets not being compared ===> '{p}'")
                    return False
                else:
                    #if there are characters in the stack
                    p1 = stack.pop()
                    #characters that are not closing brackets, like numbers, other signs that
                    #does not match the values in my_dict
                    print("current iterator IS...",p)
                    print(f"Popped one is '{p1}', Expected closing one is '{my_dict[p1]}'")
                    print("current stack ",stack)
                    if my_dict[p1] != p:
                        print("comparing......")
                        return False
        #after matching, there are extra openning brackets left unpaired
        if stack:
            print("unmatched left in the stacks", stack)
            return False
        print("All matched!!!")
        return True

# print(isValid("{{[[[[(([[[]]]))]]]]}}("))
print(isValid("[]"))