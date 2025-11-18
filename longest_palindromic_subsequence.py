import sys
def longest_palindromic_subsequence(s: str) -> tuple[int, str]:
    return (0, "")

def solve():
    s = sys.stdin.read().strip()
    length, subseq = longest_palindromic_subsequence(s)
    print(length)
    print(subseq)
    
if __name__ == "__main__":
    solve()
