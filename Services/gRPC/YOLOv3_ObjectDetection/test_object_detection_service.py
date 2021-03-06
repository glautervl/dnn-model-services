import sys
import grpc

# import the generated classes
import service.service_spec.object_detection_pb2_grpc as grpc_bt_grpc
import service.service_spec.object_detection_pb2 as grpc_bt_pb2

from service import registry

TEST_URL = "https://raw.githubusercontent.com/singnet/dnn-model-services/master/docs/assets/users_guide/backpack_man_dog.jpg"

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "test":
                test_flag = True

        endpoint = input("Endpoint (localhost:{}): ".format(registry["object_detection_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["object_detection_service"]["grpc"])

        # open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        grpc_method = "detect"
        model = "yolov3"
        confidence = input("Confidence (0.7): ") if not test_flag else ""
        if confidence == "":
            confidence = "0.7"

        img_path = input("Image (Link): ") if not test_flag else TEST_URL

        # create a stub (client)
        stub = grpc_bt_grpc.DetectStub(channel)
        # create a valid request message
        request = grpc_bt_pb2.ObjectDetectionRequest(model=model, confidence=confidence, img_path=img_path)
        # make the call
        response = stub.detect(request)
        print(response)

        if response.delta_time == "Fail":
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
