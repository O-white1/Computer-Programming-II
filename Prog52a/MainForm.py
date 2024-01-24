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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(203, 48)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Length:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._textBox1.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(221, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(490, 47)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(384, 165)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(220, 48)
		self._button1.TabIndex = 2
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._textBox2.Font = System.Drawing.Font("Microsoft Uighur", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(221, 61)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(490, 39)
		self._textBox2.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(203, 48)
		self._label2.TabIndex = 3
		self._label2.Text = "Enter Width:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 105)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(221, 54)
		self._label3.TabIndex = 5
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 159)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(221, 54)
		self._label4.TabIndex = 6
		self._label4.Text = "Width:"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(221, 105)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(157, 54)
		self._label5.TabIndex = 7
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(221, 159)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(157, 54)
		self._label6.TabIndex = 8
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 219)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(592, 76)
		self._button2.TabIndex = 9
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(384, 105)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(220, 54)
		self._button3.TabIndex = 10
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(798, 441)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label4Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		len = int(self._textBox1.Text)
		wid = int(self._textBox2.Text)
		area = len * wid
		perim = len * 2 + wid * 2
		self._label5.Text = str(area)
		self._label6.Text = str(perim)

	def Button1Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._textBox1.Text = ""
		self._textBox1.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()