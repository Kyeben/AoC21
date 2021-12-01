if __name__ == '__main__':
    with open('input11.txt', 'r') as reader:
        line = reader.read().splitlines()
        data = [int(x) for x in line]

        prev_depth = None
        increments = 0
        for depth in data:
            if prev_depth is not None:
                if depth-prev_depth > 0:
                    increments += 1
            prev_depth = depth

        print(increments)
