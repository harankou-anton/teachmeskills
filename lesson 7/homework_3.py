import csv


def group_by_customers():
    final_data = {}
    with open('data_purchases.csv', 'r') as data:
        read_data = csv.reader(data)
        data_list = list(read_data)
        get_data = data_list[1:]
        for row_data in get_data:
            if row_data[0] not in final_data:
                final_data[row_data[0]] = [int(row_data[2]), int(row_data[3])]
            else:
                final_data[row_data[0]] = [final_data[row_data[0]][0] + int(row_data[2]),
                                           final_data[row_data[0]][1] + int(row_data[3])]

    print(final_data)


def group_by_products():
    final_data = {}
    with open('data_purchases.csv', 'r') as data:
        read_data = csv.reader(data)
        data_list = list(read_data)
        get_data = data_list[1:]
        for row_data in get_data:
            if row_data[1] not in final_data:
                final_data[row_data[1]] = [int(row_data[2]), int(row_data[3])]
            else:
                final_data[row_data[1]] = [final_data[row_data[1]][0] + int(row_data[2]),
                                           final_data[row_data[1]][1] + int(row_data[3])]

    print(final_data)


if __name__ == "__main__":
    group_by_customers()
    group_by_products()
