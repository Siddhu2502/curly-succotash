#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.subscription = self.create_subscription(Image, '/camera/image_raw', self.camera_callback, 10)
        self.subscription

    def camera_callback(self, data):
        # Process and store the camera data here
        # For example, you can save the image to a file

        # Access the image width and height
        width = data.width
        height = data.height

        # Access the image data
        image_data = data.data
        
        print(image_data)

        # Store the image or perform any desired processing

        self.get_logger().info('Camera data stored!')

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
