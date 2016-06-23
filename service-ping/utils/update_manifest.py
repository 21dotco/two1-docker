import os
import re
import yaml

manifest_path = '/usr/src/app/manifest.yaml'
ipv6_pattern = re.compile(r"""\[(?P<ipv6_addr>(\w{4}:){7}\w{4})\]:(?P<port>\d*)$""")
matches = ipv6_pattern.search(os.environ['PAYMENT_SERVER_IP'])
zt_ip = matches.group('ipv6_addr')
port = matches.group('port')

with open(manifest_path, "r") as f:
    manifest_json = yaml.load(f)

service = os.environ['SERVICE']
manifest_json["basePath"] = "/%s" % service
manifest_json["host"] = "[%s]:%s" % (zt_ip, port)
try:
    manifest_json["info"]["x-21-quick-buy"] = manifest_json["info"]["x-21-quick-buy"] % (zt_ip, port, service)
except:
    pass

with open(manifest_path, "w") as f:
    yaml.dump(manifest_json, f)
