import PySimpleGUI as sg

previous_event, delete_event, compute_vent = 'Exit', 'Reset', 'Compute'

# Calculation of the total number of operations for each signalling procedure
operating_capacity = {'MME': [0, 0, 0], 'SGW': [0, 0], 'PGW': [0, 0], 'SGW_PGW': [0, 0], 'HSS': 0, 'PCRF': 0}


def makeWindowHeader(title):
    header = [
                [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
                [sg.T('', font='any 1')],  # space
                [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
                [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def signalingInputRaw():

    input_MME = [
        [sg.Text('Metriques', size=(17, 1)), sg.Text('Unité', size=(20, 1)), sg.Text('Valeur', size=(14, 1)), sg.Text('%', size=(7, 1)), sg.Text('Capacité d\'exploitation', size=(10, 2))],
        [sg.Text('Simultaneous Attached Users(SAU)', size=(17, 2)), sg.Text('abonnés', size=(17, 1)), sg.Input(key='MME_value_1', size=(13, 1)),  sg.Input(key='MME_prc_1', size=(13, 1)), sg.Input(key='MME_capacity_1', size=(13, 1), disabled=True)],
        [sg.Text('Transitions idle/active par seconde', size=(17, 2)), sg.Text('transitions/seconde', size=(17, 2)), sg.Input(key='MME_value_2', size=(13, 1)),  sg.Input(key='MME_prc_2', size=(13, 1)), sg.Input(key='MME_capacity_2', size=(13, 1), disabled=True)],
        [sg.Text('Nbre total transactions par seconde', size=(17, 2)), sg.Text('transactions/seconde', size=(17, 2)), sg.Input(key='MME_value_3', size=(13, 1)),  sg.Input(key='MME_prc_3', size=(13, 1)), sg.Input(key='MME_capacity_3', size=(13, 1), disabled=True)],
    ]

    input_SGW = [
        [sg.Text('Metriques', size=(17, 1)), sg.Text('Unité', size=(20, 1)), sg.Text('Valeur', size=(14, 1)), sg.Text('%', size=(7, 1)), sg.Text('Capacité d\'exploitation', size=(10, 2))],
        [sg.Text('Nombre de bearers', size=(17, 2)), sg.Text('bearers', size=(17, 2)), sg.Input(key='SGW_value_1', size=(13, 1)),  sg.Input(key='SGW_prc_1', size=(13, 1)), sg.Input(key='SGW_capacity_1', size=(13, 1), disabled=True)],
        [sg.Text('Capacité traitement de données', size=(17, 2)), sg.Text('Gbits', size=(17, 2)), sg.Input(key='SGW_value_2', size=(13, 1)),  sg.Input(key='SGW_prc_2', size=(13, 1)), sg.Input(key='SGW_capacity_2', size=(13, 1), disabled=True)],
    ]

    input_PGW = [
        [sg.Text('Metriques', size=(17, 1)), sg.Text('Unité', size=(20, 1)), sg.Text('Valeur', size=(14, 1)), sg.Text('%', size=(7, 1)), sg.Text('Capacité d\'exploitation', size=(10, 2))],
        [sg.Text('Nombre de bearers', size=(17, 2)), sg.Text('bearers', size=(17, 2)), sg.Input(key='PGW_value_1', size=(13, 1)),  sg.Input(key='PGW_prc_1', size=(13, 1)), sg.Input(key='PGW_capacity_1', size=(13, 1), disabled=True)],
        [sg.Text('Capacité traitement de données', size=(17, 2)), sg.Text('Gbits', size=(17, 2)), sg.Input(key='PGW_value_2', size=(13, 1)),  sg.Input(key='PGW_prc_2', size=(13, 1)), sg.Input(key='PGW_capacity_2', size=(13, 1), disabled=True)],
    ]

    input_SGW_PGW_Combined = [
        [sg.Text('Metriques', size=(17, 1)), sg.Text('Unité', size=(20, 1)), sg.Text('Valeur', size=(14, 1)), sg.Text('%', size=(7, 1)), sg.Text('Capacité d\'exploitation', size=(10, 2))],
        [sg.Text('Nombre de bearers', size=(17, 2)), sg.Text('bearers', size=(17, 2)), sg.Input(key='SGW_PGW_value_1', size=(13, 1)),  sg.Input(key='SGW_PGW_prc_1', size=(13, 1)), sg.Input(key='SGW_PGW_capacity_1', size=(13, 1), disabled=True)],
        [sg.Text('Capacité traitement de données', size=(17, 2)), sg.Text('Gbits', size=(17, 2)), sg.Input(key='SGW_PGW_value_2', size=(13, 1)),  sg.Input(key='SGW_PGW_prc_2', size=(13, 1)), sg.Input(key='SGW_PGW_capacity_2', size=(13, 1), disabled=True)],
    ]

    input_HSS_PCRF = [
        [sg.Text('Metriques', size=(17, 1)), sg.Text('Unité', size=(20, 1)), sg.Text('Valeur', size=(14, 1)), sg.Text('%', size=(7, 1)), sg.Text('Capacité d\'exploitation', size=(10, 2))],
        [sg.Text('Nombre d\'abonnés supportés HSS', size=(17, 2)), sg.Text('abonnés', size=(17, 2)), sg.Input(key='HSS_value_1', size=(13, 1)),  sg.Input(key='HSS_prc_1', size=(13, 1)), sg.Input(key='HSS_capacity_1', size=(13, 1), disabled=True)],
        [sg.Text('Nbre total transactions par seconde PCRF', size=(17, 2)), sg.Text('transactions/seconde', size=(17, 2)), sg.Input(key='PCRF_value_1', size=(13, 1)),  sg.Input(key='PCRF_prc_1', size=(13, 1)), sg.Input(key='PCRF_capacity_1', size=(13, 1), disabled=True)],
    ]

    Input_MME = sg.Column([[sg.Frame(title='MME', layout=input_MME, relief='sunken', size=(610, 170))]], scrollable=True, vertical_scroll_only=True)
    Input_SGW = sg.Column([[sg.Frame(title='SWG', layout=input_SGW, relief='sunken', size=(610, 150))]], scrollable=True, vertical_scroll_only=True)
    Input_PGW = sg.Column([[sg.Frame(title='PWG', layout=input_PGW, relief='sunken', size=(610, 150))]], scrollable=True, vertical_scroll_only=True)
    Input_SGW_PGW_Combined = sg.Column([[sg.Frame(title='SGW_PGW_Combined', layout=input_SGW_PGW_Combined, relief='sunken', size=(610, 150))]], scrollable=True, vertical_scroll_only=True)
    Input_HSS_PCRF = sg.Column([[sg.Frame(title='HSS_PCRF', layout=input_HSS_PCRF, relief='sunken', size=(610, 150))]], scrollable=True, vertical_scroll_only=True)

    return [[Input_MME]] + [[Input_SGW]] + [[Input_PGW]] + [[Input_SGW_PGW_Combined]] + [[Input_HSS_PCRF]]


def makeComputationLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)
    return header + signalingInputRaw() + [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'), sg.Button('Exit', button_color=('white', 'firebrick3'))]]


def computation(currentWindows):
    global operating_capacity, PGW_value

    for item in ['SGW', 'PGW', 'SGW_PGW']:
        for i in range(1, 3):
            result = float(currentWindows[item+'_value_' + str(i)].get()) * float(currentWindows[item+'_prc_' + str(i)].get())
            currentWindows[item + '_capacity_' + str(i)].update(result)
            operating_capacity[item][i-1] = result

    operating_capacity['PGW_value'] = int(currentWindows['PGW_value_2'].get())

    for item in ['HSS', 'PCRF']:
        result = float(currentWindows[item+'_value_1'].get()) * float(currentWindows[item+'_prc_1'].get())
        currentWindows[item + '_capacity_1'].update(result)
        operating_capacity[item] = result

    for i in range(1, 4):
        result = float(currentWindows['MME_value_' + str(i)].get()) * float(currentWindows['MME_prc_' + str(i)].get())
        currentWindows['MME_capacity_' + str(i)].update(result)
        operating_capacity['MME'][i - 1] = result

    currentWindows.Refresh
    return True


def resetFields(currentWindows):

    for item in ['SGW', 'PGW', 'SGW_PGW']:
        for i in range(1, 3):
            currentWindows[item + '_value_' + str(i)].update('')
            currentWindows[item + '_prc_' + str(i)].update('')
            currentWindows[item + '_capacity_' + str(i)].update('')

    for item in ['HSS', 'PCRF']:
        currentWindows[item + '_value_1'].update('')
        currentWindows[item + '_prc_1'].update('')
        currentWindows[item + '_capacity_1'].update('')

    for i in range(1, 4):
        currentWindows['MME_value_' + str(i)].update('')
        currentWindows['MME_prc_' + str(i)].update('')
        currentWindows['MME_capacity_' + str(i)].update('')

    currentWindows.Refresh
    return True


def loadWindows(previousWindows, event):

    windows_title = str(event)  # change windows title
    windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 670), grab_anywhere=True)
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

