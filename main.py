from kivy.app import App

from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock
#
from kivy.factory import Factory
from kivy.uix.screenmanager import *
from kivy.core.window import Window

#Declarations of the classes used in the kv files
class MainBody(ScreenManager): pass
class LoginForm(Widget): pass
class ConfPopup(Popup): pass
class ErrorPopup(Popup): pass

Builder.load_file('login.kv')
			
class LoginPage(Screen):
	loginForm=LoginForm()
	def __init__(self,):
		super(LoginPage, self).__init__()
		self.pages=["login page", "next page"]
			
	def switchTo(self, n):
		self.manager.transition=NoTransition()
		self.manager.current=self.pages[n]


class MailApp(App):
	confPopup=ConfPopup(size_hint=[None, None],size=(400,250), pos_hint={'center_x':.5, 'center_y':.5})
	loginpage=LoginPage()
	def build(self):
		self.main=MainBody()
		self.main.transition.direction="left"
		self.main.add_widget(self.loginpage)

		Window.bind(on_request_close=self.returnLastPage)
		
		return self.main
	
	def returnLastPage(self, useless ,source=None):
		i=self.loginpage.pages.index(self.main.current)
		if i != 0:
			self.main.current=self.loginpage.pages[i-1]
		else:
			self.exitConfirmation()
		return True
	def exitConfirmation(self):
		self.confPopup.open()
	
				
	
if __name__=="__main__":
	MailApp().run()
	exit()