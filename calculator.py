# sprite = codesters.Square(x, y, width, "color")
numberKeys = []
operationKeys = []
utilKeys = []
operations = ["+","-","x","/","="]
opIndex = 0
currentOp = ''
currentVal = 1
opNumbers = []
decimalPlaced = False
inputVal = ""
opPressed = False
lastVal = ''



def doMath(num,num2,op):
    if op == '+':
        return num+num2
    elif op == '-':
        return num-num2
    elif op == 'x':
        return num*num2
    elif op == '/':
        return num/num2
    else:
        return lastVal
   

def click(sprite):
    global inputVal, decimalPlaced, opPressed, currentOp, lastVal
   
    if sprite.value in operations:
        print(sprite.value)
        if lastVal == '':
            lastVal = float(inputVal)
        else:
            print(lastVal)
            print(inputVal)
            print(currentOp)
            lastVal = doMath(lastVal,float(inputVal),currentOp)
            print(lastVal)
            
            inputDisplay.set_text(str(lastVal))
        decimalPlaced = False
        currentOp = sprite.value
        opPressed = True
       #####
        
    elif sprite.value == "C":
        inputVal = ''
        inputDisplay.set_text('')
        opNumbers.clear()
        lastVal = ''

    elif sprite.value == "0" or  (sprite.value == "." and decimalPlaced == False) or (sprite.value != "." and int(sprite.value)):
        if len(inputVal) < 11:
            if opPressed == True:
                inputVal = ''
                inputDisplay.set_text('')
                opPressed = False
            inputVal += str(sprite.value)
            inputDisplay.set_text(inputVal)
            if sprite.value == ".":
                decimalPlaced = True
    
        
def makeButtons():
    global opIndex, currentVal
    for j in range(0,4):
        stage.wait(.1)
        for i in range(0,4):
            stage.wait(.1)
            if i % 4 == 3:
                operationKeys.append(codesters.Rectangle(60*i-100,60*j-100,50,50,"lightblue"))
                operationKeys[-1].value=operations[opIndex]
                operationKeys[-1].event_click(click)
                codesters.Text(operations[opIndex],60*i-100,60*j-100)
                opIndex += 1
            elif j % 4 == 0:
                if i == 0:
                    utilKeys.append(codesters.Rectangle(60*i-100,60*j-100,50,50,"green"))
                    utilKeys[-1].value = "0"
                    utilKeys[-1].event_click(click)
                    codesters.Text("0",60*i-100,60*j-100)
                else:
                    utilKeys.append(codesters.Rectangle(60*i-100,60*j-100,50,50,"red"))
                    if i == 1:
                        codesters.Text(".",60*i-100,60*j-100)
                        utilKeys[-1].value="."
                        utilKeys[-1].event_click(click)
                    else:
                        codesters.Text("C",60*i-100,60*j-100)
                        utilKeys[-1].value="C"
                        utilKeys[-1].event_click(click)
                        
            else:
                numberKeys.append(codesters.Rectangle(60*i-100,60*j-100,50,50,"green"))
                numberKeys[-1].value = currentVal
                codesters.Text(str(currentVal),60*i-100,60*j-100)
                numberKeys[-1].event_click(click)
                currentVal += 1

codesters.Rectangle(-10,0,280,450,"blue")

makeButtons()

equalBtn = codesters.Rectangle(-10,-160,230,50,"tan")
equalBtn.value = '='
equalBtn.event_click(click)
codesters.Text("=",-10,-160)
codesters.Rectangle(-10,140,230,50,"white")
inputDisplay=codesters.Text("",-20,140)
