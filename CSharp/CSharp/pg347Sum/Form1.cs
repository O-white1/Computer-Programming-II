﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;
namespace pg347Sum {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }
        private void button2_Click(object sender, EventArgs e) {
            string variable = Interaction.InputBox("Prompt Here", "Title");
            MessageBox.Show(variable);
        }
    }
}