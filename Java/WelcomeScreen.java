

import java.awt.*;
import javax.swing.*;
import javax.swing.border.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class WelcomeScreen extends JFrame {

	private JPanel contentPane;


	public static void main(String[] args) {
		
				try {
					WelcomeScreen frame = new WelcomeScreen();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
		
	}

	/**
	 * Create the frame.
	 */
	public WelcomeScreen() {
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setTitle("Word Chain Game - WELCOME");
		setSize(1280, 720);
		setLocationRelativeTo(null);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		getContentPane().setBackground( new Color(138, 74, 243) );
		
		
		JLabel welcomeLabel = new JLabel("Word Chain");
		welcomeLabel.setFont(new Font("Calibri", Font.BOLD, 20));
		welcomeLabel.setForeground(Color.WHITE);
		welcomeLabel.setHorizontalAlignment(SwingConstants.CENTER);
		welcomeLabel.setBounds(515, 168, 250, 102);
		contentPane.add(welcomeLabel);
		
		JButton playBtn = new JButton("Play");
		playBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				init();
			}
		});
		playBtn.setBounds(591, 342, 100, 39);
		// playBtn.setBackground( new Color(225, 225, 225) );
		 playBtn.setBorder(null);
		 playBtn.setFocusPainted(false);
		
		contentPane.add(playBtn);
		

	}

	protected void init() {
		// TODO Auto-generated method stub
		System.out.println("initializing game");
		dispose();
		Client client = new Client();
	}
	
	
}
