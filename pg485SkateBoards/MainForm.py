import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Silver
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 191)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.Silver
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(218, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(201, 191)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Truck Assemblies"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.Silver
		self._groupBox3.Controls.Add(self._radioButton13)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(425, 12)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(200, 191)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Wheel Sets"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(188, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Master Thrasher    $60"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 49)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(188, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Dictator of Grind    $45"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 79)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(188, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Street King                $50"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(6, 19)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(189, 24)
		self._radioButton4.TabIndex = 0
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "7.75 axle $35"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(6, 49)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(189, 24)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "8 axle       $40"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(6, 79)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(189, 24)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "8.5 axle   $45"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(6, 22)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(188, 32)
		self._radioButton7.TabIndex = 0
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "51    $20"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(6, 49)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(188, 25)
		self._radioButton8.TabIndex = 1
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "55   $22"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(6, 79)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(188, 24)
		self._radioButton9.TabIndex = 2
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "58    $24"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.Silver
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton10)
		self._groupBox4.Controls.Add(self._radioButton11)
		self._groupBox4.Controls.Add(self._radioButton12)
		self._groupBox4.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox4.Location = System.Drawing.Point(631, 12)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(192, 191)
		self._groupBox4.TabIndex = 3
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Services"
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(6, 79)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(180, 33)
		self._radioButton10.TabIndex = 2
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "Riser pads $2"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(6, 49)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(180, 33)
		self._radioButton11.TabIndex = 1
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Bearings  $30"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(6, 19)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(180, 35)
		self._radioButton12.TabIndex = 0
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "GripTape  $10"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# radioButton13
		# 
		self._radioButton13.Location = System.Drawing.Point(6, 109)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(188, 24)
		self._radioButton13.TabIndex = 3
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "61    $28"
		self._radioButton13.UseVisualStyleBackColor = True
		# 
		# radioButton14
		# 
		self._radioButton14.Location = System.Drawing.Point(6, 118)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(180, 33)
		self._radioButton14.TabIndex = 3
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "Nuts and bolts kit $3"
		self._radioButton14.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 361)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 77)
		self._button1.TabIndex = 4
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gray
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(164, 361)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(501, 77)
		self._button2.TabIndex = 5
		self._button2.Text = "Calc"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gray
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(671, 361)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(146, 77)
		self._button3.TabIndex = 6
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGray
		self._label1.Font = System.Drawing.Font("Papyrus", 48, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 222)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(805, 126)
		self._label1.TabIndex = 7
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radioButton15
		# 
		self._radioButton15.Location = System.Drawing.Point(6, 157)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(180, 24)
		self._radioButton15.TabIndex = 4
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "Assembly $10"
		self._radioButton15.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(835, 450)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Font = System.Drawing.Font("Microsoft Uighur", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)
	
	
	

	def Button2Click(self, sender, e):
		board = 0
		TA  = 0
		wheels = 0
		srv = 0
		
		
		if self._radioButton1.Checked == True:
			board = 60 # this is cost
		elif self._radioButton2.Checked == True:
			board = 45
		elif self._radioButton3.Checked == True:
			board = 50
		
		
		if self._radioButton4.Checked == True:
			TA = 35 # also price
		if self._radioButton5.Checked == True:
			TA = 40
		if self._radioButton6.Checked == True:
			TA = 45
	
		if self._radioButton7.Checked == True:
			wheels = 20
		if self._radioButton8.Checked == True:
			wheels = 22
		if self._radioButton9.Checked == True:
			wheels = 24
		if self._radioButton13.Checked == True:
			wheels = 28
		
		if self._radioButton12.Checked == True:
			srv=10
		if self._radioButton11.Checked == True:
			srv=30
		if self._radioButton10.Checked == True:
			srv=2
		if self._radioButton14.Checked == True:
			srv=3
		if self._radioButton15.Checked == True:
			srv=10

		tot = (srv+wheels+TA+board)*1.06
		self._label1.Text = str("$" + str(tot))
		
		
		
		
		





































	def Button1Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()