import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 293)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 55)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(13, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(434, 24)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(119, 293)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(221, 55)
		self._button2.TabIndex = 3
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(346, 293)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 55)
		self._button3.TabIndex = 4
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(13, 42)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(434, 24)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 101)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(434, 136)
		self._label3.TabIndex = 7
		self._label3.Text = "label3"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(459, 360)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "LP3-7"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		from ClLp37 import * # import ClLp37
		obj1 = ClLp37(num1, num2)
		obj2 = ClLp37(num2, num1)
		obj1.calc()
		obj2.calc()
		div1, mod1 = obj1.GetDivMod()
		div2, mod2 = obj2.GetDivMod()
		self._label3.Text = str(num1) + "/" + str(num2) + "=" + str(div1) + "\n"
		self._label3.Text += str(num1) + "%" + str(num2) + "=" + str(mod1) + "\n\n"
		self._label3.Text += str(num2) + "/" + str(num1) + "=" + str(div2) + "\n"
		self._label3.Text += str(num2) + "%" + str(num1) + "=" + str(mod2) + "\n"

	def Button1Click(self, sender, e):
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()