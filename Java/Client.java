

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;
import java.awt.GridBagLayout;
import javax.swing.JTextField;
import java.awt.GridBagConstraints;
import javax.swing.JLabel;
import java.awt.Insets;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.util.TreeMap;
import java.awt.event.ActionEvent;

public class Client extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField inputTxtField;
	private TreeMap<String, String> dictionary;
	private char currentLetter = 'E';
	
	
	
	
	public Client() {
		//*** add parameters for user and server ***
		
		// creates window
		createWindow();
	
	}
	
	public void createWindow() {
		
		
		setTitle("Word Chain Game");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(1280, 720);
		setLocationRelativeTo(null);
	
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setBackground( new Color(138, 74, 243) );
		
		setContentPane(contentPane);
		GridBagLayout gbl_contentPane = new GridBagLayout();
		gbl_contentPane.columnWidths = new int[]{30, 40,30};
		gbl_contentPane.rowHeights = new int[]{100, 100, 100, 100,100, 100,100};
		gbl_contentPane.columnWeights = new double[]{1.0, 1.0, 1.0};
		gbl_contentPane.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
		contentPane.setLayout(gbl_contentPane);
		
		JLabel titleLabel = new JLabel("WORD CHAIN");
		titleLabel.setHorizontalAlignment(SwingConstants.CENTER);
		titleLabel.setFont(new Font("Calibri", Font.BOLD, 20));
		titleLabel.setForeground(Color.WHITE);
		GridBagConstraints gbc_titleLabel = new GridBagConstraints();
		gbc_titleLabel.insets = new Insets(0, 0, 5, 5);
		gbc_titleLabel.gridx = 1;
		gbc_titleLabel.gridy = 1;
		contentPane.add(titleLabel, gbc_titleLabel);
		
		JLabel instrutionLabel = new JLabel("Word That Starts With "+getCurrentLetter());
		instrutionLabel.setForeground(Color.WHITE);
		GridBagConstraints gbc_instrutionLabel = new GridBagConstraints();
		gbc_instrutionLabel.insets = new Insets(0, 0, 5, 5);
		gbc_instrutionLabel.gridx = 1;
		gbc_instrutionLabel.gridy = 2;
		contentPane.add(instrutionLabel, gbc_instrutionLabel);
		
		inputTxtField = new JTextField();
		inputTxtField.setHorizontalAlignment(SwingConstants.CENTER);
		inputTxtField.setFont(new Font("Calibri", Font.PLAIN, 20));
		GridBagConstraints gbc_inputTxtField = new GridBagConstraints();
		gbc_inputTxtField.fill = GridBagConstraints.BOTH;
		gbc_inputTxtField.insets = new Insets(0, 0, 5, 5);
		gbc_inputTxtField.gridx = 1;
		gbc_inputTxtField.gridy = 3;
		contentPane.add(inputTxtField, gbc_inputTxtField);
		inputTxtField.setColumns(10);
		
		JLabel feedbackLabel = new JLabel("");
		feedbackLabel.setForeground(new Color(0, 0, 0));
		GridBagConstraints gbc_feedbackLabel = new GridBagConstraints();
		gbc_feedbackLabel.insets = new Insets(0, 0, 0, 5);
		gbc_feedbackLabel.gridx = 1;
		gbc_feedbackLabel.gridy = 5;
		contentPane.add(feedbackLabel, gbc_feedbackLabel);
		
		JButton submitBtn = new JButton("Submit");
		submitBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			
				// if not match 
				submit();
			}

			private void submit() {
		
		    	String input = inputTxtField.getText().toUpperCase();
				// if match
				if(input.length() > 0 && input.charAt(0)== getCurrentLetter()) {
					setCurrentLetter(input.charAt(input.length()-1));
					
					instrutionLabel.setText("Word That Starts With "+getCurrentLetter());
					feedbackLabel.setText("GREAT!!!!");
					feedbackLabel.setForeground(Color.green);
					inputTxtField.setText("");
				} else {
				
					feedbackLabel.setText("Sorry, Try Again!!!!");
					feedbackLabel.setForeground(Color.red);
				
					
				}
				
				    
			}
		});
		GridBagConstraints gbc_submitBtn = new GridBagConstraints();
		gbc_submitBtn.insets = new Insets(0, 0, 5, 5);
		gbc_submitBtn.gridx = 1;
		gbc_submitBtn.gridy = 4;
		contentPane.add(submitBtn, gbc_submitBtn);
		
		
		
		
		setVisible(true);
	}

	public boolean isInDictionary(String word) {
		return dictionary.containsKey(word);
	}

	public void setDictionary(TreeMap<String, String> dictionary) {
		this.dictionary = dictionary;
	}

	public char getCurrentLetter() {
		return currentLetter;
	}

	public void setCurrentLetter(char currentLetter) {
		this.currentLetter = currentLetter;
	}
   
}
