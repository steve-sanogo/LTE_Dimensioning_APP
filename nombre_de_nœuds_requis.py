import PySimpleGUI as sg
from dimensionnement_noeuds_lte import operating_capacity
from signaling_traffic_windows import result
from trafic_total_internet_vpn import buffer
from main_windows import global_parameters
from math import ceil

previous_event = 'Exit'

lte_nodes = {'MME_SAU': 0, 'MME_IDLE_ACTIVE': 0, 'MME_Trans_Second': 0, 'SGW_bearers': 0, 'SGW_BH_DL_Internet': 0,
             'SGW_BH_DL_VPN': 0, 'PGW_bearers': 0, 'PGW_BH_DL_Internet': 0, 'PGW_BH_DL_VPN': 0, 'SGW_PGW_bearers': 0,
             'SGW_PGW_BH_DL_Internet': 0, 'SGW_BH_DL_VPN': 0, 'HSS': 0, 'PCRF': 0
             }


def makeWindowHeader(title):
    header = [
        [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
        [sg.T('', font='any 1')],  # space
        [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
        [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def resultRaw():
    table_header = [[sg.Text('Types de nœud EPC', size=(23, 1)), sg.Text('Nombre requis', size=(23, 1))]]
    display_row = [
                      [sg.Text('N(MME-SAU)', size=(25, 1)), sg.Input(lte_nodes['MME_SAU'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(MME-IDLE/ACTIVE)', size=(25, 1)), sg.Input(lte_nodes['MME_IDLE_ACTIVE'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(MME-Trans/Second)', size=(25, 1)), sg.Input(lte_nodes['MME_Trans_Second'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW-bearers)', size=(25, 1)), sg.Input(lte_nodes['SGW_bearers'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW-BH-DL-Internet)', size=(25, 1)), sg.Input(lte_nodes['SGW_BH_DL_Internet'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW-BH-DL-VPN)', size=(25, 1)), sg.Input(lte_nodes['SGW_BH_DL_VPN'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(PGW-bearers)', size=(25, 1)), sg.Input(lte_nodes['PGW_bearers'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(PGW-BH-DL-Internet)', size=(25, 1)), sg.Input(lte_nodes['PGW_BH_DL_Internet'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(PGW-BH-DL-VPN)', size=(25, 1)), sg.Input(lte_nodes['PGW_BH_DL_VPN'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW/PGW-bearers)', size=(25, 1)), sg.Input(lte_nodes['SGW_PGW_bearers'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW/PGW-BH-DL-Internet)', size=(25, 1)), sg.Input(lte_nodes['SGW_PGW_BH_DL_Internet'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(SGW-BH-DL-VPN)', size=(25, 1)), sg.Input(lte_nodes['SGW_BH_DL_VPN'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(HSS)', size=(25, 1)), sg.Input(lte_nodes['HSS'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                      [sg.Text('N(PCRF)', size=(25, 1)), sg.Input(lte_nodes['PCRF'], size=(13, 1), pad=(0, 0), key='', disabled=True)],
                  ]
    inp = table_header + display_row
    layout = sg.Column([[sg.Frame(title='', layout=inp, relief='sunken', size=(610, 400))]], scrollable=True, vertical_scroll_only=True)
    return [[layout]]


def makeWindowsLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)
    return header + resultRaw() + [[sg.Button('Exit', button_color=('white', 'firebrick3'))]]


def computation():
    lte_nodes['MME_SAU'] = ceil(result['attach'] / operating_capacity['MME'][0])
    lte_nodes['MME_IDLE_ACTIVE'] = ceil(result['idle_to_active'] / 3600 / operating_capacity['MME'][1])
    lte_nodes['MME_Trans_Second'] = ceil(result['total_Procedure'] / 3600 / operating_capacity['MME'][2])
    lte_nodes['SGW_bearers'] = ceil(result['bearers_activ_desactiv'] / operating_capacity['SGW'][0])
    lte_nodes['SGW_BH_DL_Internet'] = ceil(buffer['debit_services_internet_dl'] / operating_capacity['SGW'][1])
    lte_nodes['SGW_BH_DL_VPN'] = ceil(buffer['debit_total_vpn_dl'] / operating_capacity['SGW'][1])
    lte_nodes['PGW_bearers'] = ceil(result['bearers_activ_desactiv'] / operating_capacity['PGW'][0])
    lte_nodes['PGW_BH_DL_Internet'] = ceil(buffer['debit_services_internet_dl'] / operating_capacity['PGW'][1])
    lte_nodes['PGW_BH_DL_VPN'] = ceil(buffer['debit_total_vpn_dl'] / operating_capacity['PGW_value'])
    lte_nodes['SGW_PGW_bearers'] = ceil(result['bearers_activ_desactiv'] / operating_capacity['SGW_PGW'][0])
    lte_nodes['SGW_PGW_BH_DL_Internet'] = ceil(buffer['debit_services_internet_dl'] / operating_capacity['SGW_PGW'][1])
    lte_nodes['SGW_BH_DL_VPN'] = ceil(buffer['debit_total_vpn_dl'] / operating_capacity['SGW_PGW'][1])
    lte_nodes['HSS'] = ceil(int(global_parameters['nb_abonne']) / operating_capacity['HSS'])
    lte_nodes['PCRF'] = ceil(int(result['total_Procedure']) / 3600 / operating_capacity['PCRF'])
    return True


def loadWindows(previousWindows, event):
    if event == 'Nombre De Nœuds Requis':
        windows_title = str(event)  # change windows title
        try:
            computation()
        except:
            sg.popup_error('Something went wrong, Please check Your Entries', title='Error')

        windows = sg.Window('LTE Dimensioning', makeWindowsLayout(windowsTitle=windows_title), size=(700, 500), grab_anywhere=True)
        previousWindows.hide()
        while True:
            compute_event, compute_values = windows.read()

            if compute_event == sg.WIN_CLOSED:
                previousWindows.un_hide()
                windows.close()
                exit()
            elif compute_event == previous_event:
                windows.close()
                previousWindows.un_hide()

                break
    return True