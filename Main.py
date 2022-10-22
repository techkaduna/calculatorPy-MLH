'''{Author:Kolawole Andrew
    Date: Wednesday, ‎August ‎31, ‎2022, ‏‎6:53:19 AM}'''
    
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.graphics.instructions import Canvas
import sys
import Matrix

class WindowManager(ScreenManager):
    pass

class SelectOperation(Screen):
    pass

class EquationWindows(Screen):
    pass
    
class SolveBy2(Screen):
    def __init__(self,**kwargs):
        super(SolveBy2,self).__init__(**kwargs)
        
    def solve_eqn(self):
        a = float(self.ids.a.text)
        b = float(self.ids.b.text)
        c = float(self.ids.c.text)
        d = float(self.ids.d.text)
        e = float(self.ids.e.text)
        f = float(self.ids.f.text)
        soln = Matrix.solve_by2(a, b, c, d, e, f)
        self.ids.ans_label.text = 'Answer: ' + str(soln)
        print(self.ids.some)
            
        
class SolveBy3(Screen):
    
    def __init__(self,**kwargs):
        super(SolveBy3,self).__init__(**kwargs)
      
    def solve_eqn(self):

        l = []
        for i in range(12):
            b = self.ids['b_'+str(i)].text
            l.append(b)

        eqn1 = str(l[0]) + ','+ str(l[1])+ ','+ str(l[2]) + ','+ str(l[3])
        eqn2 = str(l[4]) + ','+ str(l[5])+ ','+ str(l[6]) + ','+ str(l[7])
        eqn3 = str(l[8]) + ','+ str(l[9])+ ','+ str(l[10]) + ','+ str(l[11])
        soln = Matrix.solve_by3(eqn1,eqn2,eqn3)
        self.ids.by3_ans.text = self.ids.by3_ans.text+ '\n' +str(soln)
        
        

class Quadratic(Screen):
    def __init__(self,**kwargs):
        super(Quadratic,self).__init__(**kwargs)  
    def solve_eqn(self):
    
        a = float(self.ids['a'].text)
        b = float(self.ids['b'].text)
        c = float(self.ids['c'].text)
        soln = Matrix.quadratic(a, b, c)
        if len(soln) > 30:
            self.ids.quad_ans.font_size = dp(12)
            self.ids.quad_ans.text = str(soln)
        else:
            self.ids.quad_ans.text = self.ids.quad_ans.text + '\n' + str(soln)



class About(Screen):
    
    text = StringProperty('')
    def __init__(self,**kwargs):
        super(About,self).__init__(**kwargs)
        with open('About.txt','r') as f:
            About.text = f.read()
            f.close()

kv = Builder.load_file('main.kv')
class CalcApp(App):
    def build(self):
        Window.size = [250,300]
        return kv


if __name__ == '__main__':
    CalcApp().run()