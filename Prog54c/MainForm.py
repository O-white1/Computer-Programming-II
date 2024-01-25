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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(4, 337)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 101)
		self._button1.TabIndex = 0
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(239, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(127, 36)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter Radius:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(356, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(247, 37)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.White
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(175, 337)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(454, 101)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.White
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(635, 337)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 101)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(239, 49)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(223, 38)
		self._label2.TabIndex = 5
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(239, 87)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(223, 36)
		self._label3.TabIndex = 6
		self._label3.Text = "Circumference:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(449, 49)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(154, 38)
		self._label4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(449, 87)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(154, 36)
		self._label5.TabIndex = 8
		self._label5.Click += self.Label5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(820, 453)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label5Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		rad = int(self._textBox1.Text)
		pi = 3.14159
		circ = 2 * (rad * pi)
		area = (pi * (rad*rad))
		self._label4.Text = str(area)
		self._label5.Text = str(circ)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()