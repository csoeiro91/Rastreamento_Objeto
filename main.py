import cv2


source_video = "futebol.mp4"
cap = cv2.VideoCapture(source_video)

def selectROIfromFrame(frame):
    # box (x, y, lar, alt)
    box = cv2.selectROI("SELECT ROI", frame, fromCenter=False, showCrosshair=False)
    print(box)
    return box


if __name__ == "__main__":

    first_frame = cv2.imread("futebol.png")

    #OPENCV 4.5.3.56
    '''params = cv2.TrackerDaSiamRPN_Params()
    params.model = "model/DaSiamRPN/dasiamrpn_model.onnx"
    params.kernel_r1 = "model/DaSiamRPN/dasiamrpn_kernel_r1.onnx"
    params.kernel_cls1 = "model/DaSiamRPN/dasiamrpn_kernel_cls1.onnx"
    tracker = cv2.TrackerDaSiamRPN_create(params)

    box = selectROIfromFrame(first_frame)
    ok = tracker.init(first_frame, box)'''


    box = selectROIfromFrame(first_frame)
    tracker = cv2.TrackerMIL_create()
    ok = tracker.init(first_frame, box)


    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        ok, box = tracker.update(frame)

        if ok:
            pt1 = (box[0], box[1])
            pt2 = ((box[0] + box[2]), (box[1] + box[3]))
            cv2.rectangle(frame, pt1, pt2, (255, 0, 0), 2, 1)
        else:
            print("FALHOU")

        cv2.imshow("Tracking", frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()