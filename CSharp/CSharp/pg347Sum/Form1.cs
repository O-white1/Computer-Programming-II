using System;
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
        public Form1() 
            { InitializeComponent(); }
        private void button1_Click(object sender, EventArgs e) { Application.Exit(); }
        private void button2_Click(object sender, EventArgs e) {
            int total = 0;
            int variable = int.Parse(Interaction.InputBox("Prompt Here", "Title"));
            for (int lcv = 0; lcv <= variable; lcv++)
                total += lcv;
            MessageBox.Show(total.ToString());
        }
    }
}
