import PySimpleGUI as sg
from main_windows import global_parameters
from dataCards_smartphones_trafic import dataCardResult, smartPhoneResult
from math import ceil
choice, previous_event = '', 'Exit'
gb_factor = 1000000

buffer = {'trafic_total_smartphones': 0, 'trafic_total_dataCards': 0, 'trafic_total': 0, 'debit_internet_hc': 0, 'nb_dataCards_utilisant_vpn': 0, 'trafic_total_vpn': 0}


def setSomeParams():
    trafic_total_smartphones = int(global_parameters['nbSmartPhone']) * float(smartPhoneResult['trafic_total_DL']) / gb_factor
    trafic_total_dataCards = int(global_parameters['nbDataCard']) * float(dataCardResult['trafic_total_DL']) / gb_factor
    trafic_total = trafic_total_smartphones + trafic_total_dataCards
    debit_services_internet_dl = trafic_total * 8 * 1000 / 3600
    nb_dataCards_utilisant_vpn = ceil(int(global_parameters['nbDataCard']) * float(global_parameters['datacard_vpn_pct']))
    trafic_total_vpn = nb_dataCards_utilisant_vpn * float(dataCardResult['vpn'][1]) / gb_factor
    debit_total_vpn_dl = trafic_total_vpn * 8 * 1000 / 3600
    return debit_services_internet_dl, debit_total_vpn_dl


def makeWindowHeader(title):
    header = [
        [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
        [sg.T('', font='any 1')],  # space
        [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
        [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def TotalTrafficResult():
    table_header = [[sg.Text('Désignation', size=(35, 1)), sg.Text('Trafic total à HC pour Internet', size=(23, 1))]]
    display_row = [
                      [[sg.Text('Volume Trafic Total pour tous les smartphones(Gb)', size=(40, 1))] + [sg.Input(buffer['trafic_total_smartphones'], size=(13, 1), pad=(0, 0), key='trafic_total_smartphones', disabled=True) ]],
                      [[sg.Text('Volume Trafic Total pour les cartes de données(Gb)', size=(40, 1))] + [sg.Input(buffer['trafic_total_dataCards'], size=(13, 1), pad=(0, 0), key='trafic_total_dataCards', disabled=True)]],
                      [[sg.Text('Volumes de Trafic total(Gb)', size=(40, 1))] + [sg.Input(buffer['trafic_total'], size=(13, 1), pad=(0, 0), key='trafic_total', disabled=True)]],
                      [[sg.Text('Débit Internet à HC-UL/DL(Gbits/s)', size=(40, 1))] + [sg.Input(buffer['debit_internet_hc'], size=(13, 1), pad=(0, 0), key='debit_internet_hc', disabled=True)]],
                      [[sg.Text('Data Card(Cartes de données) utilisant VPN', size=(40, 1))] + [sg.Input(buffer['nb_dataCards_utilisant_vpn'], size=(13, 1), pad=(0, 0), key='nb_dataCards_utilisant_vpn', disabled=True)]],
                      [[sg.Text('Trafic Total pour VPN(Gb)', size=(40, 1))] + [sg.Input(buffer['trafic_total_vpn'], size=(13, 1), pad=(0, 0), key='trafic_total_vpn', disabled=True)]],
                      [[sg.Text('Débit Total VPN(data card) (Gbits/s)', size=(40, 1))] + [sg.Input(buffer['debit_total_vpn'], size=(13, 1), pad=(0, 0), key='debit_total_vpn', disabled=True)]],
                      [[sg.Button('Exit', button_color=('white', 'firebrick3'))]]
                  ]
    return table_header + display_row


def makeWindowsLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)

    return header + TotalTrafficResult()


def computation():
    global choice
    buffer['trafic_total_smartphones'] = int(global_parameters['nbSmartPhone']) * float(smartPhoneResult['trafic_total_UL_DL' if choice =='both' else 'trafic_total_DL']) / gb_factor
    buffer['trafic_total_dataCards'] = int(global_parameters['nbDataCard']) * float(dataCardResult['trafic_total_UL_DL' if choice =='both' else 'trafic_total_DL']) / gb_factor
    buffer['trafic_total'] = float(buffer['trafic_total_smartphones']) + float(buffer['trafic_total_dataCards'])
    buffer['debit_internet_hc'] = float(buffer['trafic_total'])*8*1000/3600
    buffer['nb_dataCards_utilisant_vpn'] = ceil(int(global_parameters['nbDataCard']) * float(global_parameters['datacard_vpn_pct']))
    buffer['trafic_total_vpn'] = int(buffer['nb_dataCards_utilisant_vpn']) * float(dataCardResult['vpn'][0 if choice =='both' else 1]) / gb_factor
    buffer['debit_total_vpn'] = float(buffer['trafic_total_vpn'])*8*1000/3600
    buffer['debit_services_internet_dl'], buffer['debit_total_vpn_dl'] = setSomeParams()
    return True


def loadWindows(previousWindows, event):
    global choice
    windows_title = 'Trafic ' + str(event)  # change windows title
    if event == 'Trafic Total VPN et Internet à HC en DL et UL':
        choice = 'both'
        computation()
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

    elif event == 'Trafic total VPN et Internet à HC en DL':
        choice = 'DL'
        computation()
        windows = sg.Window('LTE Dimensioning', makeWindowsLayout(windowsTitle=windows_title), size=(700, 500), grab_anywhere=True)
        previousWindows.hide()
        while True:
            compute_event, compute_values = windows.read()

            if compute_event == sg.WIN_CLOSED:
                previousWindows.un_hide()
                windows.close()
                exit()
            elif compute_event == previous_event:
                previousWindows.un_hide()
                windows.close()
                break
    return True

