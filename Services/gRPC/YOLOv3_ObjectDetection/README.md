[issue-template]: ../../../../../issues/new?template=BUG_REPORT.md
[feature-template]: ../../../../../issues/new?template=FEATURE_REQUEST.md

![singnetlogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Object Detection

This service uses [YOLOv3](https://pjreddie.com/darknet/yolo/) to perform object detection on images.

It is part of our third party [DNN Model Services](../../..).

## Getting Started

### Requirements

- [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
- [Node 8+ w/npm](https://nodejs.org/en/download/)
- YOLOv3 files: `yolov3.weights` and `yolov3.cfg`

### Development

Clone this repository and download the necessary files using the `get_yolov3.sh` script:
```
$ git clone https://github.com/singnet/dnn-model-services.git
$ cd dnn-model-services/utils
$ ./get_yolov3.sh
$ ls -la Resources/Models
total 242420
drwxrwxr-x 2 user user      4096 Nov  8 08:51 .
drwxrwxr-x 3 user user      4096 Nov  8 08:51 ..
-rw-rw-r-- 1 user user    213558 Nov  8 08:47 yolov3.cfg
-rw-rw-r-- 1 user user 248007048 Mar 25  2018 yolov3.weights
$ cd ../Services/gRPC/YOLOv3_ObjectDetection
```

### Running the service:

To get the `YOUR_AGENT_ADDRESS` you must have already published a service (check this [link](https://github.com/singnet/wiki/tree/master/tutorials/howToPublishService)).

Create the SNET Daemon's config JSON file. It must looks like this:
```
# cat snetd_object_detection_service_config.json
{
    "DAEMON_TYPE": "grpc",
    "DAEMON_LISTENING_PORT": "7007",
    "BLOCKCHAIN_ENABLED": true,
    "ETHEREUM_JSON_RPC_ENDPOINT": "https://kovan.infura.io",
    "AGENT_CONTRACT_ADDRESS": "YOUR_AGENT_ADDRESS",
    "SERVICE_TYPE": "grpc",
    "PASSTHROUGH_ENABLED": true,
    "PASSTHROUGH_ENDPOINT": "http://localhost:7003",
    "LOG_LEVEL": 10,
    "PRIVATE_KEY": "YOUR_PRIVATE_KEY"
}
```
Install all dependencies:
```
$ pip3 install -r requirements.txt
```
Generate the gRPC codes:
```
$ sh buildproto.sh
```
Start the service and SNET Daemon:
```
$ python3 run_object_detection_service.py --daemon-conf .
```

### Calling the service:

Inputs:
  - `model`: DNN Model ("yolov3").
  - `img_path`: An image URL.
  - `confidence`: Confidence of object detection (between 0 and 1).

Local (testing purpose):

```
$ python3 test_object_detection_service.py 
Endpoint (localhost:7003): 
Confidence (0.7): 
Image (Link): http://www.reidsitaly.com/images/planning/sightseeing/calcio.jpg
delta_time: "2.4893"
boxes: "[[150.5, 7.0, 31, 30], [219.5, 65.0, 73, 182], [275.0, 60.0, 212, 198]]"
class_ids: "[32, 0, 0]"
confidences: "[0.9988894462585449, 0.9795901775360107, 0.9754813313484192]"
... (BASE64_BBOX_IMAGE)
```

Through SingularityNET:

```
$ snet set current_agent_at YOUR_AGENT_ADDRESS
set current_agent_at YOUR_AGENT_ADDRESS

$ snet client call detect '{"model": "yolov3", "img_path": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/media/51/2017-10best-lead-photo-672628-s-original.jpg", "confidence": "0.5"}'
...
Read call params from cmdline...

Calling service...

    response:
        boxes: '[[8.5, 151.0, 223, 118], [294.0, 138.0, 78, 48], [127.0, 185.5, 250, 209],
            [605.0, 152.5, 224, 115], [432.0, 129.5, 86, 55], [205.5, 129.0, 81, 38],
            [18.5, 127.0, 127, 40], [439.5, 187.5, 299, 225], [525.0, 132.0, 88, 34],
            [694.5, 126.0, 115, 40]]'
        class_ids: '[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]'
        confidences: '[0.998349130153656, 0.9982008337974548, 0.9977825284004211, 0.995550811290741,
            0.9875208735466003, 0.980316698551178, 0.9753901362419128, 0.969804048538208,
            0.9632347226142883, 0.9579626321792603]'
        delta_time: '2.0124'
        img_base64: ... (BASE64_BBOX_IMAGE)
```

## Contributing and Reporting Issues

Please read our [guidelines](https://github.com/singnet/wiki/blob/master/guidelines/CONTRIBUTING.md#submitting-an-issue) before submitting an issue. If your issue is a bug, please use the bug template pre-populated [here][issue-template]. For feature requests and queries you can use [this template][feature-template].

## Authors

* **Artur Gontijo** - *Maintainer* - [SingularityNET](https://www.singularitynet.io)
