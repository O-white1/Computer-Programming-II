using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Random;
namespace CatchMe535REAL {
    public partial class Form1 : Form {
        public Form1() 
            { InitializeComponent(); }

        private void Move() {
            System.Threading.Thread.Sleep(3000);
            Form myForm = this.ParentForm;
            int length = myForm.Height;
            int width = myForm.Width;
            Random rndL = new Random(); int newl = rndL.Next(0, length);
            Random rndW = new Random(); int newr = rndW.Next(0, width);

            myForm.button1.Location.X = (rndW);
            button1.Location.Y = (rndL);
        }
       private void main() {
           this.Move();       
        }
       private void button1_Click(object sender, EventArgs e) { Application.Exit(); }

       private void Form1_Load(object sender, EventArgs e)
       {

       }
    }
}
