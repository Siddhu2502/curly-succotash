#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserNode(Node):
    def __init__(self):
        super().__init__('laser_node')
        self.subscription = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        self.subscription
        
    def laser_callback(self, data):
        # Access the laser scan data
        ranges = data.ranges
        angle_increment = data.angle_increment
        angle_min = data.angle_min

        # Process the laser scan data
        for i, range_value in enumerate(ranges):
            angle = angle_min + i * angle_increment
            x = range_value * math.cos(angle)
            y = range_value * math.sin(angle)

            # Check if an object is detected
            if range_value < data.range_max:
                print(f"Object detected at ({x:.2f}, {y:.2f}) with range {range_value:.2f} meters.")
            else:
                continue

def main(args= None):
    rclpy.init(args=args)
    laser_node = LaserNode()
    rclpy.spin(laser_node)
    laser_node.destroy_node()
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()