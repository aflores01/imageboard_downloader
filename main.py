import os
import requests


def download(resource_url):
    file = requests.get(resource_url)
    open("images/" + resource_url.rsplit('/', 1)[1], "wb").write(file.content)


def create_dir():
    try:
        os.mkdir("images")
    except Exception as ex:
        print(f"directory already exists {ex}")


def url_validation(site):
    if not site.find("http://"):
        return site
    else:
        return "http://" + site


if __name__ == '__main__':
    print("Danbooru image board engine downloader")
    create_dir()
    print("Enter site running danbooru image board engine:")
    url = input()
    site_url = url_validation(url)
    print(f"Using: {site_url}")
    print("Enter download limit <200")
    limit = input()
    print("Enter keywords separated by space: (Support wildcard: * )")
    search = input()
    api_url = requests.get(site_url + "/posts.json?tags=" + search + "&limit=" + limit)
    print(f"Response: {api_url}")

    for image in api_url.json():
        try:
            print(image['id'])
            print(image['large_file_url'])
            download(image['large_file_url'])
        except Exception as e:
            print("post does not contain ID or its banned")
            print(e)
