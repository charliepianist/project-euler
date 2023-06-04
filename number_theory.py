from collections import defaultdict

def gen_primes_up_to(n):
    """ Generate all primes <= n """
    nums = list(range(1, int(n)+1))
    is_prime = [True for num in nums]
    is_prime[0] = False

    for i in range(len(nums)):
        if is_prime[i]:
            for j in range(i+nums[i], len(nums), nums[i]):
                is_prime[j] = False

    primes = []
    for i in range(len(nums)):
        if is_prime[i]:
            primes.append(nums[i])
    return primes

def factorize(x, primes):
    """ Factorize x using the primes in the list primes. """
    if x == 0 or x == 1:
        return {}
    
    orig_x = x
    i = 0
    factorization = defaultdict(lambda : 0)

    while x > 1 and i < len(primes):
        if x % primes[i] == 0:
            factorization[primes[i]] += 1
            x //= primes[i]
        else:
            i += 1

    if x != 1:
        raise Exception(f'could not factor {orig_x} (left with {x}); largest prime was {primes[-1]}')
    return factorization

def unfactorize(factorization):
    """ Reconstruct x given its factorization """
    prod = 1
    for p in factorization:
        prod *= p**factorization[p]
    return prod

def sum_divisors(factorization):
    """ Compute the sum of the divisors for a given factorization """
    prod = 1

    for p in factorization:
        s = 1
        term = 1
        for power in range(1, factorization[p] + 1):
            term *= p
            s += term
        prod *= s
    
    return prod