import tkinter as tk

expression = ""


def press(key):
    global expression
    expression += str(key)
    equation.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial",20), bd=10)
entry.pack(fill="both")

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            action = equal
        else:
            action = lambda x=btn: press(x)

        tk.Button(frame,text=btn,font=("Arial",18),
                  command=action).pack(side="left",expand=True,fill="both")

tk.Button(root,text="Clear",font=("Arial",18),
          command=clear).pack(fill="both")

root.mainloop()
