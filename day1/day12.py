

if __name__ == '__main__':
    with open('input11.txt', 'r') as reader:
    # with open('sample.txt', 'r') as reader:
        line = reader.read().splitlines()
        data = [int(x) for x in line]

        prev_depth = None
        increments = 0
        sum_increments = []
        temp_increment = []
        for i in range(0, len(data)):
            if i+2 < len(data):
                # print("{},{},{}".format(data[i], data[i+1], data[i+2]))
                sum_depth = data[i] + data[i+1] + data[i+2]
                sum_increments.append(sum_depth)

        for depth in sum_increments:
            # print("depth: {}" .format(depth))
            # print("prevdepth: {}".format(prev_depth))
            if prev_depth is not None:
                if depth - prev_depth > 0:
                    increments += 1
            prev_depth = depth



            # # print("depth: {}" .format(depth))
            # # print("prevdepth: {}".format(prev_depth))
            # if prev_depth is not None:
            #     if depth-prev_depth > 0:
            #         increments += 1
            # prev_depth = depth

        print(increments)