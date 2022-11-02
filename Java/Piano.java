import javax.swing.*;
import javax.swing.event.*;
import java.awt.event.*;
import java.awt.*;
import javax.sound.midi.*;

public class Piano extends Frame implements ChangeListener {

    Synthesizer synth;
    MidiChannel[] mChannels;
    int keypress = 0;
    int loudn = 0;

    Piano() {

        try {
            synth = MidiSystem.getSynthesizer();
            synth.open();
            mChannels = synth.getChannels();
        } catch (MidiUnavailableException e) {
            JOptionPane.showMessageDialog(null, "Unable to open MIDI.");
        }

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
            w[i].setName("w" + Integer.toString(i));
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
            b[i].setName("b" + Integer.toString(i));
            panel.add(b[i], 1, -1);
        }

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 320);
        frame.setResizable(false);
        frame.setVisible(true);
    }

    @Override
    public void stateChanged(ChangeEvent e) {
        JButton temp = (JButton) e.getSource();
        String btnName = temp.getName();
        if (temp.getModel().isPressed()) {
            System.out.println(btnName + " pressed.");
            switch (btnName) {
                case "w0":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "b0":
                    keypress = 61;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w1":
                    keypress = 62;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "b1":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w2":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w3":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "b2":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w4":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "b3":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w5":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "b4":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;

                case "w6":
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;
            }
        }
    }

    public static void main(String[] args) {
        new Piano();
    }
}