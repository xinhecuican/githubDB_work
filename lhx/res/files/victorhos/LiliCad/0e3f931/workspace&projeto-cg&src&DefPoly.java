// DefPoly.java: Drawing a polygon.

// Copied from Section 1.5 of
//    Ammeraal, L. and K. Zhang (2007). Computer Graphics for Java Programmers, 2nd Edition,
//       Chichester: John Wiley.

// Uses: CvDefPoly (discussed below).
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class DefPoly extends Frame {

	public static void main(String[] args) {
		new DefPoly();
	}

	DefPoly() {
		super("Define polygon vertices by clicking");

		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});

		Panel panelButtons = new Panel(new GridLayout(4, 3));
		
		Checkbox checkRotacao = new Checkbox ("Rota??o", false);
		Checkbox checkTranslacao = new Checkbox ("Transla??o", false);
		Checkbox checkCisalhamento = new Checkbox ("Cisalhamento", false);
		Checkbox checkEscalonamento = new Checkbox ("Escalonamento", false);
		Checkbox checkEspelhamento = new Checkbox ("Espelhamento", false);
		
		panelButtons.add(checkRotacao);
		panelButtons.add(checkTranslacao);
		panelButtons.add(checkCisalhamento);
		panelButtons.add(checkEscalonamento);
		panelButtons.add(checkEspelhamento);
		
		/*
		 
		Button checkRotacao = new Button("Rota??o");
		Button checkTranslacao = new Button("Transla??o");
		Button checkCisalhamento = new Button("Cisalhamento");
		Button checkEscalonamento = new Button("Escalonamento");
		Button checkEspelhamento = new Button("Espelhamento");

		Button botaoRotacao = new Button("Rota??o");
		Button botaoTranslacao = new Button("Transla??o");
		Button botaoCisalhamento = new Button("Cisalhamento");
		Button botaoEscalonamento = new Button("Escalonamento");
		Button botaoEspelhamento = new Button("Espelhamento");

		ActionListener action = new MyActionListener();

		add(BorderLayout.WEST, botaoRotacao);
		add(BorderLayout.WEST, botaoTranslacao);
		add(BorderLayout.WEST, botaoCisalhamento);
		add(BorderLayout.WEST, botaoEscalonamento);
		add(BorderLayout.EAST, botaoEspelhamento);

		botaoRotacao.addActionListener(action);
		botaoTranslacao.addActionListener(action);
		botaoCisalhamento.addActionListener(action);
		botaoEscalonamento.addActionListener(action);
		botaoEspelhamento.addActionListener(action);
		*/

		add("Center", new CvDefPoly());
	    add(panelButtons, BorderLayout.WEST);

	    setSize(800, 600);
		setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
		show();
	}

}

class MyActionListener implements ActionListener {
	public void actionPerformed(ActionEvent ae) {
		String s = ae.getActionCommand();
		if (s.equals("Exit")) {
			System.exit(0);
		} else if (s.equals("Rota??o")) {
			System.out.println("Good Morning");
		} else {
			System.out.println(s + " clicked");
		}
	}
}
