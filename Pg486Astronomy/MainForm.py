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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 359)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(783, 93)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(783, 347)
		self._label1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(807, 464)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg486Astronomy"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.label1.Text = x
		x = Mercury
Type Terrestrial
Average distance from the sun 0.387 AU
Mass 3.31 × 1023 kg
Surface temperature –173°C to 430°C
Venus
Type Terrestrial
Average distance from the sun 0.7233 AU
Mass 4.87 × 1024 kg
Surface temperature 472°C
Earth
Type Terrestrial
Average distance from the sun 1 AU
Mass 5.967 × 1024 kg
Surface temperature –50°C to 50°C
Mars
Type Terrestrial
Average distance from the sun 1.5237 AU
Mass 0.6424 × 1024 kg
Surface temperature –140°C to 20°C
Jupiter
Type Jovian
Average distance from the sun 5.2028 AU
Mass 1.899 × 1027 kg
Temperature at cloud tops –110°C
Saturn
Type Jovian
Average distance from the sun 9.5388 AU
Mass 5.69 × 1026 kg
Temperature at cloud tops –180°C
Uranus
Type Jovian
Average distance from the sun 19.18 AU
Mass 8.69 × 1025 kg
Temperature above cloud tops –220°C

The
Astronomy
Helper
Problem

Programming Challenges 487

Neptune
Type Jovian
Average distance from the sun 30.0611 AU
Mass 1.03 × 1026 kg
Temperature at cloud tops –216°C
Pluto
Type Low density
Average distance from the sun 39.44 AU
Mass 1.2 × 1022 kg
Surface temperature –230°C