import jsonpath
import requests

from hogwarts_httprunner.loader import load_yaml

def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)

def runn_yaml(yaml_file):
    load_yaml = load_yaml(yaml_file)

    request = load_json["request"]

    method = request.pop("method")
    url = request.pop("url")
    resp = requests.request(method, url ,**request)

    validator_mapping = load_json["validate"]

    for key, value in validator_mapping.items():
        if "$" in key:
            actual_value = expected_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)  # resp.key
        expected_value = validator_mapping[key]

        assert actual_value == expected_value
    return True

def run_api_yaml():
    pass