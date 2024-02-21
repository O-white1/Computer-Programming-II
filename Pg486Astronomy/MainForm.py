import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(268, 93)
		self._button1.TabIndex = 0
		self._button1.Text = "Mercury"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gray
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 111)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(268, 93)
		self._button2.TabIndex = 1
		self._button2.Text = "Venus"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gray
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 210)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(268, 93)
		self._button3.TabIndex = 2
		self._button3.Text = "Earth"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Gray
		self._button4.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(12, 309)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(268, 93)
		self._button4.TabIndex = 3
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = False
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Gray
		self._button5.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(527, 12)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(268, 93)
		self._button5.TabIndex = 4
		self._button5.Text = "Saturn"
		self._button5.UseVisualStyleBackColor = False
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.Gray
		self._button6.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(527, 111)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(268, 93)
		self._button6.TabIndex = 5
		self._button6.Text = "Uranus"
		self._button6.UseVisualStyleBackColor = False
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.Gray
		self._button7.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(527, 210)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(268, 93)
		self._button7.TabIndex = 6
		self._button7.Text = "Neptune"
		self._button7.UseVisualStyleBackColor = False
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.Gray
		self._button8.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(527, 309)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(268, 93)
		self._button8.TabIndex = 7
		self._button8.Text = "Pluto"
		self._button8.UseVisualStyleBackColor = False
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Gray
		self._button9.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(286, 12)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(235, 390)
		self._button9.TabIndex = 8
		self._button9.Text = "Jupitar"
		self._button9.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(807, 411)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg486Astronomy"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pass