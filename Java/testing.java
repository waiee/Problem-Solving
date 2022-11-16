import javax.swing.*;
import javax.swing.JComboBox.KeySelectionManager;
import javax.swing.event.*;
import java.awt.event.*;
import java.awt.*;
import javax.sound.midi.*;


public class testing implements KeyListener {

        Synthesizer synth;
        MidiChannel[] mChannels;
        int keypress = 0;
        int loudn = 0;
        
    
        @Override
        public void keyReleased(KeyEvent e) {
            switch (e.getKeyChar()) {
                case 'q':
                    keypress = 60;
                    loudn = 120;
                    mChannels[0].noteOn(keypress, loudn);
                break;
        }
    
    }}
