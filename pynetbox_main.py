import pynetbox
from rich import print, inspect

credentials = {
    "url": "https://demo.netbox.dev",
    "username": "mitest",
    "password": "mitest",
}

nb = pynetbox.api(
    url=credentials["url"],
    token="13cb2dde220086944e56729186c45e546c6eee65",
    threading=True,
)

# token = nb.create_token(
# username=credentials["username"], password=credentials["password"]
# )

devices = nb.dcim.devices.all()
print(f'\n{type(devices)=}\n')
print('\n', dir(devices))
print('\ndevices.__dict__:', devices.__dict__)
