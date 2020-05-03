# Configure hostlists:
def hostlist_grab():

    hostlist_dict = {}

    hostlist_dict["van-dv1"] = ['van-dv1-dis-1a.ahsv.net', 'van-dv1-dis-1b.ahsv.net', 'van-dv1-dis-2a.ahsv.net',
                    'van-dv1-dis-2b.ahsv.net', 'van-dv1-dis-3b.ahsv.net', 'van-dv1-ge2-1a.ahsv.net',
                    'van-dv1-ge2-3a.ahsv.net', 'van-dv1-ge2-5a.ahsv.net', 'van-dv1-ge2-5b.ahsv.net',
                    'van-dv1-ge2-7a.ahsv.net', 'van-dv1-ge2-8a.ahsv.net', 'van-dv1-ge2-9a.ahsv.net']
    hostlist_dict["van-hc21n"] = ['van-hc21n-dis-1a.ahsv.net', 'van-hc21n-dis-1b.ahsv.net', 'van-hc21n-ge2-1a.ahsv.net',
                      'van-hc21n-ge2-2a.ahsv.net']
    hostlist_dict["van-hc6b"] = ['van-hc6b-dis-1a.ahsv.net', 'van-hc6b-dis-2a.ahsv.net']
    hostlist_dict["van-wf375"] = ['van-wf375-dis-1a.ahsv.net', 'van-wf375-dis-1b.ahsv.net', 'van-wf375-ge2-1b.ahsv.net',
                      'van-wf375-ge2-2b.ahsv.net', 'van-wf375-ge2-3a.ahsv.net']
    hostlist_dict["sea-wb701"] = ['sea-wb701-dis-1a.ahsv.net', 'sea-wb701-dis-1b.ahsv.net', 'sea-wb701-ge2-1a.ahsv.net',
                      'sea-wb701-ge2-2a.ahsv.net', 'sea-wb701-ge2-7a.ahsv.net', 'sea-wb701-ge2-7b.ahsv.net',
                      'sea-wb701-ge2-8a.ahsv.net', 'sea-wb701-ge2-9a.ahsv.net', 'sea-wb701-ge2-10a.ahsv.net',
                      'sea-wb701-ge2priv-10a.ahsv.net', 'sea-wb701-ge2-13a.ahsv.net', 'sea-wb701-ge2priv-13a.ahsv.net']
    hostlist_dict["sea-wb912"] = ['sea-wb912-ge2-1a.ahsv.net', 'sea-wb912-ge2priv-1a.ahsv.net']
    hostlist_dict["tor-fr802"] = ['tor-fr802-dis-1a.ahsv.net', 'tor-fr802-dis-1b.ahsv.net', 'tor-fr802-ge2-1a.ahsv.net',
                      'tor-fr802-ge2-2a.ahsv.net']
    hostlist_dict["mia-89p"] = ['mia-89p-dis-1a.ahsv.net', 'mia-89p-dis-1b.ahsv.net', 'mia-89p-ge2-1a.ahsv.net',
                    'mia-89p-ge2-2a.ahsv.net']
    hostlist_dict["la-dr425"] = ['la-dr425-dis-1a.ahsv.net', 'la-dr425-dis-1b.ahsv.net', 'la-dr425-ge2-1a.ahsv.net',
                   'la-dr425-ge2-1b.ahsv.net']
    hostlist_dict["van-cor"] = ['van-pav-cor-1.ahsv.net', 'van-pav-cor-2.ahsv.net', 'van-val-cor-1.ahsv.net']
    hostlist_dict["sea-cor"] = ['sea-pav-cor-1.ahsv.net', 'sea-pav-cor-2.ahsv.net', 'sea-prm-ed3-1.ahsv.net',
                          'sea-val-ed3-1.ahsv.net']
    hostlist_dict["tor-cor"] = ['tor-pav-cor-1.ahsv.net', 'tor-pav-cor-2.ahsv.net', 'tor-val-vmx-2.ahsv.net']
    hostlist_dict["misc"] = ['cgy-arr-dis-1a.ahsv.net', 'van-wf375-ge2ipay1.ahsv.net', 'van-wg401-ge2-1a.ahsv.net',
                     'sea-infocube-vmx.ahsv.net', 'sea-infocube-sw1.ahsv.net', 'sea-bluespan-vmx.ahsv.net']
    # hostlist_dict["hostlist_dynamic_test"] = ['test.ahsv.net', 'test2.ahsv.net', 'test-test-test.ahsv.net']

    return hostlist_dict

# Configure common commands: