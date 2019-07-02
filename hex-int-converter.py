import sublime
import sublime_plugin

# sublime text drops the Command tail, then converts CamelCase to underscore seperated
# HexIntConverterCommand becomes hex_int_converter
class HexIntConverterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#Get current window
		view = self.view.window()
		#Get current cursor and expand to word sellection
		view.run_command("expand_selection",{"to":"word"})

		#Set selection to first selected only
		sels = self.view.substr(self.view.line(self.view.sel()[0]))

		#If begining of selection is 0x number must be hex
		if sels[:2] == "0x":
			#replace with int representation
			self.view.replace(edit,self.view.sel()[0],str(int(sels, 0)))
		else:
			#replace with hex representation
			self.view.replace(edit,self.view.sel()[0],hex(int(sels)))

class ConvertIntCommand(sublime_plugin.TextCommand):
	def run(self, edit, scope_selector, **kwargs):
		#Get current window
		view = self.view.window()
		#Get current cursor and expand to word sellection
		view.run_command("expand_selection",{"to":"word"})

		#Set selection to first selected only
		sels = self.view.substr(self.view.line(self.view.sel()[0]))

		#replace with hex representation
		self.view.replace(edit,self.view.sel()[0],hex(int(sels)))

	def is_visible(self, scope_selector, **kwargs):
		if self.view.match_selector(self.view.sel()[0].begin(), scope_selector) and scope_selector:
			return self.view.match_selector(self.view.sel()[0].begin(), scope_selector)

class ConvertHexCommand(sublime_plugin.TextCommand):
	def run(self, edit, scope_selector, **kwargs):
		#Get current window
		view = self.view.window()
		#Get current cursor and expand to word sellection
		view.run_command("expand_selection",{"to":"word"})

		#Set selection to first selected only
		sels = self.view.substr(self.view.line(self.view.sel()[0]))

		#replace with int representation
		self.view.replace(edit,self.view.sel()[0],str(int(sels, 0)))

	def is_visible(self, scope_selector, **kwargs):
		if self.view.match_selector(self.view.sel()[0].begin(), scope_selector) and scope_selector:
			return self.view.match_selector(self.view.sel()[0].begin(), scope_selector)