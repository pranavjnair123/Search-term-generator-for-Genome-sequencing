import time
words=set()
def neighbor(pattern, d):
    global words
    if d == 0:
        words.add(pattern)
    else:
        bases = ['A', 'T', 'C', 'G']
        for i in range(len(pattern)):
            for j in range(len(bases)):
                new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
                if d <= 1:
                    words.add(new_pattern)
                else:
                    neighbor(new_pattern, d-1)


start_time=time.time()


neighbor("ACG",2)
print("Neighbours found (recursive method)")

print(words)

print("--- %s seconds ---" % (time.time() - start_time))
