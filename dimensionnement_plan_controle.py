import PySimpleGUI as sg
from signaling_traffic_windows import result, keys
choice = ''  # S1 or S8 interface
previous_event, delete_event, compute_vent = 'Exit', 'Reset', 'Compute'


def makeWindowHeader(title):
    header = [
                [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
                [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def msg_avg_size_input():
    msg_avg_size_row = [
        [sg.T('', font='any 1')],
        [sg.Text('Taille moyen d\'un message (bits)', size=(36, 1)), sg.Input(key='msg_avg_size', size=(13, 1))]
    ]
    return msg_avg_size_row


def signalingInputRows():
    rows = [
                    [sg.Input('N(attach)', size=(40, 1), disabled=True), sg.Input(result['attach'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(detach)', size=(40, 1), disabled=True), sg.Input(result['detach'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(idle to active)', size=(40, 1), disabled=True), sg.Input(result['idle_to_active'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(PDN)', size=(40, 1), disabled=True), sg.Input(result['PDN'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(bearers activ/desac)', size=(40, 1), disabled=True), sg.Input(result['bearers_activ_desactiv'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(TAU_inter_MME)', size=(40, 1), disabled=True), sg.Input(result['TAU_inter_MME'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(TAU)', size=(40, 1), disabled=True), sg.Input(result['TAU'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(X2_HO)', size=(40, 1),  disabled=True), sg.Input(result['X2_HO'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(S1_HO)', size=(40, 1), disabled=True), sg.Input(result['S1_HO'], size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input('N(HO_inter_MME)', size=(40, 1), disabled=True), sg.Input(result['HO_inter_MME'], size=(13, 1), pad=(0, 0), disabled=True)]
                   ]
    return rows


def S1InterfaceEntries():

    table_header_1 = [
        [sg.Text('Nombre de messages/procèdure via S1-C', size=(35, 1)), sg.Text('Capacité S1-C (Gbits/s)', size=(10, 2))]
    ]
    input_rows_1 = [
                    [sg.Input(size=(40, 1), key='attach_s1c_msg'), sg.Input(key='attach_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='detach_s1c_msg'), sg.Input(key='detach_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='idle_to_active_s1c_msg'), sg.Input(key='idle_to_active_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='PDN_s1c_msg'), sg.Input(key='PDN_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='bearers_activ_desactiv_s1c_msg'), sg.Input(key='bearers_activ_desactiv_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_inter_MME_s1c_msg'), sg.Input(key='TAU_inter_MME_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_s1c_msg'), sg.Input(key='TAU_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='X2_HO_s1c_msg'), sg.Input(key='X2_HO_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='S1_HO_s1c_msg'), sg.Input(key='S1_HO_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='HO_inter_MME_s1c_msg'), sg.Input(key='HO_inter_MME_s1c_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Text('Capacité totale(Gbits/s)', size=(35, 1)), sg.Input(key='total_capacity_s1c', size=(13, 1), pad=(0, 0), disabled=True)]
                   ]

    table_header_2 = [
        [sg.Text('Entrer le Nombre de messages via S11', size=(35, 1)), sg.Text('Capacité S11 (Gbits/s)', size=(10, 2))]
    ]

    input_rows_2 = [
                    [sg.Input(size=(40, 1), key='attach_S11_msg'), sg.Input(key='attach_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='detach_S11_msg'), sg.Input(key='detach_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='idle_to_active_S11_msg'), sg.Input(key='idle_to_active_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='PDN_S11_msg'), sg.Input(key='PDN_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='bearers_activ_desactiv_S11_msg'), sg.Input(key='bearers_activ_desactiv_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_inter_MME_S11_msg'), sg.Input(key='TAU_inter_MME_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_S11_msg'), sg.Input(key='TAU_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='X2_HO_S11_msg'), sg.Input(key='X2_HO_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='S1_HO_S11_msg'), sg.Input(key='S1_HO_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='HO_inter_MME_S11_msg'), sg.Input(key='HO_inter_MME_S11_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Text('Capacité totale(Gbits/s)', size=(35, 1)), sg.Input(key='total_capacity_S11', size=(13, 1), pad=(0, 0), disabled=True)]
                   ]

    table_1 = table_header_1 + input_rows_1
    table_2 = table_header_2 + input_rows_2

    frame_1 = sg.Column([[sg.Frame(title='Procedures', layout=signalingInputRows(), relief='sunken', size=(610, 300))]],scrollable=True, vertical_scroll_only=True)
    frame_2 = sg.Column([[sg.Frame(title='S1-C_Interface', layout=table_1, relief='sunken', size=(610, 360))]], scrollable=True, vertical_scroll_only=True)
    frame_3 = sg.Column([[sg.Frame(title='S11_Interface', layout=table_2, relief='sunken', size=(610, 360))]], scrollable=True, vertical_scroll_only=True)

    return [[frame_1]] + msg_avg_size_input() + [[frame_2]] + [[frame_3]]


def S8InterfaceEntries():

    table_header_1 = [
        [sg.Text('Nombre de messages via S8', size=(35, 1)), sg.Text('Capcité S8 (Gbits/s)', size=(10, 2))]
    ]
    input_rows_1 = [
                    [sg.Input(size=(40, 1), key='attach_S8_msg'), sg.Input(key='attach_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='detach_S8_msg'), sg.Input(key='detach_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='idle_to_active_S8_msg'), sg.Input(key='idle_to_active_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='PDN_S8_msg'), sg.Input(key='PDN_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='bearers_activ_desactiv_S8_msg'), sg.Input(key='bearers_activ_desactiv_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_inter_MME_S8_msg'), sg.Input(key='TAU_inter_MME_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_S8_msg'), sg.Input(key='TAU_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='X2_HO_S8_msg'), sg.Input(key='X2_HO_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='S1_HO_S8_msg'), sg.Input(key='S1_HO_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='HO_inter_MME_S8_msg'), sg.Input(key='HO_inter_MME_S8_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Text('Capacité totale(Gbits/s)', size=(35, 1)), sg.Input(key='total_capacity_S8', size=(13, 1), pad=(0, 0), disabled=True)]
                   ]
    table_header_2 = [
        [sg.Text('Entrer le Nombre de messages via S6a', size=(35, 1)), sg.Text('Capcité S6a (Gbits/s)', size=(10, 2))]
    ]

    input_rows_2 = [
                    [sg.Input(size=(40, 1), key='attach_S6a_msg'), sg.Input(key='attach_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='detach_S6a_msg'), sg.Input(key='detach_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='idle_to_active_S6a_msg'), sg.Input(key='idle_to_active_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='PDN_S6a_msg'), sg.Input(key='PDN_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='bearers_activ_desactiv_S6a_msg'), sg.Input(key='bearers_activ_desactiv_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_inter_MME_S6a_msg'), sg.Input(key='TAU_inter_MME_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='TAU_S6a_msg'), sg.Input(key='TAU_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='X2_HO_S6a_msg'), sg.Input(key='X2_HO_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='S1_HO_S6a_msg'), sg.Input(key='S1_HO_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Input(size=(40, 1), key='HO_inter_MME_S6a_msg'), sg.Input(key='HO_inter_MME_S6a_capacity', size=(13, 1), pad=(0, 0), disabled=True)],
                    [sg.Text('Capacité totale(Gbits/s)', size=(35, 1)), sg.Input(key='total_capacity_S6a', size=(13, 1), pad=(0, 0), disabled=True)]
                   ]
    table_1 = table_header_1 + input_rows_1
    table_2 = table_header_2 + input_rows_2

    frame_1 = sg.Column([[sg.Frame(title='Procedures', layout=signalingInputRows(), relief='sunken', size=(610, 300))]],scrollable=True, vertical_scroll_only=True)
    frame_2 = sg.Column([[sg.Frame(title='S8_Interface', layout=table_1, relief='sunken', size=(610, 360))]], scrollable=True, vertical_scroll_only=True)
    frame_3 = sg.Column([[sg.Frame(title='S6a_Interface', layout=table_2, relief='sunken', size=(610, 360))]], scrollable=True, vertical_scroll_only=True)

    return [[frame_1]] + msg_avg_size_input() + [[frame_2]] + [[frame_3]]


def makeComputationLayout(windowsTitle):
    global choice
    header = makeWindowHeader(title=windowsTitle)
    if choice == 'S1':
        return header + S1InterfaceEntries() + [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'), sg.Button('Exit', button_color=('white', 'firebrick3'))]]

    else:
        return header + S8InterfaceEntries() + [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'), sg.Button('Exit', button_color=('white', 'firebrick3'))]]


def computation(currentWindows):
    global choice
    total = 0
    if choice == 'S1':
        for item in ['s1c', 'S11']:
            for sig in keys:
                final = (int(currentWindows['msg_avg_size'].get()) * result[sig] * int(currentWindows[sig + '_' + item + '_msg'].get())) / (3600 * 1000000)
                total += final
                currentWindows[f'{sig}_{item}_capacity'].update(final)
            currentWindows['total_capacity_' + item].update(total)
            total = 0

    else:
        for item in ['S8', 'S6a']:
            for sig in keys:
                final = (int(currentWindows['msg_avg_size'].get()) * result[sig] * int(currentWindows[sig + '_' + item + '_msg'].get())) / (3600 * 1000000)
                total += final
                currentWindows[f'{sig}_{item}_capacity'].update(final)
            currentWindows['total_capacity_' + item].update(total)
            total = 0

    currentWindows.Refresh()
    return True


def resetFields(currentWindows):
    global choice
    if choice == 'S1':
        for item in ['s1c', 'S11']:
            for sig in keys:
                currentWindows[f'{sig}_{item}_capacity'].update('')
                currentWindows[f'{sig}_{item}_msg'].update('')
            currentWindows['total_capacity_' + item].update('')
    else:
        for item in ['S8', 'S6a']:
            for sig in keys:
                currentWindows[f'{sig}_{item}_capacity'].update('')
                currentWindows[f'{sig}_{item}_msg'].update('')
            currentWindows['total_capacity_' + item].update('')

    currentWindows.Refresh
    return True


def loadWindows(previousWindows, event):
    global choice
    if event == 'Calcul des Capacités des Interfaces S1U(Trafic Utilisateur)':
        choice = 'S1'
        windows_title = str(event)  # change windows title
        windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 700), grab_anywhere=True)
        previousWindows.hide()
        while True:
            compute_event, compute_values = windows.read()

            if compute_event == sg.WIN_CLOSED:
                exit()

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

    elif event == 'Calcul des Capacités des Interfaces S8(Trafic Utilisateur)':
        choice = 'S8'
        windows_title = str(event)
        windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 700),
                            grab_anywhere=True)
        previousWindows.hide()
        while True:
            compute_event, compute_values = windows.read()

            if compute_event == sg.WIN_CLOSED or compute_event == previous_event:
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
