import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular shades Add $0",
			"Folding shades Add $10",
			"Roman shades Add $15"]))
		self._comboBox1.Location = System.Drawing.Point(12, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 1
		self._comboBox1.Text = "Styles"
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 inches wide Add $0",
			"27 inches wide Add $2",
			"32 inches wide Add $4",
			"40 inches wide Add $6"]))
		self._comboBox2.Location = System.Drawing.Point(139, 12)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(527, 21)
		self._comboBox2.TabIndex = 2
		self._comboBox2.Text = "Sizes"
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural Add $5",
			"Blue Add $0",
			"Teal Add $0",
			"Red Add $0",
			"Green Add $0"]))
		self._comboBox3.Location = System.Drawing.Point(672, 12)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 3
		self._comboBox3.Text = "Colors"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 61)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 102)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 102)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(175, 102)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(805, 456)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "Pg485ShadeDesigner"
		self.ResumeLayout(False)
		
		

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button1Click(self, sender, e):
		indexStyles = self._comboBox1.SelectedIndex
		indexSizes = self._comboBox2.SelectedIndex
		indexColor = self._comboBox3.SelectedIndex
		cost = 50
		
		costStyle = [0,10,15]
		costSizes = [0,2,4,6]
		costColor = [5,0,0,0,0]
		
		cost = costStyle[indexStyles] + costSizes[indexSizes] + costColor[indexColor]
		self._label1.Text = str(cost)
		
		