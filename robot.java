/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package frc.robot;

import edu.wpi.first.wpilibj.networktables.NetworkTable;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.VictorSP;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.SpeedControllerGroup;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.wpilibj.livewindow.LiveWindow;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;


public class Robot extends IterativeRobot {
	private VictorSP sagmotor1 = new VictorSP(0);
	private VictorSP sagmotor2 = new VictorSP(1);
	private VictorSP solmotor1 = new VictorSP(2);
	private VictorSP solmotor2 = new VictorSP(3);
	private Joystick stick = new Joystick(0);
	private Timer m_timer = new Timer();
  
  SpeedControllerGroup sagtekerler = new SpeedControllerGroup(sagmotor1, sagmotor2);
  SpeedControllerGroup soltekerler = new SpeedControllerGroup(solmotor1, solmotor2);
  private final DifferentialDrive robotDrive = new DifferentialDrive(soltekerler,sagtekerler);

	public static NetworkTable table1 = NetworkTable.getTable("Vision"); // vision adında table çekilioyr


	@Override
	public void robotInit() {
	}


	@Override
	public void autonomousInit() {
		m_timer.reset();
		m_timer.start();
	}
	
	public static double konumX()
	{
		return table1.getNumber("X", 0.0); //Pythondan gelen x kordinati
	}
	public static double kas() 
	{
		return table1.getNumber("kas", 0.0); //pythondan gelen kas datasi
	}


	@Override
	public void autonomousPeriodic() {

	}

	@Override
	public void teleopInit() {
	}


	@Override
	public void teleopPeriodic() {

    robotDrive.setMaxOutput(0.3);//Robotun maximum hızı

    if(kas()> 300){ // gelen kas datasi 300den buyukse
     robotDrive.arcadeDrive(0.3, 0.0); // ileri git
}
    else{ //buyuk degilse
     robotDrive.arcadeDrive(0.0, 0.0); // dur
}


    if(konumX() == 0){ // el degeri 0'sa hareket etme
      sagmotor1.set(0); 
			sagmotor2.set(0);
      solmotor1.set(0); 
			solmotor2.set(0);
    }
		else if(konumX() < 400) // degerler 400'den kucukse saga don
		{
			sagmotor1.set(0.3); // sag motorları calistir
			sagmotor2.set(0.3);
		}
	  else if (konumX() > 600) // degerler 600'den buyukse sola don
		{
			solmotor1.set(0.3); //sol motorlari calistir
			solmotor2.set(0.3);
    }


		SmartDashboard.putNumber("El konumu: ", konumX()); // smartdashboarda x konumu yazdır
		SmartDashboard.putNumber("Kas Datasi: ", kas()); // smartdashboarda kas datasını yazdır

	}


	@Override
	public void testPeriodic() {
	}
}
