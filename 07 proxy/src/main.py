from file_proxy import FileProxy


def main():
    file_proxy = FileProxy(file_content=dict())

    for i in range(2):
        for j in range(10):
            file_proxy.read(j)


main()
