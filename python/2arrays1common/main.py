# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    df = [[[1, 5, 7, 9, 12, 13, 17],
           [2, 17, 18, 23, 32, 34, 45],
           [3, 5, 11, 33, 34, 36, 45]],
          [[6, 21, 22, 50, 56, 58, 72],
           [7, 5, 12, 13, 55, 56, 74],
           [8, 23, 24, 32, 56, 58, 64]]]

    df2 = [[[100, 5, 12, 15, 27, 32, 54],
            [120, 10, 17, 18, 19, 43, 55],
            [99, 21, 32, 33, 34, 36, 54]],
           [[41, 16, 32, 45, 66, 67, 76],
            [56, 10, 11, 43, 54, 55, 56],
            [77, 12, 16, 18, 19, 21, 23]]]

    output = []
    for i in range(len(df)):
        inner_output = []
        for j in range(len(df[i])):
            common_elements = list(set(df[i][j]) & set(df2[i][j]))
            inner_output.append(common_elements)
        output.append(inner_output)

    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
