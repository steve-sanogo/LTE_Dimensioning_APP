import PySimpleGUI as sg
from math import ceil

sg.theme('Dark Blue 3')
global_parameters = {'nb_abonne': 0, 'datacard_pct': 0, 'smartphones_pct': 0, 'abonnes_actifs_acces_internet_pct': 0, 'datacard_vpn_pct': 0,
                      'nbSmartPhone': 0, 'nbDataCard': 0
                     }


def returnLayout():
    glParams_layout = [
                            [sg.Text('Entrez le nombre d\'abonnés', size=(40, 1), text_color='black'), sg.InputText(key='nb_abonne')],
                            [sg.Text('Entrez le % de datacard', size=(40, 1), text_color='black'), sg.InputText(key='datacard_pct')],
                            [sg.Text('Entrez le % de smartphones', size=(40, 1), text_color='black'), sg.InputText(key='smartphones_pct')],
                            [sg.Text('Entrez le % d\' abonnés actifs ayant acces a internet', size=(40, 1), text_color='black'), sg.InputText(key='abonnes_actifs_acces_internet_pct')],
                            [sg.Text('Entrez le % d\' abonnés actifs utilisant le vpn ', size=(40, 1), text_color='black'), sg.InputText(key='datacard_vpn_pct')]
                          ]
    layout = [
        [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
        [sg.T('', font='any 1')],  # space
        [sg.Text('Welcome To LTE Network Dimensioning Application', text_color='black', justification='center',
                 relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
        [sg.T('', font='any 1')],
        [sg.Column([[sg.Frame(title='Entrez les parametres globaux', layout=glParams_layout, relief='sunken')]])],
        [sg.Button('Start', button_color=('white', 'green')), sg.Button('Cancel')],
    ]
    return layout


def setGlobalParameters(currentWindows):
    global global_parameters
    for e in ['nb_abonne', 'datacard_pct', 'smartphones_pct', 'abonnes_actifs_acces_internet_pct', 'datacard_vpn_pct']:
        global_parameters[e] = currentWindows[e].get()
    global_parameters['nbDataCard'] = ceil(int(global_parameters['nb_abonne']) * float(global_parameters['datacard_pct']))
    global_parameters['nbSmartPhone'] = ceil(int(global_parameters['nb_abonne']) * float(global_parameters['smartphones_pct']))
    return True


def load_main_windows():
    window = sg.Window('LTE Dimensioning', returnLayout(), size=(500, 380), grab_anywhere=True)  #
    event, values = window.read()
    if event == 'Start':
        try:
            setGlobalParameters(currentWindows=window)
            window.close()
        except:
            sg.popup_error('Something went wrong, Please check Your Entries', title='Error')
            exit()

    elif event == sg.WIN_CLOSED or event == 'Cancel':
        exit()

    return True

