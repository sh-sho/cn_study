import oci
from base64 import b64encode 
import time
import json

ociMessageEndpoint = "https://cell-1.streaming.us-phoenix-1.oci.oraclecloud.com"  
ociStreamOcid = "ocid1.stream.oc1.phx.amaaaaaassl65iqap5ath7yuo7q6foymcme6omvrhprcgdwmk7zldsxsp5ea"  
ociConfigFilePath = "/home/opc/.oci/config"  
ociProfileName = "DEFAULT"

data = {
        "timestamp": "2019-01-07T21:00:08Z",
        "values": [
            0.4738691915899007,
            -0.2103424394727376,
            0.024398945908493404,
            1.178795358083708,
            -0.0027861332237756747,
            -0.3361819458453297,
            0.46908916038037074,
            -0.8186905010094537,
            -0.4766573216296686,
            0.21636488871770235
        ]
}

error_data = {
        "timestamp": "2019-01-07T21:00:08Z",
        "values": [
            -0.00000000000000001,
            -1.5588250424377889,
            -2.3941492028804823,
            2.593357112443483,
            -1.6094973523998164,
            -1.8641932916192756,
            -1.4677973361129089,
            -2.7708583572138727,
            -2.9587694388165655,
            1000000000000000
        ]
}

def produce_messages(client, stream_id, i):
    # Build up a PutMessagesDetails and publish some messages to the stream
    message_list = []#      
    time.sleep(5)
    key = "messageKey" + str(i)
    #   data_bytes = bytes(data, 'utf-8')
    value = json.dumps(error_data)
    print(type(value))
    encoded_key = b64encode(key.encode()).decode()
    encoded_value = b64encode(value.encode()).decode()
    message_list.append(oci.streaming.models.PutMessagesDetailsEntry(key=encoded_key, value=encoded_value))  

    print("Publishing {} messages to the stream {} ".format(len(message_list), stream_id))
    messages = oci.streaming.models.PutMessagesDetails(messages=message_list)
    put_message_result = client.put_messages(stream_id, messages)
    
    # The put_message_result can contain some useful metadata for handling failures
    for entry in put_message_result.data.entries:
        if entry.error:
            print("Error ({}) : {}".format(entry.error, entry.error_message))
        else:
            print("Published message to partition {} , offset {}".format(entry.partition, entry.offset))

config = oci.config.from_file(ociConfigFilePath, ociProfileName)
stream_client = oci.streaming.StreamClient(config, service_endpoint=ociMessageEndpoint)

# Publish some messages to the stream
for i in range(5):
    produce_messages(stream_client, ociStreamOcid, i)

# data = {
#         "requestType": "INLINE",
#         "signalNames": [
#             "temperature_1",
#             "temperature_2",
#             "temperature_3",
#             "temperature_4",
#             "temperature_5",
#             "pressure_1",
#             "pressure_2",
#             "pressure_3",
#             "pressure_4",
#             "pressure_5"
#         ],
#         "data": [
#             {
#             "timestamp": "2019-01-07T21:00:08Z",
#             "values": [
#                 0.4738691915899007,
#                 -0.2103424394727376,
#                 0.024398945908493404,
#                 1.178795358083708,
#                 -0.0027861332237756747,
#                 -0.3361819458453297,
#                 0.46908916038037074,
#                 -0.8186905010094537,
#                 -0.4766573216296686,
#                 0.21636488871770235
#             ]
#             }
#         ]
#     }