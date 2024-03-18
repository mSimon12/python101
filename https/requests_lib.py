import requests


def print_response_status(status_code: int) -> None:
    if int(status_code/500) > 0:
        print(f"Status {status_code}: Server Error!")
    elif int(status_code/400) > 0:
        print(f"Status {status_code}: Client Error!")
    elif int(status_code/300) > 0:
        print(f"Status {status_code}: Request redirected!")
    elif int(status_code/200) > 0:
        print(f"Status {status_code}: Successful request!")
    elif int(status_code/100) > 0:
        print(f"Status {status_code}: Information!")
    else:
        print("Invalid status code!")


def print_response_head(header: dict) -> None:
    print("HEADER:")
    for key in header:
        print("\t" + key + " : " + header[key])


def save_response_content(filename: str, data) -> int:
    with open(file=filename, mode="w+") as file:
        file.write(data)
    return 0


def website_request(name: str) -> None:
    res = requests.get(name)

    print_response_status(res.status_code)
    print_response_head(dict(res.headers))

    save_response_content("Website Content.html", res.content.__str__())


def main() -> None:
    website_request("https://scotch.io")


if __name__ == "__main__":
    main()
