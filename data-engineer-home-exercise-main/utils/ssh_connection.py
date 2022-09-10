import requests


def call_api(method, url, timeout=30, payload=None, headers=None):
    if payload is None:
        payload = {}
    try:
        response = dict(content=None)
        if method == 'get':
            response = requests.get(url, timeout=timeout, headers=headers)
        elif method == 'put':
            response = requests.put(url, data=payload, headers=headers)
        elif method == 'post':
            response = requests.post(url, timeout=timeout, headers=headers)

        return response
    except requests.exceptions.HTTPError as err:
        message = "Error occurred while calling drift-empty schema: {url}. " \
                  "Error: {e}".format(url=url, e=err)
        raise requests.exceptions.HTTPError(message)

    except requests.exceptions.TooManyRedirects as err:
        message = "Bad URL: {url}" \
                  "Error: {e}".format(url=url, e=err)
        raise requests.exceptions.TooManyRedirects(message)
    except requests.exceptions.RequestException as e:
        message = "Error occurred while calling url: {url}" \
                  "Error: {e}".format(url=url, e=e)
        raise requests.exceptions.RequestException(message)