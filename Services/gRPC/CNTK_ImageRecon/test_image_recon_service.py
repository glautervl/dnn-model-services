import sys
import grpc

# import the generated classes
import service.service_spec.image_recon_pb2_grpc as grpc_bt_grpc
import service.service_spec.image_recon_pb2 as grpc_bt_pb2

from service import registry

TEST_URL = "https://raw.githubusercontent.com/singnet/dnn-model-services/master/docs/assets/users_guide/rose.jpg"

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "test":
                test_flag = True

        endpoint = input("Endpoint (localhost:{}): ".format(registry["image_recon_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["image_recon_service"]["grpc"])

        # open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        grpc_method = input("Method (flowers|dogs): ") if not test_flag else "flowers"

        model = input("Model (ResNet152): ") if not test_flag else ""
        if model == "":
            model = "ResNet152"

        img_path = input("Image (Link): ") if not test_flag else TEST_URL

        if grpc_method == "flowers":
            # create a stub (client)
            stub = grpc_bt_grpc.FlowersStub(channel)
            # create a valid request message
            number = grpc_bt_pb2.ImageReconRequest(model=model, img_path=img_path)
            # make the call
            response = stub.flowers(number)
            # et voilà
            print(response.delta_time)
            print(response.top_5)

        elif grpc_method == "dogs":
            # create a stub (client)
            stub = grpc_bt_grpc.DogsStub(channel)
            # create a valid request message
            number = grpc_bt_pb2.ImageReconRequest(model=model, img_path=img_path)
            # make the call
            response = stub.dogs(number)
            # et voilà
            print(response.delta_time)
            print(response.top_5)

        elif grpc_method == "cars":
            # create a stub (client)
            stub = grpc_bt_grpc.CarsStub(channel)
            # create a valid request message
            number = grpc_bt_pb2.ImageReconRequest(model=model, img_path=img_path)
            # make the call
            response = stub.cars(number)
            # et voilà
            print(response.delta_time)
            print(response.top_5)

            if response.top_5 == "Fail":
                exit(1)

        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
