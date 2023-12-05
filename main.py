import requests


def main():
    prompt = input("Pass in some value:")

    with requests.get(f"https://google.com/search?q={prompt}") as response:
        print(response.text)


main()
