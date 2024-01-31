import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.WhiteSmoke
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(124, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Time of day:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.WhiteSmoke
		self._label2.Location = System.Drawing.Point(247, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(227, 53)
		self._label2.TabIndex = 1
		self._label2.Text = "Length of Call (minutes):"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Maroon
		self._radioButton1.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.ForeColor = System.Drawing.Color.WhiteSmoke
		self._radioButton1.Location = System.Drawing.Point(12, 44)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(236, 35)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "DayTime(6:00AM - 5:59 PM)"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Maroon
		self._radioButton2.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.ForeColor = System.Drawing.Color.WhiteSmoke
		self._radioButton2.Location = System.Drawing.Point(12, 74)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(236, 35)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening(6:00PM - 11:59PM)"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Maroon
		self._radioButton3.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.ForeColor = System.Drawing.Color.WhiteSmoke
		self._radioButton3.Location = System.Drawing.Point(12, 104)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(236, 35)
		self._radioButton3.TabIndex = 4
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off Peak(12:00AM - 5:59PM)"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Silver
		self._textBox1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.WhiteSmoke
		self._textBox1.Location = System.Drawing.Point(263, 44)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(211, 37)
		self._textBox1.TabIndex = 5
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.WhiteSmoke
		self._label3.Location = System.Drawing.Point(247, 201)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 32)
		self._label3.TabIndex = 6
		self._label3.Text = "Cost:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Silver
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(19, 201)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 144)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(19, 351)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 40)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Silver
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(19, 397)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 40)
		self._button3.TabIndex = 9
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Silver
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.WhiteSmoke
		self._label4.Location = System.Drawing.Point(309, 201)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(165, 43)
		self._label4.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(486, 449)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg272_Long_Distance"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		calltime = int(self._textBox1.Text)
		todc = 0 #time of day charge
		if self._radioButton1.Enabled == True:
			todc = 0.07
		if self._radioButton2.Enabled == True:
			todc = 0.12
		if self._radioButton2.Enabled == True:
			todc = 0.05
		self._label4.Text = ("$" + str(todc*calltime))

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()