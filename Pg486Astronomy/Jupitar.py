
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Jupitar(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 163)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(255, 34)
		self._button1.TabIndex = 19
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGray
		self._label4.Location = System.Drawing.Point(12, 129)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(253, 31)
		self._label4.TabIndex = 18
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGray
		self._label3.Location = System.Drawing.Point(12, 89)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(253, 31)
		self._label3.TabIndex = 17
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGray
		self._label2.Location = System.Drawing.Point(12, 49)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(253, 31)
		self._label2.TabIndex = 16
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGray
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(253, 31)
		self._label1.TabIndex = 15
		# 
		# Jupitar
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(276, 212)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "Jupitar"
		self.Text = "Jupitar"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.label1_.Text = "Type:  Jovian"
		self.label2_.Text = "Average distance from the sun:  5.2028 AU"
		self.label3_.Text = "Mass:  1.899 × 10**27 kg"
		self.label4.Text = "Surface Tempurature:  –220°C"