# netdevr
An expanded version of netbackup with improved functionality for batch commands and backups.

---

### Install
```
netDevr requires Python3.5+
```
- Download and extract netDevr package to local directory.

- Install pip3 dependencies in Powershell: `pip3 install progress pyinquirer pyinstaller keyring netmiko`   

- Navigate to netDevr directory and execute with `python netdevr`

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



#### Supported platforms:
a10: A10SSH,  
accedian: AccedianSSH,    
alcatel_aos: AlcatelAosSSH,   
alcatel_sros: AlcatelSrosSSH,   
arista_eos: AristaSSH,    
aruba_os: ArubaSSH,   
avaya_ers: AvayaErsSSH,   
avaya_vsp: AvayaVspSSH,   
brocade_fastiron: BrocadeFastironSSH,   
brocade_netiron: BrocadeNetironSSH,   
brocade_nos: BrocadeNosSSH,   
brocade_vdx: BrocadeNosSSH,   
brocade_vyos: VyOSSSH,    
checkpoint_gaia: CheckPointGaiaSSH,   
ciena_saos: CienaSaosSSH,   
cisco_asa: CiscoAsaSSH,   
cisco_ios: CiscoIosBase,    
cisco_nxos: CiscoNxosSSH,   
cisco_s300: CiscoS300SSH,   
cisco_tp: CiscoTpTcCeSSH,   
cisco_wlc: CiscoWlcSSH,   
cisco_xe: CiscoIosBase,   
cisco_xr: CiscoXrSSH,   
dell_force10: DellForce10SSH,   
dell_powerconnect: DellPowerConnectSSH,   
eltex: EltexSSH,    
enterasys: EnterasysSSH,    
extreme: ExtremeSSH,    
extreme_wing: ExtremeWingSSH,   
f5_ltm: F5LtmSSH,   
fortinet: FortinetSSH,    
generic_termserver: TerminalServerSSH,    
hp_comware: HPComwareSSH,   
hp_procurve: HPProcurveSSH,   
huawei: HuaweiSSH,    
juniper: JuniperSSH,    
juniper_junos: JuniperSSH,    
linux: LinuxSSH,    
mellanox_ssh: MellanoxSSH,    
mrv_optiswitch: MrvOptiswitchSSH,   
ovs_linux: OvsLinuxSSH,     
paloalto_panos: PaloAltoPanosSSH,   
pluribus: PluribusSSH,    
quanta_mesh: QuantaMeshSSH,   
ubiquiti_edge: UbiquitiEdgeSSH,   
vyatta_vyos: VyOSSSH,   
vyos: VyOSSSH   
