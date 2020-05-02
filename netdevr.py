#!/usr/bin/env python3.7
from netdevr_functions import host_compile
from netdevr_config import hostlist_grab
from datetime import date, timedelta
from keyring import get_password
from progress.bar import ShadyBar
from PyInquirer import prompt, Separator
import os, logging, sys, time, argparse, ast, netmiko, getpass


############
##ARGPARSE##
############
parser = argparse.ArgumentParser(description = "Options for network_config")
parser.add_argument("-v", "--verbose", help = "enables verbose output", action="store_true")
parser.add_argument("-o", "--output", help = "writes output to file", action="store", dest="output")
parser.add_argument("-s", "--silence", help = "silences console output", action="store_true")

args = parser.parse_args()


########################
##DIRECTORY MANAGEMENT##
########################
date = str(date.today())
#last_date = date.today() - timedelta(days=1)
#root_dir = "/usr/home/astutebackups/backups/network_backups/"
#save_dir = os.path.join(root_dir, str(date))
#log_dir = (root_dir + "network_backups_" + str(date) + ".log")
#last_log_dir = (root_dir + "network_backups_" + str(last_date) + ".log")

#if not os.path.exists(save_dir):
#    os.mkdir(save_dir)


if args.output is None:
        if args.silence:
                filename = ("netconf_output_" + date + "_0.txt")
                i=0
                while os.path.isfile(filename):
                        filename = ("netconf_output_" + date + "_" + str(i) + ".txt")
                        i+=1
        elif args.silence is False:
                filename = args.output
elif args.output is not None:
        filename = args.output


#####################
##CONFIGURE LOGGING##
#####################
# create logger with 'network_backups'
logger = logging.getLogger('network_backups')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
#fh = logging.FileHandler(log_dir)
#fh.setLevel(logging.DEBUG)

# create console handler with it's own log level
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
#logger.addHandler(fh)
logger.addHandler(ch)

# set time monitor
start_time = time.time()
current_time = time.strftime("%H:%M:%S", time.localtime())

if args.verbose:
        ch.setLevel(logging.DEBUG)
        logger.info("Verbose mode enabled.")
        loader_visual = False
else:
        ch.setLevel(logging.WARNING)
        loader_visual = True

#logger.info("Backup directory set as: " + save_dir)
#logger.info("Log file(s) can be found at " + log_dir)


#########################
##CONFIGURE CREDENTIALS##
#########################
username = input("Enter username: ")
password = getpass.getpass(prompt="Enter password: ", stream=None)

command = input("Enter command or type 'list' for preset options: ")
if command == "list":
        print("list = true")

        command_options = [
                {
                        'type': 'list',
                        'name': 'command_options',
                        'message': 'Select a command with [enter]',
                        'choices': ['show interfaces descriptions', 'show interfaces terse', 'show bgp summary', 'show spanning-tree interface'],
                },
        ]

        command_dict = prompt(command_options)
        command = command_dict.get("command_options")

logger.info("Command has been set as: " + command)


####################
##CREATE HOSTLISTS##
####################

hostlist_active = hostlist_grab()

logger.info(hostlist_active)


# hostlist_dv1 = ['van-dv1-dis-1a.ahsv.net', 'van-dv1-dis-1b.ahsv.net', 'van-dv1-dis-2a.ahsv.net', 'van-dv1-dis-2b.ahsv.net', 'van-dv1-dis-3b.ahsv.net', 'van-dv1-ge2-1a.ahsv.net', 'van-dv1-ge2-3a.ahsv.net', 'van-dv1-ge2-5a.ahsv.net', 'van-dv1-ge2-5b.ahsv.net', 'van-dv1-ge2-7a.ahsv.net', 'van-dv1-ge2-8a.ahsv.net', 'van-dv1-ge2-9a.ahsv.net']
# hostlist_hc21n = ['van-hc21n-dis-1a.ahsv.net', 'van-hc21n-dis-1b.ahsv.net', 'van-hc21n-ge2-1a.ahsv.net', 'van-hc21n-ge2-2a.ahsv.net']
# hostlist_hc6b = ['van-hc6b-dis-1a.ahsv.net', 'van-hc6b-dis-2a.ahsv.net']
# hostlist_wf375 = ['van-wf375-dis-1a.ahsv.net', 'van-wf375-dis-1b.ahsv.net', 'van-wf375-ge2-1b.ahsv.net', 'van-wf375-ge2-2b.ahsv.net', 'van-wf375-ge2-3a.ahsv.net']
# hostlist_wb701 = ['sea-wb701-dis-1a.ahsv.net', 'sea-wb701-dis-1b.ahsv.net', 'sea-wb701-ge2-1a.ahsv.net', 'sea-wb701-ge2-2a.ahsv.net', 'sea-wb701-ge2-7a.ahsv.net', 'sea-wb701-ge2-7b.ahsv.net', 'sea-wb701-ge2-8a.ahsv.net', 'sea-wb701-ge2-9a.ahsv.net', 'sea-wb701-ge2-10a.ahsv.net', 'sea-wb701-ge2priv-10a.ahsv.net', 'sea-wb701-ge2-13a.ahsv.net', 'sea-wb701-ge2priv-13a.ahsv.net']
# hostlist_wb912 = ['sea-wb912-ge2-1a.ahsv.net', 'sea-wb912-ge2priv-1a.ahsv.net']
# hostlist_fr802 = ['tor-fr802-dis-1a.ahsv.net', 'tor-fr802-dis-1b.ahsv.net', 'tor-fr802-ge2-1a.ahsv.net', 'tor-fr802-ge2-2a.ahsv.net']
# hostlist_mia = ['mia-89p-dis-1a.ahsv.net', 'mia-89p-dis-1b.ahsv.net', 'mia-89p-ge2-1a.ahsv.net', 'mia-89p-ge2-2a.ahsv.net']
# hostlist_la = ['la-dr425-dis-1a.ahsv.net', 'la-dr425-dis-1b.ahsv.net', 'la-dr425-ge2-1a.ahsv.net', 'la-dr425-ge2-1b.ahsv.net']
# hostlist_van_cores = ['van-pav-cor-1.ahsv.net', 'van-pav-cor-2.ahsv.net', 'van-val-cor-1.ahsv.net']
# hostlist_sea_cores = ['sea-pav-cor-1.ahsv.net', 'sea-pav-cor-2.ahsv.net', 'sea-prm-ed3-1.ahsv.net', 'sea-val-ed3-1.ahsv.net']
# hostlist_tor_cores = ['tor-pav-cor-1.ahsv.net', 'tor-pav-cor-2.ahsv.net', 'tor-val-vmx-2.ahsv.net']
# hostlist_misc = ['cgy-arr-dis-1a.ahsv.net', 'van-wf375-ge2ipay1.ahsv.net', 'van-wg401-ge2-1a.ahsv.net', 'sea-infocube-vmx.ahsv.net', 'sea-infocube-sw1.ahsv.net', 'sea-bluespan-vmx.ahsv.net']

#hostlist_options = [
#       inquirer.Checkbox('Hostlists', message="Select 1 or more hostlists for command deployment",
#               choices=['hostlist_dv1', 'hostlist_hc21n', 'hostlist_hc6b', 'hostlist_wf375', 'hostlist_wb701', 'hostlist_wb912',
#               'hostlist_tor', 'hostlist_mia', 'hostlist_la', 'hostlist_van_cores', 'hostlist_sea_cores', 'hostlist_tor_cores',
#               'hostlist_misc']),
#]
#hostlist_select = inquirer.prompt(hostlist_options)

hostlist_select = [
    {
        'type': 'checkbox',
        'name': 'hostlist_options',
        'message': "Select 1 or more hostlists with [space], continue with [enter]",
        'choices': [
                Separator('= Vancouver ='),
                {
                'name': 'hostlist_dv1'
                },
                {
                'name': 'hostlist_hc21n'
                },
                {
                'name': 'hostlist_hc6b',
                },
                {
                'name': 'hostlist_wf375'
                },
                {
                'name': 'hostlist_van_cores'
                },
                Separator('= Seattle ='),
                {
                'name': 'hostlist_wb701'
                },
                {
                'name': 'hostlist_wb912'
                },
                {
                'name': 'hostlist_sea_cores'
                },
                Separator('= Toronto ='),
                {
                'name': 'hostlist_fr802'
                },
                {
                'name': 'hostlist_tor_cores'
                },
                Separator('= Miami ='),
                {
                'name': 'hostlist_mia'
                },
                Separator('= Los Angeles ='),
                {
                'name': 'hostlist_la'
                },
                Separator('= Customer & Misc ='),
                {
                'name': 'hostlist_misc'
                },
                Separator('= APPLY ALL ='),
                {
                'name': 'hostlist_complete'
                }
        ],
        'validate': lambda answer: 'You must choose at least one hostlist.' \
                if len(answer) == 0 else True
    }
]

hostlist_selected = prompt(hostlist_select)
hostlist_undict = hostlist_selected["hostlist_options"]
hostlist_len = len(hostlist_selected["hostlist_options"])

#hostlist_complete = []

hostlist_complete = host_compile(hostlist_undict, hostlist_active)
#hostlist_complete = host_compile(hostlist_undict, hostlist_dv1, hostlist_fr802, hostlist_hc6b, hostlist_hc21n, hostlist_la, hostlist_mia, hostlist_misc, hostlist_wb701, hostlist_wb912, hostlist_sea_cores, hostlist_tor_cores, hostlist_van_cores, hostlist_wf375)

# if any(s in hostlist_undict for s in ('hostlist_dv1', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_dv1
# if any(s in hostlist_undict for s in ('hostlist_hc21n', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_hc21n
# if any(s in hostlist_undict for s in ('hostlist_hc6b', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_hc6b
# if any(s in hostlist_undict for s in ('hostlist_wf375', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_wf375
# if any(s in hostlist_undict for s in ('hostlist_wb701', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_wb701
# if any(s in hostlist_undict for s in ('hostlist_wb912', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_wb912
# if any(s in hostlist_undict for s in ('hostlist_fr802', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_fr802
# if any(s in hostlist_undict for s in ('hostlist_mia', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_mia
# if any(s in hostlist_undict for s in ('hostlist_la', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_la
# if any(s in hostlist_undict for s in ('hostlist_van_cores', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_van_cores
# if any(s in hostlist_undict for s in ('hostlist_sea_cores', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_sea_cores
# if any(s in hostlist_undict for s in ('hostlist_tor_cores', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_tor_cores
# if any(s in hostlist_undict for s in ('hostlist_misc', 'hostlist_complete')):
#         hostlist_complete = hostlist_complete + hostlist_misc

logger.info("Outputting to selected hostlist(s)...")
logger.info(hostlist_undict)
logger.info("Outputting to selected host(s)...")
logger.info(hostlist_complete)


########################################
##ADD/REMOVE ACTIONABLE HOSTLISTS HERE##
########################################
# initiate progress bar
if args.silence:
        bar = ShadyBar('Processing', max=(len(hostlist_complete)))

for host in hostlist_complete:

#       if loader_visual == True:
#               bar.next()

        junos1 = {
                "device_type": "juniper_junos",
                "host": host,
                "username": username,
                "password": password,
                "global_delay_factor": 2,
        }

#       filename = (save_dir + "/" + host + "_" + str(date) + ".txt")

        net_connect = netmiko.Netmiko(**junos1)
        output = net_connect.send_command(command)

        if args.silence:
                bar.next()
        else:
                print()
                print("-------=====================-------")
                print()

                print(net_connect.find_prompt())
                print("> " + command)
                print(output)

        if filename is not None:
                with open(filename, "a") as f:
                        print(file=f)
                        print("-------=====================-------", file=f)
                        print(file=f)
                        print(net_connect.find_prompt(), file=f)
                        print("> " + command, file=f)
                        print(output, file=f)
                net_connect.disconnect()

if filename is not None:
        logger.info("Output written to " + filename)

if args.silence:
        bar.finish()

# calculate and output run time
logger.info("Task completed in %.2f minutes!" % ((time.time() - start_time)/60))