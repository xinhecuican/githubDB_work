import java.awt.*;        // using AWT containers and components
import java.awt.event.*;  // using AWT events and listener interfaces
 
// An AWT GUI program inherits the top-level container java.awt.Frame
public class AWTAccumulator extends Frame implements ActionListener {
   private Label lblInput;     // declare input Label
   private Label lblOutput;    // declare output Label
   private TextField tfInput;  // declare input TextField
   private TextField tfOutput; // declare output TextField
   private int numberIn;       // input number
   private int sum = 0;        // accumulated sum, init to 0
 
   /** Constructor to setup the GUI */
   public AWTAccumulator() {
      setLayout(new FlowLayout());
         // "this" Frame sets layout to FlowLayout, which arranges the components
         //  from left-to-right, and flow to next row from top-to-bottom.
 
      lblInput = new Label("Enter an Integer: "); // construct Label
      add(lblInput);               // "this" Frame adds Label
 
      tfInput = new TextField(10); // construct TextField
      add(tfInput);                // "this" Frame adds TextField
 
      // The TextField tfInput registers "this" object (AWTAccumulator)
      //  as an ActionEvent listener.
      tfInput.addActionListener(this);
 
      lblOutput = new Label("The Accumulated Sum is: ");  // allocate Label
      add(lblOutput);               // "this" Frame adds Label
 
      tfOutput = new TextField(10); // allocate TextField
      tfOutput.setEditable(false);  // read-only
      add(tfOutput);                // "this" Frame adds TextField
 
      setTitle("AWT Accumulator");  // "this" Frame sets title
      setSize(350, 120);  // "this" Frame sets initial window size
      setVisible(true);   // "this" Frame shows
   }
 
   /** The entry main() method */
   public static void main(String[] args) {
      // Invoke the constructor to setup the GUI, by allocating an anonymous instance
      new AWTAccumulator();
   }
 
   /** Event handler - Called back when user hits the enter key on the TextField */
   @Override
   public void actionPerformed(ActionEvent evt) {
      // Get the String entered into the TextField tfInput, convert to int
      numberIn = Integer.parseInt(tfInput.getText());
      sum += numberIn;      // accumulate numbers entered into sum
      tfInput.setText("");  // clear input TextField
      tfOutput.setText(sum + ""); // display sum on the output TextField
                                  // convert int to String
   }
}