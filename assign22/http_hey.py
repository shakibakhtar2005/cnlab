import requests

def http_demo():
    url = "https://httpbin.org/get"
    post_url = "https://httpbin.org/post"

    # GET request
    try:
        response = requests.get(url)
        print("GET Status:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text[:200])  # first 200 chars
    except Exception as e:
        print("GET request failed:", e)

    # POST request
    try:
        data = {"name": "Shakib", "lab": "CN"}
        response = requests.post(post_url, data=data)
        print("\nPOST Status:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text[:200])
    except Exception as e:
        print("POST request failed:", e)

http_demo()
