# Configure hostlists:
def hostlist_conf():

    hostlist_dict = {}

    hostlist_dict["van-dv1"] = ['type_set:juniper_junos', 'van-dv1-dis-1a.ahsv.net', 'van-dv1-dis-1b.ahsv.net', 'van-dv1-dis-2a.ahsv.net',
                    'van-dv1-dis-2b.ahsv.net', 'van-dv1-dis-3b.ahsv.net', 'van-dv1-ge2-1a.ahsv.net',
                    'van-dv1-ge2-3a.ahsv.net', 'van-dv1-ge2-5a.ahsv.net', 'van-dv1-ge2-5b.ahsv.net',
                    'van-dv1-ge2-7a.ahsv.net', 'van-dv1-ge2-8a.ahsv.net', 'van-dv1-ge2-9a.ahsv.net']
    hostlist_dict["van-hc21n"] = ['type_set:juniper_junos', 'van-hc21n-dis-1a.ahsv.net', 'van-hc21n-dis-1b.ahsv.net', 'van-hc21n-ge2-1a.ahsv.net',
                      'van-hc21n-ge2-2a.ahsv.net']
    hostlist_dict["van-hc6b"] = ['type_set:juniper_junos', 'van-hc6b-dis-1a.ahsv.net', 'van-hc6b-dis-2a.ahsv.net']
    hostlist_dict["van-wf375"] = ['type_set:juniper_junos', 'van-wf375-dis-1a.ahsv.net', 'van-wf375-dis-1b.ahsv.net', 'van-wf375-ge2-1b.ahsv.net',
                      'van-wf375-ge2-2b.ahsv.net', 'van-wf375-ge2-3a.ahsv.net']
    hostlist_dict["sea-wb701"] = ['type_set:juniper_junos', 'sea-wb701-dis-1a.ahsv.net', 'sea-wb701-dis-1b.ahsv.net', 'sea-wb701-ge2-1a.ahsv.net',
                      'sea-wb701-ge2-2a.ahsv.net', 'sea-wb701-ge2-7a.ahsv.net', 'sea-wb701-ge2-7b.ahsv.net',
                      'sea-wb701-ge2-8a.ahsv.net', 'sea-wb701-ge2-9a.ahsv.net', 'sea-wb701-ge2-10a.ahsv.net',
                      'sea-wb701-ge2priv-10a.ahsv.net', 'sea-wb701-ge2-13a.ahsv.net', 'sea-wb701-ge2priv-13a.ahsv.net']
    hostlist_dict["sea-wb912"] = ['type_set:juniper_junos', 'sea-wb912-ge2-1a.ahsv.net', 'sea-wb912-ge2priv-1a.ahsv.net']
    hostlist_dict["tor-fr802"] = ['type_set:juniper_junos', 'tor-fr802-dis-1a.ahsv.net', 'tor-fr802-dis-1b.ahsv.net', 'tor-fr802-ge2-1a.ahsv.net',
                      'tor-fr802-ge2-2a.ahsv.net']
    hostlist_dict["mia-89p"] = ['type_set:juniper_junos', 'mia-89p-dis-1a.ahsv.net', 'mia-89p-dis-1b.ahsv.net', 'mia-89p-ge2-1a.ahsv.net',
                    'mia-89p-ge2-2a.ahsv.net']
    hostlist_dict["la-dr425"] = ['type_set:juniper_junos', 'la-dr425-dis-1a.ahsv.net', 'la-dr425-dis-1b.ahsv.net', 'la-dr425-ge2-1a.ahsv.net',
                   'la-dr425-ge2-1b.ahsv.net']
    hostlist_dict["van-cor"] = ['type_set:juniper_junos', 'van-pav-cor-1.ahsv.net', 'van-pav-cor-2.ahsv.net', 'van-val-cor-1.ahsv.net']
    hostlist_dict["sea-cor"] = ['type_set:juniper_junos', 'sea-pav-cor-1.ahsv.net', 'sea-pav-cor-2.ahsv.net', 'sea-prm-ed3-1.ahsv.net',
                          'sea-val-ed3-1.ahsv.net']
    hostlist_dict["tor-cor"] = ['type_set:juniper_junos', 'tor-pav-cor-1.ahsv.net', 'tor-pav-cor-2.ahsv.net', 'tor-val-vmx-2.ahsv.net']
    hostlist_dict["misc"] = ['type_set:juniper_junos', 'cgy-arr-dis-1a.ahsv.net', 'van-wf375-ge2ipay1.ahsv.net', 'van-wg401-ge2-1a.ahsv.net',
                     'sea-infocube-vmx.ahsv.net', 'sea-infocube-sw1.ahsv.net', 'sea-bluespan-vmx.ahsv.net']
    hostlist_dict["hostlist_dynamic_test"] = ['type_set:juniper_junos', 'van-test-dis-1a.ahsv.net', 'type_set:linux', 'van-dv1-mon-1.ahsv.net']

    return hostlist_dict


# Configure common commands:
def command_conf():

    commands = ['show interfaces descriptions', 'show interfaces terse', 'show bgp summary', 'show spanning-tree interface',
                'show arp no-resolve', 'show config', 'show system uptime', 'show route advertising-protocol bgp <input>', 'show route receive-protocol bgp <input>']

    return commands