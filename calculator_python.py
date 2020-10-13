import wx

OPRT_NONE = ''
OPRT_DIVIDE = ' / '
OPRT_MULTIPLY= ' + '
OPRT_MINUS = ' - '
OPRT_PLUS = ' + '

class CalculatorFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='송재욱_계산기')
        self.SetSize(400, 350)
        self.mainPanel = wx.Panel(self)
        self.btnPanel = wx.Panel(self.mainPanel)
        
        self.oprtInput = OPRT_NONE
        self.result = 0     # calculation result

        self.InitUI()
        self.InitBind()
        self.SetFocus()


    def InitUI(self):
        self.calcLog = wx.StaticText(self.mainPanel, label = '')
        self.calcIO = wx.TextCtrl(self.mainPanel, value='0')
        self.calcIO.SetValue('0')
        self.numBtns = (
            wx.Button(self.btnPanel, label='1'),
            wx.Button(self.btnPanel, label='2'),
            wx.Button(self.btnPanel, label='3'),
            wx.Button(self.btnPanel, label='4'),
            wx.Button(self.btnPanel, label='5'),
            wx.Button(self.btnPanel, label='6'),
            wx.Button(self.btnPanel, label='7'),
            wx.Button(self.btnPanel, label='8'),
            wx.Button(self.btnPanel, label='9'),
            wx.Button(self.btnPanel, label='0'),
            wx.Button(self.btnPanel, label='00'),
            wx.Button(self.btnPanel, label='.')
            )
        self.oprtBtns = (
            wx.Button(self.btnPanel, label='/'),
            wx.Button(self.btnPanel, label='*'),
            wx.Button(self.btnPanel, label='-'),
            wx.Button(self.btnPanel, label='+')
            )
        self.clearBtns = (
            wx.Button(self.btnPanel, label='←'),
            wx.Button(self.btnPanel, label='C'),
            wx.Button(self.btnPanel, label='CE')
            )
        self.resultBtn = wx.Button(self.btnPanel, label='=')

        " sizer of calcLog "
        self.staticBoxSizer = wx.StaticBoxSizer(wx.HORIZONTAL, self.mainPanel, 'Calc Log')
        self.staticBoxSizer.Add(self.calcLog)
        '''
        " sizer of number buttons "
        self.numBtnSizer = wx.GridSizer(rows=5, cols=3, hgap=5, vgap=5)
        for clearBtn in self.clearBtns:
            self.numBtnSizer.Add(clearBtn, 0, wx.EXPAND)
        for numBtn in self.numBtns:
            self.numBtnSizer.Add(numBtn, 0, wx.EXPAND)
        '''
        " sizer of operator buttons "
        '''
        self.oprtBtnSizer = wx.GridSizer(rows=5, cols=1, hgap=5, vgap=5)
        for oprtBtn in self.oprtBtns:
            self.oprtBtnSizer.Add(oprtBtn)
        self.oprtBtnSizer.Add(self.resultBtn)
        '''


        self.btnSizer = wx.GridSizer(rows=5, cols=4, hgap=5, vgap=5)
        " col 1 "
        self.btnSizer.Add(self.clearBtns[0], 0, wx.EXPAND)
        self.btnSizer.Add(self.clearBtns[1], 0, wx.EXPAND)
        self.btnSizer.Add(self.clearBtns[2], 0, wx.EXPAND)
        self.btnSizer.Add(self.oprtBtns[0], 0, wx.EXPAND)
        " col 2 "
        self.btnSizer.Add(self.numBtns[6], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[7], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[8], 0, wx.EXPAND)
        self.btnSizer.Add(self.oprtBtns[1], 0, wx.EXPAND)
        " col 3 "
        self.btnSizer.Add(self.numBtns[3], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[4], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[5], 0, wx.EXPAND)
        self.btnSizer.Add(self.oprtBtns[2], 0, wx.EXPAND)
        " col 4 "
        self.btnSizer.Add(self.numBtns[0], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[1], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[2], 0, wx.EXPAND)
        self.btnSizer.Add(self.oprtBtns[3], 0, wx.EXPAND)
        " col 5 "
        self.btnSizer.Add(self.numBtns[9], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[10], 0, wx.EXPAND)
        self.btnSizer.Add(self.numBtns[11], 0, wx.EXPAND)
        self.btnSizer.Add(self.resultBtn, 0, wx.EXPAND)
        self.btnPanel.SetSizer(self.btnSizer)
        
        
        " sizer of mainPanel "        
        self.mainPanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainPanelSizer.Add(self.staticBoxSizer, 1, wx.EXPAND | wx.ALL, 5)
        self.mainPanelSizer.Add(self.calcIO, 0, wx.EXPAND | wx.ALL, 5)
        self.mainPanelSizer.Add(self.btnPanel, 6, wx.EXPAND | wx.ALL, 5)
        self.mainPanel.SetSizer(self.mainPanelSizer)

    def InitBind(self):
        " bind number buttons to button event "
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_1, self.numBtns[0])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_2, self.numBtns[1])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_3, self.numBtns[2])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_4, self.numBtns[3])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_5, self.numBtns[4])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_6, self.numBtns[5])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_7, self.numBtns[6])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_8, self.numBtns[7])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_9, self.numBtns[8])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_0, self.numBtns[9])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_00, self.numBtns[10])
        self.Bind(wx.EVT_BUTTON, self.OnNumBtn_Point, self.numBtns[11])
        " bind operator buttons to button event "
        self.Bind(wx.EVT_BUTTON, self.OnOprtBtn_Divide, self.oprtBtns[0])
        self.Bind(wx.EVT_BUTTON, self.OnOprtBtn_Multiply, self.oprtBtns[1])
        self.Bind(wx.EVT_BUTTON, self.OnOprtBtn_Minus, self.oprtBtns[2])
        self.Bind(wx.EVT_BUTTON, self.OnOprtBtn_Plus, self.oprtBtns[3])
        " bind clear buttons to button event "
        self.Bind(wx.EVT_BUTTON, self.OnDeleteBtn, self.clearBtns[0])
        self.Bind(wx.EVT_BUTTON, self.OnClearBtn, self.clearBtns[1])
        self.Bind(wx.EVT_BUTTON, self.OnEntryClearBtn, self.clearBtns[2])
        " bind result button to button event "
        self.Bind(wx.EVT_BUTTON, self.OnResultBtn, self.resultBtn)
        " bind calcIO to focus event "
        self.calcIO.Bind(wx.EVT_SET_FOCUS, self.OnCalcIOLeftDown)
        " bind keyboard input to key down event "
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)


    def OnNumBtn_1(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('1')
        else:
            self.calcIO.SetValue(entryInput + '1')
        self.SetFocus()

    def OnNumBtn_2(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('2')
        else:
            self.calcIO.SetValue(entryInput + '2')
        self.SetFocus()

    def OnNumBtn_3(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('3')
        else:
            self.calcIO.SetValue(entryInput + '3')
        self.SetFocus()
            
    def OnNumBtn_4(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('4')
        else:
            self.calcIO.SetValue(entryInput + '4')
        self.SetFocus()

    def OnNumBtn_5(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('5')
        else:
            self.calcIO.SetValue(entryInput + '5')
        self.SetFocus()

    def OnNumBtn_6(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('6')
        else:
            self.calcIO.SetValue(entryInput + '6')
        self.SetFocus()

    def OnNumBtn_7(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('7')
        else:
            self.calcIO.SetValue(entryInput + '7')
        self.SetFocus()

    def OnNumBtn_8(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('8')
        else:
            self.calcIO.SetValue(entryInput + '8')
        self.SetFocus()

    def OnNumBtn_9(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry == 0:
            self.calcIO.SetValue('9')
        else:
            self.calcIO.SetValue(entryInput + '9')
        self.SetFocus()

    def OnNumBtn_0(self, event):
        entryInput = self.calcIO.GetValue()
        if entryInput != '0':
            self.calcIO.SetValue(entryInput + '0')
        self.SetFocus()

    def OnNumBtn_00(self, event):
        entryInput = self.calcIO.GetValue()
        if entryInput != '0':
            self.calcIO.SetValue(entryInput + '00')
        self.SetFocus()

    def OnNumBtn_Point(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        if entry != 0 and entryInput.find('.') == -1:
            self.calcIO.SetValue(entryInput + '.')
        self.SetFocus()

    def OnOprtBtn_Divide(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        calcLogLabel = self.calcLog.GetLabel()
        self.calcLog.SetLabel(calcLogLabel + str(entry) + '/')
        self.calcIO.SetValue('0')
        self.SetFocus()

    def OnOprtBtn_Multiply(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        calcLogLabel = self.calcLog.GetLabel()
        self.calcLog.SetLabel(calcLogLabel + str(entry) + '*')
        self.calcIO.SetValue('0')
        self.SetFocus()
        
    def OnOprtBtn_Minus(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        calcLogLabel = self.calcLog.GetLabel()
        self.calcLog.SetLabel(calcLogLabel + str(entry) + '-')
        self.calcIO.SetValue('0')
        self.SetFocus()
    
    def OnOprtBtn_Plus(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        calcLogLabel = self.calcLog.GetLabel()
        self.calcLog.SetLabel(calcLogLabel + str(entry) + '+')
        self.calcIO.SetValue('0')
        self.SetFocus()

    def OnDeleteBtn(self, event):
        entryInput = self.calcIO.GetValue()
        if entryInput != '0':
            if 1 ==len(entryInput):
                self.calcIO.SetValue('0')
            else:
                self.calcIO.SetValue(entryInput[:-1]) 
        self.SetFocus()

    def OnClearBtn(self, event):
        self.calcLog.SetLabel('')
        self.calcIO.SetValue('0')
        self.SetFocus()
        
    def OnEntryClearBtn(self, event):
        self.calcIO.SetValue('0')
        self.SetFocus()
         
    def OnResultBtn(self, event):
        entryInput = self.calcIO.GetValue()
        entry = float(entryInput)
        equation = self.calcLog.GetLabel()
        postfix = []
        if equation == '':  # if 'equation' is empty
            result = entry
            wx.MessageBox('결과 : ' + str(result))
        else:
            try:
                postfix = self.ConvertToPostfix(equation+str(entry))   # 후위연산식으로 변환
                result = postfix.pop(0)
                while postfix:
                    num = postfix.pop(0)
                    oprt = postfix.pop(0)
                    if oprt == '+':
                        result += num
                    elif oprt == '-':
                        result -= num
                    elif oprt == '*':
                        result *= num
                    elif oprt == '/':
                        result /= num
                wx.MessageBox('결과 : ' + str(result))
            except ZeroDivisionError:
                wx.MessageBox('0으로 나눌 수 없습니다!')
            except Exception as err:
                wx.MessageBox(str(err))
        self.calcLog.SetLabel('')
        self.calcIO.SetValue('0')
        self.SetFocus()

    def OnCalcIOLeftDown(self, event):
        self.SetFocus()
        
    def OnKeyDown(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_NUMPAD1:               # 1
            self.OnNumBtn_1(event)
        elif key == wx.WXK_NUMPAD2:             # 2
            self.OnNumBtn_2(event)
        elif key == wx.WXK_NUMPAD3:             # 3
            self.OnNumBtn_3(event)
        elif key == wx.WXK_NUMPAD4:             # 4
            self.OnNumBtn_4(event)
        elif key == wx.WXK_NUMPAD5:             # 5
            self.OnNumBtn_5(event)
        elif key == wx.WXK_NUMPAD6:             # 6
            self.OnNumBtn_6(event)
        elif key == wx.WXK_NUMPAD7:             # 7
            self.OnNumBtn_7(event)
        elif key == wx.WXK_NUMPAD8:             # 8
            self.OnNumBtn_8(event)
        elif key == wx.WXK_NUMPAD9:             # 9
            self.OnNumBtn_9(event)
        elif key == wx.WXK_NUMPAD0:             # 0
            self.OnNumBtn_0(event)
        elif key == wx.WXK_NUMPAD_DECIMAL:      # .
            self.OnNumBtn_Point(event)
        elif key == wx.WXK_NUMPAD_DIVIDE:       # /
            self.OnOprtBtn_Divide(event)
        elif key == wx.WXK_NUMPAD_MULTIPLY:     # *
            self.OnOprtBtn_Multiply(event)
        elif key == wx.WXK_NUMPAD_SUBTRACT:     # -
            self.OnOprtBtn_Minus(event)
        elif key == wx.WXK_NUMPAD_ADD:          # +
            self.OnOprtBtn_Plus(event)
        elif key == wx.WXK_NUMPAD_ENTER:        # Enter
            self.OnResultBtn(event)
        self.SetFocus()

    def ConvertToPostfix(self, equation):
        postfix = []
        " convert 'equation' to list "
        start = 0
        buffer = ''
        for i in range(1, len(equation)):
            if not self.isfloat(equation[start:i]):
                postfix.append(float(equation[start:i-1]))
                postfix.append(equation[i-1])
                start = i
        postfix.append(float(equation[start:]))
        " convert infix to postfix "
        i = 0
        while i < len(postfix):
            if self.isfloat(postfix[i]):
                i += 1
            else:
                tmp = postfix[i]
                postfix[i] = postfix[i+1]
                postfix[i+1] = tmp
                i += 2
        return postfix
        
    def isfloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        

if __name__ == '__main__':
    app = wx.App()
    frame = CalculatorFrame()
    frame.Show()
    app.MainLoop()
