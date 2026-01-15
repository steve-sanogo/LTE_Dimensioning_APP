import PySimpleGUI as sg

import dataCards_smartphones_trafic
import main_windows
import trafic_total_internet_vpn
import signaling_traffic_windows
import dimensionnement_noeuds_lte
import nombre_de_nœuds_requis
import dimensionnement_plan_usager
import dimensionnement_plan_controle


windows_title = 'Please Choose an Operation'


sg.theme('Dark Blue 3')  #

# Home windows Menu
menu = [['&Calcul du Trafic', ['&Internet & VPN généré par une \'Data Card\' en UL/DL et DL',
                               '&Internet généré par un smartphone LTE en UL/DL et DL',
                               '&Trafic Total VPN et Internet à HC en DL et UL',
                               '&Trafic total VPN et Internet à HC en DL']],
        ['&Calcul du Trafic de Signalisation', ['&Calcul du nombre total d\'opérations pour chaque procèdure de signalisation']
                                               ],
        ['&Dimensionnement', ['&Dimensionnement des nœuds LTE', '&Nombre De Nœuds Requis', '&Dimensionnement Du Plan Usager',
                              '&Dimensionnement Du Plan de Contrôle', ['&Calcul des Capacités des Interfaces S1U(Trafic Utilisateur)', '&Calcul des Capacités des Interfaces S8(Trafic Utilisateur)']]

        ],

        ['&Help', ['&About...', '&Exit']]
        ]


def makeWindowHeader(title, Menu=True):
    header = [
        [sg.Menu(menu)] if Menu else [],
        [sg.Image(r'./images/esmt_resize.png'), sg.Push(), sg.Image(r'./images/lte.png')],
        [sg.T('', font='any 1')],  # space
        [sg.Text(title, text_color='black', justification='center', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15))],
        [[sg.T('', font='any 1', key='windowHeader')]],
    ]
    return header


layout = makeWindowHeader(windows_title)
window = sg.Window('LTE Dimensioning', layout, size=(700, 400), grab_anywhere=True)

main_windows.load_main_windows()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    # load windows
    elif event == 'Internet & VPN généré par une \'Data Card\' en UL/DL et DL' or event == 'Internet généré par un smartphone LTE en UL/DL et DL':
        dataCards_smartphones_trafic.loadWindows(previousWindows=window, event=event)

    elif event == 'Trafic Total VPN et Internet à HC en DL et UL' or event == 'Trafic total VPN et Internet à HC en DL':
        trafic_total_internet_vpn.loadWindows(previousWindows=window, event=event)

    elif event == 'Calcul du nombre total d\'opérations pour chaque procèdure de signalisation':
        signaling_traffic_windows.loadWindows(previousWindows=window, event=event)

    elif event == 'Dimensionnement des nœuds LTE':
        dimensionnement_noeuds_lte.loadWindows(previousWindows=window, event=event)

    elif event == 'Nombre De Nœuds Requis':
        nombre_de_nœuds_requis.loadWindows(previousWindows=window, event=event)
        pass
    elif event == 'Dimensionnement Du Plan Usager':
        dimensionnement_plan_usager.loadWindows(previousWindows=window, event=event)
        pass
    elif event == 'Calcul des Capacités des Interfaces S1U(Trafic Utilisateur)' or event == 'Calcul des Capacités des Interfaces S8(Trafic Utilisateur)':
        dimensionnement_plan_controle.loadWindows(previousWindows=window, event=event)

    elif event == 'About...':
        sg.popup_timed('This is the first version of LTE Dimensioning\'s app. \n For more informations please read '
                       'the documentation', title='About...', button_type=5)

    else:
        if sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break


window.close()
# and sg.popup_yes_no('Do you really want to exit?') == 'Yes'
