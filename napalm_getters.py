from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

napalm_results = nr.run(task=napalm_get, getters='arp_table')
# other getters: 'facts', 'interfaces', 'config'

print_result(napalm_results)
print(type(napalm_results))
# ios = napalm_results['facts']
# print_result(ios)
