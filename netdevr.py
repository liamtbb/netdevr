#!/usr/bin/env python3.7
from netdevr_functions import host_compile, host_separator
from netdevr_config import hostlist_conf, command_conf
from datetime import date, timedelta
from keyring import get_password
from progress.bar import ShadyBar
from PyInquirer import prompt, Separator
import os, logging, sys, time, argparse, ast, netmiko, getpass


# argument parsing
parser = argparse.ArgumentParser(description = "Options for network_config")
parser.add_argument("-v", "--verbose", help = "enables verbose output", action="store_true")
parser.add_argument("-o", "--output", help = "writes output to file", action="store", dest="output")
parser.add_argument("-s", "--silence", help = "silences console output", action="store_true")
parser.add_argument("-u", "--username", help = "sets username", action="store", dest="username_inline")
parser.add_argument("-p", "--password", help = "sets password", action="store", dest="password_inline")
parser.add_argument("-c", "--command", help = "sets command", action="store", dest="command_inline")
parser.add_argument("-e", "--edit", help = "sets edit mode, use at own risk", action="store_true")
parser.add_argument("-d", "--destination", help = "sets destination hostlist(s), separate multiple lists with ',' e.g. <list1>,<list2>", action="store", dest="destination_inline")
parser.add_argument("-l", "--list", help = "list all available destination hostlists", action="store_true")

args = parser.parse_args()

if args.list:
        print("Configured hostlists:\n")
        for key in hostlist_conf():
                print(key + ":\n" + str(hostlist_conf()[key]) + "\n")
        exit("\n")


# directory management
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


# logging setup
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


# credentials acquisition
if args.username_inline is not None:
        username = args.username_inline
else:
        username = input("Enter username: ")

if args.password_inline is not None:
        password = args.password_inline
else:
        password = getpass.getpass(prompt="Enter password: ", stream=None)


# command input
if args.command_inline is not None:
        command = args.command_inline
        if args.edit:
                edit_mode = True
        elif args.edit == False:
                edit_mode = False
else:
        command = input("Enter command or type 'list' for preset options, or 'edit' to make config change: ")

        if command == "list":
                command_options = [
                        {
                                'type': 'list',
                                'name': 'command_options',
                                'message': 'Select a command with [enter]',
                                'choices': command_conf(),
                        },
                ]

                command_dict = prompt(command_options)
                command = command_dict.get("command_options")
                edit_mode = False

                logger.info("Command has been set as: " + command)
        elif command == "edit":
                edit_mode = True
                command = input("Enter edit command: ")

                logger.info("Edit command has been set as: " + command)
        else:
                edit_mode = False

# hostlist compiling and dynamic list creation
hostlist_active = hostlist_conf()

if args.destination_inline is None:
        separator_autopop = host_separator(hostlist_active)

        exec(separator_autopop)

        hostlist_selected = prompt(hostlist_select)
        hostlist_undict = hostlist_selected["hostlist_options"]
else:
        hostlist_undict = list(args.destination_inline.split(","))

hostlist_complete = host_compile(hostlist_undict, hostlist_active)

logger.info("Outputting to selected hostlist(s)...")
logger.info(hostlist_undict)
logger.info("Outputting to selected host(s)...")
logger.info(hostlist_complete)


# initiate progress bar
if args.silence:
        bar = ShadyBar('Processing', max=(len(hostlist_complete)))

for host in hostlist_complete:

        # for key in hostlist_active:
        #         if host in hostlist_active[key]:
        #                 device_type = "juniper_junos"

        if host == 'juniper':
                device_type = "juniper_junos"
                print("The device type has been set to: " + device_type)
                continue
        if host == 'cisco':
                device_type = "cisco_ios"
                print("The device type has been set to: " + device_type)
                continue
        if host == 'linux':
                device_type = "linux"
                print("The device type has been set to: " + device_type)
                continue

        device = {
                "device_type": "autodetect",
                "host": host,
                "username": username,
                "password": password,
                "global_delay_factor": 2,
        }

        # guesser = netmiko.SSHDetect(**device)
        # best_match = guesser.autodetect()
        # print(best_match)  # Name of the best device_type to use further
        # print(guesser.potential_matches)  # Dictionary of the whole matching result
        # exit()
        #
        # device["device_type"] = best_match
        device["device_type"] = device_type

        net_connect = netmiko.Netmiko(**device)
        if edit_mode is False:
                output = net_connect.send_command(command)
        elif edit_mode is True:
                output = net_connect.send_config_set(command)
                output = net_connect.send_config_set("commit and-quit")

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