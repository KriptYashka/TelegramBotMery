import requests


def main():
    url = "https://lks.bmstu.ru/schedule/201a4eb8-8610-11ea-a708-005056960017"
    response = requests.get(url)
    print(response)


if __name__ == '__main__':
    main()