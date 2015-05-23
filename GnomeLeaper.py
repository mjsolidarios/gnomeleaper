import os, sys, inspect, thread, time, pyautogui, math

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = 'lib/x64' if sys.maxsize > 2**32 else 'lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeaperListener(lib.Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(lib.Leap.Gesture.TYPE_SCREEN_TAP);

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()
        finger = frame.fingers.frontmost
        stabilizedPosition = finger.stabilized_tip_position
        interactionBox = frame.interaction_box
        normalizedPosition = interactionBox.normalize_point(stabilizedPosition)
        if finger.type() == 1:
            pyautogui.moveTo(normalizedPosition.x * pyautogui.size()[0], pyautogui.size()[1] - normalizedPosition.y * pyautogui.size()[1], 0)
            for gesture in frame.gestures():
                if gesture.type is lib.Leap.Gesture.TYPE_SCREEN_TAP:
                    screen_tap = LlibLeap.ScreenTapGesture(gesture)
                    print screen_tap
        # pyautogui.PAUSE = 0.1
        # pyautogui.moveTo(normalizedPosition.x * pyautogui.size()[0], pyautogui.size()[1] - normalizedPosition.y * pyautogui.size()[1], 0)
        # if finger.touch_zone > 0:
        #     finger_count = len(frame.fingers)
        #     if finger.touch_zone == 1:
        #         if finger_count < 5:
        #
        #         elif finger_count == 5:
        #             finger_velocity = finger.tip_velocity
        #             print(finger_velocity.x)
        #             print(finger_velocity.y)
        #         else:
        #             print "Finger count: %s" % finger_count
            # elif finger.touch_zone == 2:
            #     if finger_count == 1:
            #         self.cursor.set_left_button_pressed(True)
            #     elif finger_count == 2:
            #         self.cursor.set_left_button_pressed(True)
            #         self.cursor.move(normalizedPosition.x * self.screen_resolution[0], self.screen_resolution[1] - normalizedPosition.y * self.screen_resolution[1])
        # for hand in frame.hands:
        #
        #     handType = "Left hand" if hand.is_left else "Right hand"
        #
        #     # print "  %s, id %d, position: %s" % (
        #     #     handType, hand.id, hand.palm_position)
        #     print hand.palm_position[0]*10
        #     # print pyautogui.position()[0]
        #     # print int()
        #     # pyautogui.moveTo(int(hand.palm_position[0]),None )

def main():
    listener = LeaperListener()
    controller = lib.Leap.Controller()
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
