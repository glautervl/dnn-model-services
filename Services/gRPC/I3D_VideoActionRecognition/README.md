[issue-template]: ../../../../../issues/new?template=BUG_REPORT.md
[feature-template]: ../../../../../issues/new?template=FEATURE_REQUEST.md

![singnetlogo](../../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

# I3D Video Action Recognition

This service uses [I3D](https://github.com/deepmind/kinetics-i3d) to perform action recognition on videos.

It is part of our third party [DNN Model Services](../../..).

## Getting Started

### Requirements

- [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
- [Node 8+ w/npm](https://nodejs.org/en/download/)

### Development

Clone this repository:

```
$ git clone https://github.com/singnet/dnn-model-services.git
$ cd dnn-model-services/Services/gRPC/I3D_VideoActionRecognition
```

### Running the service:

To get the `YOUR_AGENT_ADDRESS` you must have already published a service (check this [link](https://github.com/singnet/wiki/tree/master/tutorials/howToPublishService)).

Create the SNET Daemon's config JSON file. It must looks like this:
```
$ cat snetd_video_action_recon_service_config.json
{
    "DAEMON_TYPE": "grpc",
    "DAEMON_LISTENING_PORT": "7008",
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
$ python3 run_video_action_recon_service.py --daemon-conf .
```

### Calling the service:

Inputs:
  - `model`: kinetics-i3d model ("400" or "600").
  - `url`: A video URL.

Local (testing purpose):

```
$ python3 test_call_video_action_recon_service.py
Endpoint (localhost:7003):
Method (video_action_recon): 
Model: 400
Url: http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/v_MoppingFloor_g25_c01.avi
{'Action': 'mopping floor\t56.66%\ncleaning floor\t31.83%\nsweeping floor\t11.39%\nsanding floor\t0.02%\nshoveling snow\t0.01%\n'}

$ python3 test_call_video_action_recon_service.py 
Endpoint (localhost:7003): <ENTER>
Method (video_action_recon): <ENTER>
Model: 600
Url: http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/v_MoppingFloor_g25_c01.avi
{'Action': 'mopping floor\t54.51%\nsweeping floor\t41.16%\ncurling (sport)\t4.13%\ngolf driving\t0.05%\nplaying ice hockey\t0.03%\n'}
```

Through SingularityNET:

```
$ snet set current_agent_at YOUR_AGENT_ADDRESS
set current_agent_at YOUR_AGENT_ADDRESS

$ snet client call video_action_recon '{"model": "400", "url": "http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/v_CricketShot_g04_c02.avi"}'
...
Read call params from cmdline...

Calling service...

    response:
        value: '{'Action': 'playing cricket\t97.77%\nskateboarding\t0.71%\nrobot dancing\t0.56%\nroller skating\t0.56%\ngolf putting\t0.13%\n'}'
```

## Contributing and Reporting Issues

Please read our [guidelines](https://github.com/singnet/wiki/blob/master/guidelines/CONTRIBUTING.md#submitting-an-issue) before submitting an issue. If your issue is a bug, please use the bug template pre-populated [here][issue-template]. For feature requests and queries you can use [this template][feature-template].

## Authors

* **Artur Gontijo** - *Maintainer* - [SingularityNET](https://www.singularitynet.io)
