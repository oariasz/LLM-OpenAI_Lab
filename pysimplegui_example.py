import PySimpleGUI as sg

def main():
    # Define the layout of the window
    layout = [
        [sg.Text('PySimpleGUI Example', font=('Helvetica', 16), justification='center')],
        [sg.Button('Click Me', key='btn_click'), sg.Button('Clear Bar', key='btn_clear')],
        [sg.Text('Hello, PySimpleGUI!', key='output_text', size=(30, 1), justification='center')],
        # [sg.Stretch(), sg.Text("Welcome!", key="message_bar", background_color="lightgray", text_color="black", justification="center"), sg.Stretch()]
        # [sg.Column([[sg.Text("Welcome!", key="message_bar", background_color="lightgray", text_color="black", justification="center", size=(None, 1), expand_x=True)]], justification="center")]
        # [sg.Frame("", [[sg.Text("", key="message_bar", background_color="lightgray", text_color="black", justification="center", size=(None, 1), expand_x=True)]], background_color="lightgray", pad=(0, 0))]

    ]

    # Create the window
    window = sg.Window('PySimpleGUI Demo', layout, resizable=True, finalize=True)

    # Event loop
    while True:
        event, values = window.read()

        # Exit the program if the window is closed
        if event == sg.WINDOW_CLOSED:
            break

        # Handle button events
        if event == 'btn_click':
            window['output_text'].update('Button Clicked!')
            window['message_bar'].update('Button Clicked!')
        # Handle button click event
        if event == 'btn_clear':
            window['output_text'].update('')
            window['message_bar'].update('Screen text cleared!')  
                      
    # Close the window when the event loop exits
    window.close()

if __name__ == '__main__':
    main()
