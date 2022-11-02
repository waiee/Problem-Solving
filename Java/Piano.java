import javax.swing.*;
import javax.swing.event.*;
import java.awt.event.*;
import java.awt.*;

public class Piano extends Frame implements ChangeListener {
    
    Piano() {
        JFrame frame = new JFrame("Pea-Air-Know");
        JButton[] w = new JButton[7];
        JButton[] b = new JButton[6];
        JLayeredPane panel = new JLayeredPane();
        frame.add(panel);

        for (int i = 0; i < 7; i++) {
            w[i] = new JButton();
            w[i].setBackground(Color.WHITE);
            w[i].setLocation(i * 70, 0);
            w[i].setSize(70, 300);
            
            w[i].addChangeListener(this);
            w[i].setName("W"+ Integer.toString(i));
            panel.add(w[i], 0, -1);
        }

        for (int i = 0; i < 6; i++) {
            if (i == 2)
                continue;
            b[i] = new JButton();
            b[i].setBackground(Color.BLACK);
            b[i].setLocation(35 + i * 70, 0);
            b[i].setSize(70, 150);

            b[i].addChangeListener(this);
            b[i].setName("b"+ Integer.toString(i));
            panel.add(b[i], 1, -1);
        }

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 320);
        frame.setResizable(false);
        frame.setVisible(true);
    }

    @Override
    public void stateChanged(ChangeEvent e){
        JButton temp = (JButton)e.getSource();
        String btnName = temp.getName();
        if(temp.getModel().isPressed()){
            System.out.println(btnName+ " pressed.");
        }
    }

    public static void main(String[] args) {
        new Piano();
    }
}