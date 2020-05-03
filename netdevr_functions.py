def host_compile(hostlist_undict, hostlist_active):

    hostlist_complete = []

    for host in hostlist_active:
        if any(s in hostlist_undict for s in (str(host), 'ALL HOSTS')):
            key_list = list(hostlist_active[str(host)])
            hostlist_complete = hostlist_complete + key_list

    # print(hostlist_complete)
    # exit()

    return hostlist_complete


def host_separator(hostlist_active):

    separator_autopop = ""

    for host in hostlist_active:
        separator_autopop = separator_autopop + ",\n\t\t\t{\n\t\t\t'name': '" + host + "'\n\t\t\t}"

    separator_autopop = separator_autopop + ",\n\t\t\t{\n\t\t\t'name': '" + "ALL HOSTS" + "'\n\t\t\t}"

    separator_provision_head = '''
hostlist_select = [
    {
        'type': 'checkbox',
        'name': 'hostlist_options',
        'message': "Select 1 or more hostlists with [space], continue with [enter]",
        'choices': [
            Separator('= Vancouver =')'''

    separator_provision_tail = '''
        ],
        'validate': lambda answer: 'You must choose at least one hostlist.' \\
                if len(answer) == 0 else True
    }
]'''

    separator_provision = separator_provision_head + separator_autopop + separator_provision_tail

    return(separator_provision)