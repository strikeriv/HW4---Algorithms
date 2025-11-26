import sys

def longest_palindromic_subsequence(s: str) -> tuple[int, str]:
    str_length = len(s)
    
    # make the 2d array to store size of 
    sequences: list[list[int]] = [[0] * str_length for _ in range(str_length)]
    split_str = list(s)
    
    # every character ('b', 'a') is a pailndrome. so we set the length to 1
    # required for later steps with DP where we look backwards while backtracing to reconstruct
    for x in range(str_length):
        sequences[x][x] = 1

    # out outer loop handles from 2 -> end of string
    # we start at 2 because of the for loop above and not 1,
    # because of previous loop
    for length in range(2, str_length + 1):
        for x in range(str_length - length + 1):
            # add the two values together, minus 1 because 0 based, for end character
            # (gets index position on other side of split string)
            y = x + length - 1
            
            # now we check if the characters match.
            if split_str[x] == split_str[y]:
                # if they match, we set that palindrome length to 2 + the previous combination
                sequences[x][y] = 2 + sequences[x+1][y-1]
            else:
                # otherwise, not a palindrome, so we carry the max previous resul;t
                sequences[x][y] = max(sequences[x+1][y], sequences[x][y-1])

    # now that we have the sequences, we need to backtrace to construct the sequence
    x, y = 0, str_length - 1
    left: list[str] = []
    right: list[str]  = []
    
    # this loop traverses the split string based on
    # the largest palindrome length. we adjust x & y to always guarentee we are
    # using the largest aplindrome to be backtrace correctly
    while x <= y:
        if split_str[x] == split_str[y]:
            left.append(split_str[x])
            
            # this is to make sure we don't add the middle character
            if x != y:
                right.append(split_str[y])
            x += 1
            y -= 1
        else:
            if sequences[x+1][y] > sequences[x][y-1]:
                x += 1
            else:
                y -= 1

    # join the two parts together to make the palindrome
    subsequence = "".join(left + right[::-1])
    
    return (len(subsequence), subsequence)

def solve():
    s = sys.stdin.read().strip()
    length, subseq = longest_palindromic_subsequence(s)
    print(length)
    print(subseq)
    
if __name__ == "__main__":
    solve()
