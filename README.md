# netdevr
A simple network device manager for batch commands and backups.

---

#### Install
```
netDevr requires Python3.5+ already installed.
```
- Download and extract netDevr package to local directory.

- Install pip3 dependencies in Powershell: 'pip3 install progress pyinquirer pyinstaller keyring netmiko' 

- Navigate to netDevr directory and execute with 'python netdevr'

---
#### Help [netdevr -h]

usage: netdevr.py [-h] [-v] [-o OUTPUT] [-s] [-u USERNAME_INLINE] [-p PASSWORD_INLINE] [-c COMMAND_INLINE] [-e]
                  [-d DESTINATION_INLINE] [-l] [-a AUTODETECT]

Options for network_config

optional arguments:
  **-h, --help**            show this help message and exit     
  **-v, --verbose**         enables verbose output      
  **-o OUTPUT, --output OUTPUT**
                        writes output to file     
  **-s, --silence**         silences console output     
  **-u USERNAME_INLINE, --username USERNAME_INLINE**
                        sets username     
  **-p PASSWORD_INLINE, --password PASSWORD_INLINE**
                        sets password     
  **-c COMMAND_INLINE, --command COMMAND_INLINE**
                        sets command      
  **-e, --edit**            sets edit mode, use at own risk     
  **-d DESTINATION_INLINE, --destination DESTINATION_INLINE**
                        sets destination hostlist(s), separate multiple lists with ','      
  **-l, --list**            list all available destination hostlists      
  **-a AUTODETECT, --autodetect AUTODETECT**
                        autodetects device type of specified host     
