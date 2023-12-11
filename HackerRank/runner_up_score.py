if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # Sort the list in descending order
    sorted_arr = sorted(arr, reverse=True)

    # Find the runner-up score
    runner_up = None
    for score in sorted_arr:
        if score < max(sorted_arr):
            runner_up = score
            break

    print(runner_up)