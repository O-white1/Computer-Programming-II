
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.myparent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(74, 88)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Name = "Form2"
		self.Text = "Form2"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, world!")
		form1.Show()
		self.Hide()
	