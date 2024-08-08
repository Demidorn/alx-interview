#!/usr/bin/python3
''' Prime Game '''


def isWinner(x, nums):
    ''' Prime Game '''
    def sieve(n):
        """Return a list of primes up to n."""
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n, primes):
        """Simulate the game for a given n and list of primes."""
        available_numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        for p in primes:
            if p > n:
                break
            if p in available_numbers:
                # Remove p and its multiples
                multiples = set(range(p, n + 1, p))
                available_numbers -= multiples
                # Switch turns
                turn = 1 - turn
        # If turn is 0, it means Ben has no move and Maria wins
        return 'Maria' if turn == 1 else 'Ben'

    if x != len(nums):
        raise ValueError("The length of nums must be equal to x")

    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    # Process each game round
    for n in nums:
        winner = play_game(n, primes)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
