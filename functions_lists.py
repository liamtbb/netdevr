def host_compile():
    if any(s in hostlist_undict for s in ('hostlist_dv1', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_dv1
    if any(s in hostlist_undict for s in ('hostlist_hc21n', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_hc21n
    if any(s in hostlist_undict for s in ('hostlist_hc6b', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_hc6b
    if any(s in hostlist_undict for s in ('hostlist_wf375', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_wf375
    if any(s in hostlist_undict for s in ('hostlist_wb701', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_wb701
    if any(s in hostlist_undict for s in ('hostlist_wb912', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_wb912
    if any(s in hostlist_undict for s in ('hostlist_fr802', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_fr802
    if any(s in hostlist_undict for s in ('hostlist_mia', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_mia
    if any(s in hostlist_undict for s in ('hostlist_la', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_la
    if any(s in hostlist_undict for s in ('hostlist_van_cores', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_van_cores
    if any(s in hostlist_undict for s in ('hostlist_sea_cores', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_sea_cores
    if any(s in hostlist_undict for s in ('hostlist_tor_cores', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_tor_cores
    if any(s in hostlist_undict for s in ('hostlist_misc', 'hostlist_complete')):
            hostlist_complete = hostlist_complete + hostlist_misc