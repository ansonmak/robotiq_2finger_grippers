#! /usr/bin/env python
import rospy

# Brings in the SimpleActionClient
import actionlib

from robotiq_2f_gripper_msgs.msg import CommandRobotiqGripperFeedback, CommandRobotiqGripperResult, CommandRobotiqGripperAction, CommandRobotiqGripperGoal
from robotiq_2f_gripper_control.robotiq_2f_gripper_driver import Robotiq2FingerGripperDriver as Robotiq

rospy.init_node('robotiq_controller')

action_name = rospy.get_param('~action_name', 'command_robotiq_action')
robotiq_client = actionlib.SimpleActionClient(action_name, CommandRobotiqGripperAction)
robotiq_client.wait_for_server()

def control_gripper():

    while not rospy.is_shutdown():
        print("Go to (0-1000): ")
        x = float(input())
        width = x/1000 * 0.085
        Robotiq.goto(robotiq_client, pos=width, speed=0.1, force=1, block=True)

if __name__ == '__main__':
    control_gripper()