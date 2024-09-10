def winner(arr: list[str], n: int) -> tuple:
    votes_count = dict()
    for name in arr:
        if name in votes_count:
            votes_count[name] += 1
        else:
            votes_count[name] = 1
    votes_count = sorted(votes_count.items(), key=lambda x: (-x[1], x[0]))
    winner_name, votes = votes_count[0]
    return winner_name, votes

if __name__ == '__main__':
    names = list(map(str, input('Enter the names list: ').split()))
    ans = winner(names, len(names))
    print(ans)