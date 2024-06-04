def is_palindrome(str):
    start_index =0
    end_index = len(str) - 1
    for _ in str:
        if str[start_index] != str[end_index] :
            return False
    return True

print(is_palindrome('racecar'))
print(is_palindrome('racecars'))