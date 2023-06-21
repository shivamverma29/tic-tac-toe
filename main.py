import PySimpleGUI as sg

sg.theme("Black")

box1 = sg.Button(key=1, size=[9, 4], metadata='false')
box2 = sg.Button(key=2, size=[9, 4], metadata='false')
box3 = sg.Button(key=3, size=[9, 4], metadata='false')
box4 = sg.Button(key=4, size=[9, 4], metadata='false')
box5 = sg.Button(key=5, size=[9, 4], metadata='false')
box6 = sg.Button(key=6, size=[9, 4], metadata='false')
box7 = sg.Button(key=7, size=[9, 4], metadata='false')
box8 = sg.Button(key=8, size=[9, 4], metadata='false')
box9 = sg.Button(key=9, size=[9, 4], metadata='false')
exit_button = sg.Button("Exit!")
circle_turn = sg.Text("Circle's turn!", visible=True, key='circle_turn')
cross_turn = sg.Text("Cross's turn!", visible=False, key='cross_turn')
circle_won = sg.Text("Circle Won!", visible=False, key='circle')
cross_won = sg.Text("Cross Won!", visible=False, key='cross')
turn = 0
status = {"flag1": -1, "flag2": -1, "flag3": -1, "flag4": -1, "flag5": -1,
          "flag6": -1, "flag7": -1, "flag8": -1, "flag9": -1}
layout = [[circle_turn, cross_turn], [box1, box2, box3], [box4, box5, box6],
          [box7, box8, box9], [cross_won], [circle_won], [exit_button]]
window = sg.Window("Tic-Tac-toe", layout=layout)

while True:
    event = window.read()
    print(event[0])
    if window[event[0]].metadata == 'false':
        if turn == 0:
            window['circle_turn'].update(visible=False)
            window['cross_turn'].update(visible=True)
            image_path = 'circle2.png'
            turn = 1
            window[event[0]].metadata = True
            status[f'flag{event[0]}'] = 0
        else:
            window['circle_turn'].update(visible=True)
            window['cross_turn'].update(visible=False)
            image_path = 'cross2.png'
            turn = 0
            window[event[0]].metadata = True
            status[f'flag{event[0]}'] = 1
        window[event[0]].update(image_filename=image_path)
        if status["flag1"] == status["flag2"] == status["flag3"] == 0 or \
                status["flag4"] == status["flag5"] == status["flag6"] == 0 or \
                status["flag7"] == status["flag8"] == status["flag9"] == 0 or \
                status["flag1"] == status["flag4"] == status["flag7"] == 0 or \
                status["flag2"] == status["flag5"] == status["flag8"] == 0 or \
                status["flag3"] == status["flag6"] == status["flag9"] == 0 or \
                status["flag1"] == status["flag5"] == status["flag9"] == 0 or \
                status["flag3"] == status["flag5"] == status["flag7"] == 0:
            window['circle'].update(visible=True)

        elif status["flag1"] == status["flag2"] == status["flag3"] == 1 or \
                status["flag4"] == status["flag5"] == status["flag6"] == 1 or \
                status["flag7"] == status["flag8"] == status["flag9"] == 1 or \
                status["flag1"] == status["flag4"] == status["flag7"] == 1 or \
                status["flag2"] == status["flag5"] == status["flag8"] == 1 or \
                status["flag3"] == status["flag6"] == status["flag9"] == 1 or \
                status["flag1"] == status["flag5"] == status["flag9"] == 1 or \
                status["flag3"] == status["flag5"] == status["flag7"] == 1:
            window['cross'].update(visible=True)
        elif event[0] == "Exit!":
            break

window.close()