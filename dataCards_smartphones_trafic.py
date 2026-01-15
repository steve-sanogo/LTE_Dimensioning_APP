import PySimpleGUI as sg

choice = ''  # take dataCarte or smartphone
previous_event, delete_event, compute_vent = 'Exit', 'Reset', 'Compute'

# each list first position is for volume traffic UL/DL and the seconds are for volume traffic in DL
dataCardResult = {'web': 2 * [0], 'email': 2 * [0], 'video': 2 * [0], 'vpn': 2 * [0], 'game': 2 * [0], 'trafic_total_UL_DL': 0, 'trafic_total_DL': 0}
smartPhoneResult = {'web': 2 * [0], 'email': 2 * [0], 'video': 2 * [0], 'vpn': 2 * [0], 'game': 2 * [0], 'trafic_total_UL_DL': 0, 'trafic_total_DL': 0}


def makeWindowHeader(title, Menu=True):
    header = [
                [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
                [sg.T('', font='any 1')],  # space
                [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
                [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


def dataCardSmartphoneInputRaw(choice):
    table_header = [
        [sg.Text('Types de services', size=(17, 2)),
         sg.Text('Nbre sessions', size=(10, 2)),
         sg.Text('Taille session (Mb)', size=(14, 2)),
         sg.Text('%DL', size=(7, 2)),
         sg.Text('Volume Trafic UL/DL (Mb)', size=(10, 2)),
         sg.Text('Volume Trafic DL(Mb)', size=(10, 2))
         ]
    ]
    input_rows = [[[sg.Text('Navigation Web', size=(17, 1))] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'web{col + 1}') for col in range(3)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'web{col + 1}', disabled=True) for col in range(3, 5)]],
                  [[sg.Text('Email', size=(17, 1))] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'email{col + 1}') for col in range(3)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'email{col + 1}', disabled=True) for col in range(3, 5)]],
                  [[sg.Text('Streaming video', size=(17, 1))] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'video{col + 1}') for col in range(3)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'video{col + 1}', disabled=True) for col in range(3, 5)]],
                  [[sg.Text('VPN', size=(17, 1))] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'vpn{col + 1}') for col in range(3)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'vpn{col + 1}', disabled=True) for col in range(3, 5)]],
                  [[sg.Text('Gaming', size=(17, 1))] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'game{col + 1}') for col in range(3)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'game{col + 1}', disabled=True) for col in range(3, 5)]],
                  [[sg.Text('', size=(17, 1))] + [sg.Input('Volume total du trafic Internet', size=(40, 1), pad=(0, 0), disabled=True,key=None)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'volume_total_trafic_internet_HC_UL_DL_{choice}',disabled=True)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'volume_total_trafic_internet_HC_DL_{choice}',disabled=True)]],
                  [[sg.Text('', size=(17, 1))] + [sg.Input('Volume total du trafic VPN', size=(40, 1), pad=(0, 0), disabled=True, key=None)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'volume_total_trafic_vpn_HC_UL_DL_{choice}',disabled=True)] + [sg.Input(size=(13, 1), pad=(0, 0), key=f'volume_total_trafic_vpn_HC_DL_{choice}',disabled=True)]],
                  [[sg.Button('Compute', button_color=('white', 'green')), sg.Button('Reset'),sg.Button('Exit', button_color=('white', 'firebrick3'))]]
                  ]
    return table_header + input_rows


def makeComputationLayout(windowsTitle):
    header = makeWindowHeader(title=windowsTitle)

    return header + dataCardSmartphoneInputRaw(choice)


def computation(entries, output):
    sum_trafic_dl_up, sum_trafic_dl = 0, 0
    for e in ['web', 'email', 'video', 'game']:
        output[e][1] = float(entries[e + str(1)]) * float(entries[e + str(2)]) * float(entries[e + str(3)])
        output[e][0] = output[e][1] / float(entries[e + str(3)])
        sum_trafic_dl_up += output[e][0]
        sum_trafic_dl += output[e][1]
    output['vpn'][1] = float(entries['vpn1']) * float(entries['vpn2']) * float(entries['vpn3'])
    output['vpn'][0] = output['vpn'][1] / float(entries['vpn3'])
    output['trafic_total_UL_DL'] = sum_trafic_dl_up
    output['trafic_total_DL'] = sum_trafic_dl
    return True


def updateValues(entries, currentWindows):
    for e in ['web', 'email', 'video', 'vpn', 'game']:
        currentWindows[e + str(4)].update(entries[e][0])
        currentWindows[e + str(5)].update(entries[e][1])
    currentWindows[f'volume_total_trafic_internet_HC_UL_DL_{choice}'].update(entries['trafic_total_UL_DL'])
    currentWindows[f'volume_total_trafic_internet_HC_DL_{choice}'].update(entries['trafic_total_DL'])
    currentWindows[f'volume_total_trafic_vpn_HC_UL_DL_{choice}'].update(entries['vpn'][0])
    currentWindows[f'volume_total_trafic_vpn_HC_DL_{choice}'].update(entries['vpn'][1])
    currentWindows.Refresh()
    return True


def resetFields(currentWindows):
    fields = list()
    for e in ['web', 'email', 'video', 'vpn', 'game']:
        fields.append([e + str(i) for i in range(1, 6)])
    fields.append([f'volume_total_trafic_internet_HC_UL_DL_{choice}', f'volume_total_trafic_internet_HC_DL_{choice}',
                   f'volume_total_trafic_vpn_HC_UL_DL_{choice}', f'volume_total_trafic_vpn_HC_DL_{choice}'])
    for liste in fields:
        for elem in liste:
            currentWindows[elem].update('')
    currentWindows.Refresh
    return True


def loadWindows(previousWindows, event):
    global choice
    if event == 'Internet & VPN généré par une \'Data Card\' en UL/DL et DL':
        choice = 'dataCard'
        windows_title = 'Trafic ' + str(event)  # change windows title
        windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 500), grab_anywhere=True)
        previousWindows.hide()
        while True:
            compute_event, compute_values = windows.read()

            if compute_event == sg.WIN_CLOSED or compute_event == previous_event:
                previousWindows.un_hide()
                windows.close()
                break

            elif compute_event == compute_vent:
                try:
                    computation(entries=compute_values, output=dataCardResult)
                    updateValues(dataCardResult, currentWindows=windows)
                except:
                    sg.popup_error('Something went wrong, Please check Your Entries', title='Error')

            else:  # compute_event == delete_event
                resetFields(currentWindows=windows)

    elif event == 'Internet généré par un smartphone LTE en UL/DL et DL':
        choice = 'smartphone'
        windows_title = 'Trafic ' + str(event)
        windows = sg.Window('LTE Dimensioning', makeComputationLayout(windowsTitle=windows_title), size=(700, 500),
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
                    computation(entries=compute_values, output=smartPhoneResult)
                    updateValues(smartPhoneResult, currentWindows=windows)
                except:
                    sg.popup_error('Something went wrong, Please check Your Entries', title='Error')

            else:  # compute_event == delete_event
                resetFields(currentWindows=windows)

    return True
