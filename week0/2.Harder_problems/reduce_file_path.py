def reduce_file_path(path):
    path = path.replace('//', '/')
    path = path.split('/')
    reduced_path = []
    for i, item in enumerate(path):
        if item == '..':
            if reduced_path:
                del reduced_path[-1]
        elif item != '.' and item != '':
            reduced_path.append(item)
    return "/".join(reduced_path)


def main():
    print('/' + reduce_file_path("/../"))

if __name__ == '__main__':
    main()


