import sys


def print_progress_bar(
        iteration: int,
        total: int,
        bar_length: int=30,
        prefix='',
        filled='#',
        unfilled=' ',
        caps='[]'):
    if len(caps) == 0:
        lcap, rcap = '', ''
    elif len(caps) == 1:
        lcap, rcap = caps, caps
    else:
        lcap, rcap = caps[0], caps[1]

    n = int((iteration / total) * bar_length)

    print("\r{}{}{}{}{}".format(prefix, lcap, n * filled, (bar_length - n) * unfilled, rcap), end='', flush=True)


if __name__ == "__main__":
    print("Doing nothing...")
    
    N = 50_000
    for i in range(N):
        print_progress_bar(i, N)
    print_progress_bar(N, N)
    print()

    print("Finished!")