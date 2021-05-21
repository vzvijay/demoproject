import requests
import json


class Utils:

    @staticmethod
    def makeRequest(url, data, headers, method, timeout=50):
        method = str(method).upper()

        if method == 'GET':
            r = requests.get(url, headers=headers, verify=False, timeout=timeout)
        elif method == 'POST':
            r = requests.post(url, data=data, headers=headers, verify=False, timeout=timeout)
        elif method == 'DELETE':
            r = requests.delete(url, headers=headers, verify=False, timeout=timeout)
        elif method == 'PUT':
            r = requests.put(url, data=data, headers=headers, verify=False, timeout=timeout)
        elif method == 'PATCH':
            r = requests.patch(url, data=data, headers=headers, verify=False, timeout=timeout)
        else:
            print("Invalid method name:", method)
            raise RuntimeError("Invalid Method:", method)
        return r
