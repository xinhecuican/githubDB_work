package views;

public class Start {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Gui gui = new Gui();
		DesktopTest4 dt = new DesktopTest4();
		gui.setDt(dt);
		dt.setGui(gui);
	}

}
