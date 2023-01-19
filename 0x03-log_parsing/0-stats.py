#!/usr/bin/python3
"""script that reads line by line from stdin"""
import sys

count = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
total = 0


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if 'Exit' == line.rstrip():
                break
            sample = line
            if len(sample.rstrip().split(" ")) != 9:
                pass
            else:
                if count == 10:
                    print("File size: {}".format(total))
                    for k, v in status.items():
                        if v != 0:
                            print("{}: {}".format(k, v))
                    count = 0
                else:
                    sample = sample.rstrip().split(" ")
                    size = int(sample[8])
                    if sample[7] in status.keys():
                        key = sample[7]
                        status[key] += 1
                        total += size
                        count = count + 1
    except KeyboardInterrupt:
        print("File size: {}".format(total))
        for k, v in status.items():
            if v != 0:
                print("{}: {}".format(k, v))
        raise
