import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 373)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(131, 98)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.Font = System.Drawing.Font("Microsoft Uighur", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(149, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(558, 361)
		self._label1.TabIndex = 1
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(149, 373)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(558, 98)
		self._button2.TabIndex = 5
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(713, 373)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(131, 98)
		self._button3.TabIndex = 6
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(856, 483)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "AboutMe"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "I am cool"

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		self._label1.Text = ""