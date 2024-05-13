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

namespace Pg498PayRoll {
    public partial class Form1 : Form {
        const decimal decHOURLY_PAY_RATE = 0.6m;
        const int intMAX_EMPLOYEES = 5;
        public Form1() {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e) { }
        private void button1_Click(object sender, EventArgs e) {
            int[] intHours = new int[intMAX_EMPLOYEES]; // new[5]
            // new int array new[] of capacity: employees__ arrays are a fixed size
            int intCount = 0;           // loop control varaible
            int intEmpHours = 0;       // hours
            decimal decEmpPay = 0.0m; // gross pay
            for (intCount = 0; intCount <= intMAX_EMPLOYEES; intCount++) {
                while (int.TryParse(Interaction.InputBox("Enter hours worked by Employee #" +(intCount+1).ToString(), "Need Hours Worked"), out intEmpHours) == false {  MessageBox.Show("Please enter an integer for hours worked");
                intHours[intCount] = intEmpHours;
            }
            listBox1.Items.Clear();
            for (intCount = 0; intCount <= intMAX_EMPLOYEES; intCount++) {
                decEmpPay = intHours[intCount] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee" + (intCount+1).ToString() + " Earned " + decEmpPay.ToString("$.00"));
            }

        }

    }
    }
}
