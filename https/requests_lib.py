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


class RequestsMethods(object):

    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        self.session.max_redirects = 3

    def test_get(self):
        print("Testing requests GET!")
        payload = {"id": [1, 2, 3], "userId": 1}

        try:
            res = self.session.get(self.url, params=payload, timeout=1)            # Execute GET command
            res.raise_for_status()
        except requests.HTTPError as error:
            print(error)
        except requests.exceptions.TooManyRedirects as error:
            print(error)
        except requests.Timeout as error:
            print("Timeout happened!")
            print(error)
            return

        print("Request to URL " + res.url)
        print_response_status(res.status_code)
        print_response_head(res.headers)

        print("Response as Content:")
        print(res.content)
        print("Response as Text:")
        print(res.text)
        print("Response as JSON:")
        for element in res.json():
            print(element)

    def test_post(self):
        print("Testing requests POST!")
        new_data = {
            "userId": 2,
            "id": 1,
            "title": "aii caramba",
            "body": "dont remind me"
        }

        try:
            res = self.session.post(self.url, json=new_data)            # Execute POST command
            res.raise_for_status()
        except requests.HTTPError as error:
            print(error)
        except requests.exceptions.TooManyRedirects as error:
            print(error)

        print_response_status(res.status_code)
        print_response_head(res.headers)
        print("Response as JSON:")
        print(res.json())


def main() -> None:
    exp_url = "https://jsonplaceholder.typicode.com/posts"
    req_examples = RequestsMethods(exp_url)
    req_examples.test_get()
    req_examples.test_post()

    # website_request("https://scotch.io")
    # translation_api()


if __name__ == "__main__":
    main()
