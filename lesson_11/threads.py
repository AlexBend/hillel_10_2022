from threading import Thread


def get_primes(start: int, end: int):
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    print(results)
    # return results


def run_thread(start: int, end: int):
    pool = (end - start) // 5
    thread_1 = Thread(target=get_primes, args=(start, start + pool))
    thread_2 = Thread(target=get_primes, args=(start + pool, start + pool * 2))
    thread_3 = Thread(target=get_primes, args=(start + pool * 2, start + pool * 3))
    thread_4 = Thread(target=get_primes, args=(start + pool * 3, start + pool * 4))
    thread_5 = Thread(target=get_primes, args=(start + pool * 4, end))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()


def main():
    run_thread(10, 10000)


if __name__ == "__main__":
    main()
