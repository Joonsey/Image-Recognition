import pyautogui as gui

gui.alert('Pog?', 'POG', button="Pog.")

n = gui.confirm('Pog?', 'POG', buttons=["pog1","pog2","pog3"])
print(n)

gui.prompt('Pog?', 'POG', 'POG!')

gui.password(text="Pog?", default="POG!", mask="*")