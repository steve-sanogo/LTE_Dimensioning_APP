import PySimpleGUI as sg
from trafic_total_internet_vpn import buffer
from math import ceil

previous_event, delete_event, compute_vent = 'Exit', 'Reset', 'Compute'

# Results dictionary
S1U_interface_result = {'overhead_per_packet': 0, 'packet_size': 0,  'overhead': 0, 'debit_services_internet': 0, 'debit_service_VPN': 0, 'debit_total': 0}
S5_interface_result = {'overhead_per_packet': 0, 'packet_size': 0, 'overhead': 0, 'debit_services_internet': 0, 'debit_service_VPN': 0, 'debit_total': 0}
SGi_interface_result = {'overhead_per_packet': 0, 'packet_size': 0, 'overhead': 0, 'debit_services_internet': 0, 'debit_service_VPN': 0, 'debit_total': 0}


def makeWindowHeader(title):
    header = [
                [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
                [sg.T('', font='any 1')],  # space
                [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
                [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def signalingInputRaw():

    S1U = [
        [sg.Text('Overhead par paquet (octets)', size=(17, 2)), sg.Input(key='S1U_overhead_per_packet', size=(13, 1))],
        [sg.Text('Taille paquet', size=(17, 1)), sg.Input(key='S1U_packet_size', size=(13, 1))],
        [sg.Text('Overhead', size=(17, 2)), sg.Input(key='S1U_overhead', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour les services Internet', size=(17, 2)), sg.Input(key='S1U_debit_services_internet', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour le service VPN', size=(17, 2)),  sg.Input(key='S1U_debit_service_VPN', size=(13, 1), disabled=True)],
        [sg.Text('Débit total', size=(17, 2)), sg.Input(key='S1U_debit_total', size=(13, 1), disabled=True)],

    ]

    S5 = [
        [sg.Text('Overhead par paquet (octets)', size=(17, 2)), sg.Input(key='S5_overhead_per_packet', size=(13, 1))],
        [sg.Text('Taille paquet', size=(17, 1)), sg.Input(key='S5_packet_size', size=(13, 1))],
        [sg.Text('Overhead', size=(17, 2)), sg.Input(key='S5_overhead', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour les services Internet', size=(17, 2)), sg.Input(key='S5_debit_services_internet', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour le service VPN', size=(17, 2)), sg.Input(key='S5_debit_service_VPN', size=(13, 1), disabled=True)],
        [sg.Text('Débit total', size=(17, 2)), sg.Input(key='S5_debit_total', size=(13, 1), disabled=True)],
    ]

    SGi = [
        [sg.Text('Overhead par paquet (octets)', size=(17, 2)), sg.Input(key='SGi_overhead_per_packet', size=(13, 1))],
        [sg.Text('Taille paquet', size=(17, 1)), sg.Input(key='SGi_packet_size', size=(13, 1))],
        [sg.Text('Overhead', size=(17, 2)), sg.Input(key='SGi_overhead', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour les services Internet', size=(17, 2)), sg.Input(key='SGi_debit_services_internet', size=(13, 1), disabled=True)],
        [sg.Text('Debit pour le service VPN', size=(17, 2)), sg.Input(key='SGi_debit_service_VPN', size=(13, 1), disabled=True)],
        [sg.Text('Débit total', size=(17, 2)), sg.Input(key='SGi_debit_total', size=(13, 1), disabled=True)],

    ]

    Input_S1U = sg.Column([[sg.Frame(title='S1U_Interface', layout=S1U, relief='sunken', size=(610, 250))]], scrollable=True, vertical_scroll_only=True)
    Input_S5 = sg.Column([[sg.Frame(title='S5_Interface', layout=S5, relief='sunken', size=(610, 250))]], scrollable=True, vertical_scroll_only=True)
    Input_SGi = sg.Column([[sg.Frame(title='SGI_Interface', layout=SGi, relief='sunken', size=(610, 250))]], scrollable=True, vertical_scroll_only=True)

    return [[Input_S1U]] + [[Input_S5]] + [[Input_SGi]]


def makeComputationLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)
    return header + signalingInputRaw() + [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'), sg.Button('Exit', button_color=('white', 'firebrick3'))]]


def setValue(interface, windows):
    global S1U_interface_result, S5_interface_result, SGi_interface_result
    if interface == 'S1U':
        S1U_interface_result['overhead_per_packet'] = int(windows['S1U_overhead_per_packet'].get())
        S1U_interface_result['packet_size'] = int(windows['S1U_packet_size'].get())

    elif interface == 'S5':
        S1U_interface_result['overhead_per_packet'] = int(windows['S5_overhead_per_packet'].get())
        S1U_interface_result['packet_size'] = int(windows['S5_packet_size'].get())

    else:
        SGi_interface_result['overhead_per_packet'] = int(windows['SGi_overhead_per_packet'].get())
        SGi_interface_result['packet_size'] = int(windows['SGi_packet_size'].get())
    return True


def computation(currentWindows):
    for item in ['S1U', 'S5', 'SGi']:
        setValue(interface=item, windows=currentWindows)
        result = int(currentWindows[item + '_overhead_per_packet'].get()) / int(currentWindows[item + '_packet_size'].get())
        currentWindows[item + '_overhead'].update(result)
        debit_services_internet = (1+result)*buffer['debit_services_internet_dl']
        currentWindows[item + '_debit_services_internet'].update(debit_services_internet)
        debit_service_VPN = (1+result)*buffer['debit_total_vpn_dl']
        currentWindows[item + '_debit_service_VPN'].update(debit_service_VPN)
        currentWindows[item + '_debit_total'].update(debit_services_internet + debit_service_VPN)

    currentWindows.Refresh
    return True


def resetFields(currentWindows):
    for item in ['S1U', 'S5', 'SGi']:
        currentWindows[item + '_overhead_per_packet'].update('')
        currentWindows[item + '_overhead'].update('')
        currentWindows[item + '_packet_size'].update('')
        currentWindows[item + '_debit_services_internet'].update('')
        currentWindows[item + '_debit_service_VPN'].update('')
        currentWindows[item + '_debit_total'].update('')
    currentWindows.Refresh

    return True


def loadWindows(previousWindows, event):

    windows_title = str(event)  # change windows title
    windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 610), grab_anywhere=True)
    previousWindows.hide()
    while True:
        compute_event, compute_values = windows.read()

        if compute_event == sg.WIN_CLOSED:
            exit()  # Quit application
        elif compute_event == previous_event:
            previousWindows.un_hide()
            windows.close()
            break

        elif compute_event == compute_vent:
            try:
                computation(currentWindows=windows)
            except:
                sg.popup_error('Something went wrong, Please check Your Entries', title='Error')

        else:  # compute_event == delete_event
            resetFields(currentWindows=windows)

    return True

