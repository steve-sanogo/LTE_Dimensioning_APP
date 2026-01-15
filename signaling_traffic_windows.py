import PySimpleGUI as sg

from main_windows import global_parameters
from math import ceil

previous_event, delete_event, compute_vent = 'Exit', 'Reset', 'Compute'

# Calculation of the total number of operations for each signalling procedure
result = {'attach': 0, 'detach': 0, 'idle_to_active': 0, 'PDN': 0, 'bearers_activ_desactiv': 0, 'TAU_inter_MME': 0, 'TAU': 0, 'X2_HO': 0, 'S1_HO': 0, 'HO_inter_MME': 0, 'total_Procedure': 0}
keys = ['attach', 'detach', 'idle_to_active', 'PDN', 'bearers_activ_desactiv', 'TAU_inter_MME', 'TAU', 'X2_HO', 'S1_HO', 'HO_inter_MME']


def makeWindowHeader(title):
    header = [
                [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
                [sg.T('', font='any 1')],  # space
                [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
                [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def signalingInputRaw():

    input = [
        [sg.Text('% Utilisateurs actifs à HC', size=(17, 2)), sg.Input(key='bh_active_user_prt', size=(13, 1))],
        [sg.Text('', size=(17, 1)), sg.Text('Procédure/Abonné/HC', size=(14, 2)), sg.Text('Nombre', size=(7, 2))],
        [sg.Text('N(attach)', size=(17, 1)),  sg.Input(size=(13, 1), pad=(0, 0), key='attach'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_attach', disabled=True)],
        [sg.Text('N(detach)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='detach'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_detach', disabled=True)],
        [sg.Text('N(idle to active)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='idle_to_active'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_idle_to_active', disabled=True)],
        [sg.Text('N(PDN)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='PDN'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_PDN', disabled=True)],
        [sg.Text('N(bearers activ/desac)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='bearers_activ_desactiv'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_bearers_activ_desactiv', disabled=True)],
        [sg.Text('N(TAU_inter_MME)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='TAU_inter_MME'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_TAU_inter_MME', disabled=True)],
        [sg.Text('N(TAU)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='TAU'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_TAU', disabled=True)],
        [sg.Text('N(X2_HO)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='X2_HO'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_X2_HO', disabled=True)],
        [sg.Text('N(S1_HO)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='S1_HO'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_S1_HO', disabled=True)],
        [sg.Text('N(HO_inter_MME)', size=(17, 1)), sg.Input(size=(13, 1), pad=(0, 0), key='HO_inter_MME'), sg.Input(size=(13, 1), pad=(0, 0), key='nb_HO_inter_MME', disabled=True)],
        [sg.Text('N(procèdures)', size=(17, 1)), sg.Input(size=(27, 1), pad=(0, 0), key='nb_total_Procedure', disabled=True)],
                  ]
    input_column = sg.Column([[sg.Frame(title='', layout=input, relief='sunken', size=(610, 380))]], scrollable=True, vertical_scroll_only=True)
    return [[input_column]]


def makeComputationLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)
    return header + signalingInputRaw() + [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'), sg.Button('Exit', button_color=('white', 'firebrick3'))]]


def computation(currentWindows):
    global result, entries
    total_procedure = 0
    bh_active_customer_prt = currentWindows['bh_active_user_prt'].get()
    nb_active_user = ceil(float(bh_active_customer_prt)*int(global_parameters['nb_abonne']))
    for item in keys:
        result[item] = ceil(float(currentWindows[item].get()) * int(nb_active_user))
        currentWindows['nb_' + item].update(result[item])
        total_procedure += result[item]

    currentWindows['nb_total_Procedure'].update(total_procedure)
    currentWindows.Refresh

    result['bh_active_customer_prt'] = bh_active_customer_prt
    result['nb_active_user'] = nb_active_user
    result['total_Procedure'] = total_procedure
    return True


def resetFields(currentWindows):
    for e in ['attach', 'detach', 'idle_to_active', 'PDN', 'bearers_activ_desactiv', 'TAU_inter_MME', 'TAU', 'X2_HO', 'S1_HO', 'HO_inter_MME']:
        currentWindows[e].update('')
        currentWindows['nb_' + e].update('')
    currentWindows['nb_total_Procedure'].update('')
    currentWindows['bh_active_user_prt'].update('')
    currentWindows.Refresh
    return True


def loadWindows(previousWindows, event):

    windows_title = str(event)  # change windows title
    windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 500), grab_anywhere=True)
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

