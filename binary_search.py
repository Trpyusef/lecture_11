import os
import json

cwd_path = os.getcwd()
file_path = "files"


def read_data(file_name, key="ordered_numbers"):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, str), sequential data
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), mode="r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]





def recrusive_binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return recrusive_binary_search(arr, low, mid - 1, x)


        else:
            return recrusive_binary_search(arr, mid + 1, high, x)

    else:
        return -1

def main(file_name, number):
    sequence = read_data(file_name=file_name, key="ordered_numbers")

    # iterative binary search
    arr = [2,3,4,5,6,7,8]
    x = 3
    print(recrusive_binary_search(arr,0 ,len(arr)-1,x))


if __name__ == "__main__":
    my_file = "sequential.json"
    my_number = 90
    main(my_file, my_number)
