import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 61)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(123, 23)
		self._label1.TabIndex = 0
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(112, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 108)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(123, 66)
		self._button1.TabIndex = 2
		self._button1.Text = "Check"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 15)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Word:"
		self._label2.Click += self.Label2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(816, 483)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StringInterview3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		word = self._textBox1.Text
		wordi = []
		for i in len(word):
			wordi.append(i)
			if wordi.count(wordi[i]) == 1:
				self._label1.Text = str(wordi[i])
				return