from objects_on_road_processor import ObjectsOnRoadProcessor
import cv2
import time

class TEST(object):
    def __init__(self):
        processor = ObjectsOnRoadProcessor(self)
        file = 'C:/Users/iiile/Auto_project/Autonomous-car/AI-self-driving-RC-car/code/test/data/tmp/obj_test.png'
        # cap = cv2.VideoCapture(file)
        # while cap.isOpened():
        #     start_time = time.time()
        #     try:
        #         _, frame = cap.read()

        #         combo_image = processor.process_objects_on_road(frame)

        #         # FPS
        #         elapse_time = time.time() - start_time
        #         fps = 1/elapse_time
                
        #         cv2.putText(combo_image, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        #         cv2.imshow('frame', combo_image)

        #         if cv2.waitKey(1) & 0xFF == ord('q'):
        #             cap.release()
        #             # video_overlay.release()
        #             cv2.destroyAllWindows()
        #             break
        #     except Exception as e:
        #             print('Exception:', e)
        #             print('fail')
        #             break
        ################
        frame = cv2.imread(file)
        combo_image = processor.process_objects_on_road(frame)
        cv2.imshow('Detected Objects', combo_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
