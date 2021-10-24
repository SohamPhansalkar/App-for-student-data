import kivy
from kivy.app import App
from kivy.uix.behaviors import button 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

import collections
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

DB_token = ("Make your own account on mongoDB.com and use your key!")

client = MongoClient(DB_token)

bd = client.test

Collection = bd.app1_1

data_1 = {"password": "1",
          "accname": "ALPHA (main)",
          "id": 10222,
          "name" : "Soham"}


class Main(GridLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.cols = 1
        self.size_hint = (0.6 ,0.7)
        self.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        
        #self.testinj = Image(source='imagesback 1.jfif', height = 100, width = 300)
        #self.add_widget(self.testinj)
        
        self.loginpage = Label(text = "Log-in", 
                               font_size = 45,
                               color = "#FFFF00")
        self.add_widget(self.loginpage)
        
        self.blanklabel_1 = Label(text = "", 
                               font_size = 38,
                               color = "#FFFF00")
        self.add_widget(self.blanklabel_1)
        ##
        self.labelaccname = Label(text = "Account name", 
                               font_size = 35,
                               color = "#FFFF00")
        self.add_widget(self.labelaccname)
        
        ##
        self.inputaccname = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (1, 0.5))
        self.add_widget(self.inputaccname)
        
        ##
        self.labelaccpass = Label(text = "Account Password", 
                               font_size = 35,
                               color = "#FFFF00")
        self.add_widget(self.labelaccpass)
        
        ##
        self.inputaccpass = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (1, 0.5))
        self.add_widget(self.inputaccpass)
        
        self.passbtn_1 = Button(text = "log-in",
                                size_hint = (1, 0.5),
                                background_color = "#00ffce",
                                background_normal = "",
                                bold = True)
        self.passbtn_1.bind(on_press = self.log_in_btn)
        self.add_widget(self.passbtn_1)
        
        self.blanklabel_2 = Label(text = "", 
                               font_size = 30,
                               color = "#FFFF00")
        self.add_widget(self.blanklabel_2)
    
        self.create_account = Button(text = "Create Account",
                                size_hint = (1, 0.5),
                                background_color = "#00ffce",
                                #background_normal = "",
                                bold = True)
        self.create_account.bind(on_press = self.create_account_btn)
        self.add_widget(self.create_account)
                
    def log_in_btn(self, event):
        try:
            result = Collection.find_one({"_id" : str(self.inputaccname.text)})
            a = result["password"]
            
            
            if self.inputaccpass.text == a:
                c = result["name"]
                self.blanklabel_1.text = f"Your logged in as {c}"
                self.blanklabel_1.color = "#00FF00"
                #time.sleep(3)
                
                self.remove_widget(self.loginpage)
                self.remove_widget(self.inputaccpass)
                self.remove_widget(self.passbtn_1)
                self.remove_widget(self.blanklabel_1)
                self.remove_widget(self.blanklabel_2)
                self.remove_widget(self.create_account)
                self.remove_widget(self.labelaccname)
                self.remove_widget(self.labelaccpass)
                self.remove_widget(self.inputaccname)
                self.remove_widget(self.inputaccpass)
                self.selectionPage()
                
                
            else:
                self.blanklabel_1.text = f"Incorrect password"
                self.blanklabel_1.color = "#FF0000"
        except:
            self.blanklabel_1.text = f"No account like this"
            self.blanklabel_1.color = "#FF0000"
            
        
    def selectionPage(self, event = None):
        result = Collection.find_one({"_id" : str(self.inputaccname.text)})
        c = result["name"]
        self.loggedinas = Label(text = f"Logged in as - {c}",
                                font_size = 45,
                               color = "#FFFF00")
        self.add_widget(self.loggedinas)
        
        self.btn2_1 = Button(text = "Edit account details")
        self.btn2_1.bind(on_press = self.AddDataPage)
        self.add_widget(self.btn2_1)
        
        self.btn2_2 = Button(text = "Find Info")
        self.btn2_2.bind(on_press = self.FindPage) 
        self.add_widget(self.btn2_2)
           
    
    def FindPage(self, event):
        
        self.remove_widget(self.btn2_1)
        self.remove_widget(self.btn2_2)
        self.remove_widget(self.loggedinas)
        self.remove_widget(self.labelaccname)
        self.remove_widget(self.labelaccpass)
        self.remove_widget(self.inputaccname)
        self.remove_widget(self.inputaccpass)
        
        #self.back2_1 = Button(text = "<-- Back",
                                #size_hint = (0.5, 0.20))
                                #background_color = "#00ffce"
                                #background_normal = "",
                                #bold = True)
        #self.back2_1.bind(on_press = self.selectionPage)
        #self.add_widget(self.back2_1)
        
        self.label2_1 = Label(text = "Find by id",
                              font_size = 27,
                              color = "#D4AF37")
        self.add_widget(self.label2_1)
        
        self.input2_1 = TextInput(multiline = False,
                                  padding_y = (20, 20)
                                  )
        self.add_widget(self.input2_1)
        
        self.btn2_1 = Button(text = "submit id",
                                size_hint = (1, 0.5),
                                background_color = "#00ffce",
                                #background_normal = "",
                                bold = True)
        self.btn2_1.bind(on_press = self.finder_id) 
        self.add_widget(self.btn2_1)
        
        self.Or = Label(text = "OR")
        self.add_widget(self.Or)
        
        self.label2_2 = Label(text = "Find by name",
                              font_size = 27,
                              color = "#D4AF37")
        self.add_widget(self.label2_2)
        
        self.input2_2 = TextInput(multiline = False,
                                  padding_y = (20, 20))
        self.add_widget(self.input2_2)
        
        self.btn2_2 = Button(text = "submit name",
                                size_hint = (1, 0.5),
                                background_color = "#00ffce",
                                #background_normal = "",
                                bold = True)
       #self.btn2_2.bind(on_press = ) 
        self.add_widget(self.btn2_2)


    def AddDataPage(self, event):
        
        self.remove_widget(self.btn2_2)
        self.remove_widget(self.btn2_1)
        
        self.label3_1 = Label(text = "Name")
        self.add_widget(self.label3_1)
        
        self.input3_1 = TextInput()
        self.add_widget(self.input3_1)
        
        self.btn3_1 = Button(text = "submit")
        self.btn3_1.bind(on_press = self.btn3_1_event)
        self.add_widget(self.btn3_1)
  

    def finder_id(self, event):
        
        self.remove_widget(self.label2_1)
        self.remove_widget(self.btn2_1)
        self.remove_widget(self.label2_2)
        self.remove_widget(self.input2_2)
        self.remove_widget(self.btn2_2)


        
        self.a_text = str(self.input2_1.text)
        
        self.result = Collection.find_one({"_id" : self.a_text}) #self.input2_1.text
        self.ar = self.result["_id"]
        self.br = self.result["name"]
        self.cr = self.result["gr-no"]
        self.dr = self.result["std"]
        self.er = self.result["roll-no"]
        self.fr = self.result["div"]
        self.gr = self.result["e-mail"]
        self.hr = self.result["phone-no"]
        
        self.remove_widget(self.input2_1)
        
        self.Or.text = f"user id - {self.ar} \nuser name - {self.br} \nuser GR.no - {self.cr} \nuser roll.no - {self.er} \nuser std - {self.dr} \nuser div - {self.fr} \nuser number - {self.hr} \nuser e-mail - {self.gr}"
        self.Or.font_size = 28


    def create_account_btn(self, event):
        self.remove_widget(self.loginpage)
        #self.remove_widget(self.inputpass)
        self.remove_widget(self.passbtn_1)
        self.remove_widget(self.blanklabel_1)
        self.remove_widget(self.blanklabel_2)
        self.remove_widget(self.create_account)
        self.remove_widget(self.inputaccname)
        self.remove_widget(self.inputaccpass)
        self.remove_widget(self.labelaccname)
        self.remove_widget(self.labelaccpass)
        
        
        """self.account_label = Label(text = "account name (xyz@alpha.com)",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.account_label)
        
        self.account_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.account_input)
        
        self.add_widget(Label(text = ""))
        
        self.accountpass_label = Label(text = "account password",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.accountpass_label)
        
        self.accountpass_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.accountpass_input)
        
        
        self.add_widget(Label(text = ""))
        self.add_widget(Label(text = ""))"""
        # --
        self.blank_space_1 = Label(text = "",
                                   font_size = 25)
        
        self.gr_label = Label(text = "Gr number ",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.gr_label)
        self.add_widget(self.blank_space_1)
        
        self.gr_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.gr_input)
        # --
        self.blank_space_2 = Label(text = "")
        self.add_widget(self.blank_space_2)
        
        
        self.name_label = Label(text = "Your name ",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.name_label)
        # --
        self.blank_space_3 = Label(text = "")
        self.add_widget(self.blank_space_3)
        
        self.name_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.name_input)
        # --
        self.blank_space_4 = Label(text = "")
        self.add_widget(self.blank_space_4)
        
        self.rollno_label = Label(text = "Roll-number",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.rollno_label)
        self.blank_space_5 = Label(text = "")
        self.add_widget(self.blank_space_5)
        
        self.rollno_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.rollno_input)
        self.blank_space_6 = Label(text = "")
        self.add_widget(self.blank_space_6)
        
        
        self.grade_label = Label(text = "standerd/grade",
                                color = "#ff9100",
                                font_size = 32,)
        self.add_widget(self.grade_label)
        self.blank_space_7 = Label(text = "")
        self.add_widget(self.blank_space_7)
        
        self.grade_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.grade_input)
        self.blank_space_8 = Label(text = "")
        self.add_widget(self.blank_space_8)
        
        
        self.div_label = Label(text = "division [A ,B, C, D]",
                               color = "#ff9100",
                              font_size = 32,)
        self.add_widget(self.div_label)
        self.blank_space_9 = Label(text = "")
        self.add_widget(self.blank_space_9)
        
        self.div_input = TextInput(multiline = False,
                                  padding_y = (5, 5),
                                  size_hint = (5, 2.5))
        self.add_widget(self.div_input)
       
       # --  
        self.blank_space_10 = Label(text = "")
        self.blank_space_11 = Label(text = "")
        self.add_widget(self.blank_space_10)
        self.add_widget(self.blank_space_11)
        
        self.create_account_btn_1 = Button(text = "Next Page",
                                           size_hint = (1, 0.5),
                                            background_color = "#00e700",
                                            background_normal = "",
                                            #text_color = "#1d1500",
                                            bold = True)
        self.create_account_btn_1.bind(on_press = self.create_account_btn_1_event)
        self.add_widget(self.create_account_btn_1)
        
        
    def create_account_btn_1_event(self, event):
        
        if self.gr_input.text == "":
            self.gr_label.text = f"You din't put in your GR number"
            self.gr_label.color = "#FF0000"
            self.gr_label.font_size = 30
            
        elif self.name_input.text == "":
            self.name_label.text = f"You din't put in your Name"
            self.name_label.color = "#FF0000"
            self.name_label.font_size = 30
        else:
            self.remove_widget(self.create_account_btn_1)
            self.remove_widget(self.div_input)
            self.remove_widget(self.div_label)
            self.remove_widget(self.grade_input)
            self.remove_widget(self.grade_label)
            self.remove_widget(self.rollno_input)
            self.remove_widget(self.rollno_label)
            self.remove_widget(self.gr_input)
            self.remove_widget(self.name_input)
            self.remove_widget(self.name_label)
            self.remove_widget(self.rollno_label)
            self.remove_widget(self.rollno_input)
            self.remove_widget(self.gr_label)
            
            self.remove_widget(self.blank_space_1)
            self.remove_widget(self.blank_space_2)
            self.remove_widget(self.blank_space_3)
            self.remove_widget(self.blank_space_4)
            self.remove_widget(self.blank_space_11)
            self.remove_widget(self.blank_space_5)
            self.remove_widget(self.blank_space_6)
            self.remove_widget(self.blank_space_7)
            self.remove_widget(self.blank_space_8)
            self.remove_widget(self.blank_space_9)
            self.remove_widget(self.blank_space_10)
            
            self.impinfo = Label(text = "This Page is very important, please fill care fully.",
                                font_size = 27,
                                color = "#DC143C")
            self.add_widget(self.impinfo)
            self.blank_space__1 = Label(text = "")
            self.add_widget(self.blank_space__1) 
            # ----- 
            self.account_label = Label(text = "account name (xyz@alpha.com)",
                                    color = "#ff9100",
                                    font_size = 32,)
            self.add_widget(self.account_label)
            self.blank_space__2 = Label(text = "")
            self.add_widget(self.blank_space__2) 
            
            self.account_input = TextInput(multiline = False,
                                    padding_y = (5, 5),
                                    size_hint = (5, 2.5))
            self.add_widget(self.account_input)
            
            self.blank_space__3 = Label(text = "")
            self.add_widget(self.blank_space__3) 
            
            self.accountpass_label = Label(text = "account password",
                                    color = "#ff9100",
                                    font_size = 32,)
            self.add_widget(self.accountpass_label)
            self.blank_space__3 = Label(text = "")
            self.add_widget(self.blank_space__3)  
            
            self.accountpass_input = TextInput(multiline = False,
                                    padding_y = (5, 5),
                                    size_hint = (5, 2.5))
            self.add_widget(self.accountpass_input)
            self.blank_space__4 = Label(text = "")
            self.add_widget(self.blank_space__4) 
            
            self.phoneno_label = Label(text = "Phone Number(s)",
                                    color = "#ff9100",
                                    font_size = 32,)
            self.add_widget(self.phoneno_label)
            self.blank_space__5 = Label(text = "")
            self.add_widget(self.blank_space__5) 
            
            self.phoneno_input = TextInput(multiline = False,
                                    padding_y = (5, 5),
                                    size_hint = (5, 2.5))
            self.add_widget(self.phoneno_input)
            self.blank_space__6 = Label(text = "")
            self.add_widget(self.blank_space__6) 
            
            self.email_label = Label(text = "G-mail/e-mail (xyz@gmail.com)",
                                    color = "#ff9100",
                                    font_size = 30,)
            self.add_widget(self.email_label) 
            self.blank_space__7 = Label(text = "")
            self.add_widget(self.blank_space__7)  
            
            self.email_input = TextInput(multiline = False,
                                    padding_y = (5, 5),
                                    size_hint = (5, 2.5))
            self.add_widget(self.email_input)
            self.blank_space__8 = Label(text = "")
            self.add_widget(self.blank_space__8)
            
            self.submit_all_filled_info = Button(text = "Create Account",                
                                                size_hint = (5, 2.5),
                                                background_color = "#00ff00",
                                                background_normal = "",
                                                bold = True)
            self.submit_all_filled_info.bind(on_press = self.db_fill_details)
            self.add_widget(self.submit_all_filled_info)
            
    # CREATEING THE ACCOUNT (BACK END) !!! Next Page
        
    def db_fill_details(self, event):
        self.storage_look_like(self.account_input.text, self.accountpass_input.text, self.name_input.text, self.gr_input.text, self.grade_input.text, self.rollno_input.text, self.div_input.text, self.email_input.text, self.phoneno_input.text, )
        
        
        
        
        
    def storage_look_like(self, a, b, c, d, e, f, g, h, i):
        if self.email_input.text == "":
            self.impinfo.text = f"Error - you need fill email..."
            
        elif self.accountpass_input.text == "":
            self.impinfo.text = f"Error - You dint put in your account password..."
            
        elif len(self.accountpass_input.text) < 4:
            self.impinfo.text = f"The password should be more than 4 charactors..."
            
        elif self.phoneno_input.text == "":
            self.impinfo.text = f"Error - Put at-least 1 phone number..."
            
        else:
            try:
                if a[-10] == "@":
                    if a[-9] == "a":
                        if a[-8] == "l":
                            if a[-7] == "p":
                                if a[-6] == "h":
                                    if a[-5] == "a":
                                        if a[-4] == ".":
                                            if a[-3] == "c":
                                                if a[-2] == "o":
                                                    if a[-1] == "m":
                
                                                        try:
                                                            self.look_like = {
                                                                "_id" : a.lower(),
                                                                "password": b,
                                                                "name": c,
                                                                "gr-no": d,
                                                                "std": e,
                                                                "roll-no": f,
                                                                "div": g,
                                                                "e-mail" : h,
                                                                "phone-no": i,
                                                                "alphamails" : "none",
                                                                "mail-count" : 0
                                                            }
                                                            
                                                            Collection.insert_one(self.look_like)
                                                            
                                                            self.remove_widget(self.account_label)
                                                            self.remove_widget(self.account_input)
                                                            self.remove_widget(self.accountpass_label)
                                                            self.remove_widget(self.accountpass_input)
                                                            self.remove_widget(self.phoneno_label)
                                                            self.remove_widget(self.phoneno_input)
                                                            self.remove_widget(self.email_label)
                                                            self.remove_widget(self.email_input)
                                                            self.remove_widget(self.submit_all_filled_info)
                                                            
                                                            self.impinfo.text = f"Account created ! \nAccount name - {a} \nAccount password - {b}"
                                                            self.impinfo.color = "#00ff00"
                                                        except:
                                                            self.impinfo.text = f"Error - The account name is already taken..."
                else:
                    self.impinfo.text = f"Error - you need to end with '@alpha.com' eg - xyz@alpha.com"
            except:
                self.impinfo.text = f"Error - you need to end with '@alpha.com' eg - xyz@alpha.com"
        
        
        
class ALPHA_app(App):
    def build(self):
        return Main()
    
        
    
if __name__ == "__main__":
    ALPHA_app().run()
    
    
    
    
