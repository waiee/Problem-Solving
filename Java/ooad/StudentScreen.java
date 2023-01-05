package ooad;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class StudentScreen implements ActionListener{
    int count = 0;
    JLabel clickLabel;

    public StudentScreen(){

        JFrame frame = new JFrame();

        JButton button = new JButton("View Subject");
        button.addActionListener(this);
        JLabel label = new JLabel("Welcome to Student Screen");
        clickLabel = new JLabel("Number of clicks: 0");

        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        panel.setLayout(new GridLayout(0, 1));
        panel.add(label);
        panel.add(button);
        panel.add(clickLabel);

        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Student Screen");
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) {
       new StudentScreen();
    }

    @Override
    public void actionPerformed(ActionEvent e){
        count++;
        clickLabel.setText("Number of clicks: " + count);
    }
}
