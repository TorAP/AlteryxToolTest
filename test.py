import json
import requests

name = "tor@inviso.dk"
password ="Jegerfoedti1996"
contentURL = "Inviso-TorPetersen"

dict = {
"credentials": {
"name": name,
"password": password,
"site": {"contentUrl": contentURL},
}
}

json_object = json.dumps(dict, indent=4)

headers = {"accept": "application/json", "content-type": "application/json"}

# signin_url = "https://{server}/api/{version}/auth/signin".format(server=server_name, version=version)
baseUrl = "https://tableau.inviso.dk"

response = requests.post(
f"{baseUrl}/api/2.8/auth/signin", json_object, headers=headers, verify=True
)
# self.display_error_msg(f"{response}")
response = json.loads(response.content)
# response

token = response["credentials"]["token"]
site_id = response["credentials"]["site"]["id"]

print(site_id)
print(token)