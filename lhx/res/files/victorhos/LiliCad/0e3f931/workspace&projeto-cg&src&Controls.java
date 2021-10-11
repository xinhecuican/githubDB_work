import java.awt.*;
import java.applet.Applet;

public class Controls extends Applet {
  /* Declaration */
  private Label DemoLabel;
  private Button DemoButton;
  private Scrollbar DemoSlider;
  private Checkbox DemoRadio;
  private Checkbox DemoBox;
  private TextField DemoText;
  private TextArea DemoArea;
  private Choice DemoCombo;
  private List DemoList;
  private LayoutManager Layout;
  private CheckboxGroup Group;

  public Controls () {
    /* Instantiation */
    DemoLabel = new Label ();
    DemoSlider = new Scrollbar ();
    Group = new CheckboxGroup ();
    DemoRadio = new Checkbox ("Checkbox", Group, false);
    DemoBox = new Checkbox ();
    DemoButton = new Button ();
    DemoText = new TextField ();
    DemoCombo = new Choice ();
    DemoList = new List (3);
    DemoArea = new TextArea (5, 30);
    Layout = new FlowLayout ();

    /* Location */
    setLayout (Layout);
    add (DemoLabel);
    add (DemoButton);
    add (DemoRadio);
    add (DemoBox);
    add (DemoText);
    add (DemoList);
    add (DemoCombo);
    add (DemoArea);
    add (DemoSlider);
    
    /* Decoration */
    DemoLabel.setText ("Label");
    DemoSlider.setName ("Scrollbar");
    DemoButton.setLabel ("Button");
    DemoBox.setLabel ("Checkbox");
    DemoText.setText ("TextField");
    DemoCombo.addItem ("Choice");
    DemoCombo.addItem ("Selection");
    DemoList.add ("List");
    DemoList.add ("Selection");
    DemoArea.setText ("TextArea");
  }

}