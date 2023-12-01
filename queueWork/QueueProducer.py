import oci

from base64 import b64encode

ociMessageEndpoint = "https://cell-1.queue.messaging.us-phoenix-1.oci.oraclecloud.com"
ociQueueOcid = "ocid1.queue.oc1.phx.amaaaaaassl65iqau6t4rpjks5fjqudjy3v5r33fd4rp2wlptjr7qimp5dca"
ociConfigFilePath = "/home/opc/.oci/config"  
ociProfileName = "DEFAULT"  

def produce_messages(client, queue_id):
    message_list = []
    for i in range(10):
        value = "messageValue " + str(i)
        message_list.append(oci.queue.models.PutMessagesDetailsEntry(content=value))
        # encoded_value = b64encode(value.encode()).decode()
        # message_list.append(oci.queue.models.PutMessagesDetailsEntry(content=encoded_value))


    print("Publishing {} messages to the stream {} ".format(len(message_list), queue_id))
    print(message_list)
    messages = oci.queue.models.PutMessagesDetails(messages=message_list)
    put_message_result = client.put_messages(queue_id, messages)
    
    # for entry in put_message_result.data.entries:
    #     if entry.error:
    #         print("Error ({}) : {}".format(entry.error, entry.error_message))
    #     else:
    #         print("Published message to partition {} , offset {}".format(entry.partition, entry.offset))

config = oci.config.from_file(ociConfigFilePath, ociProfileName)
queue_client = oci.queue.QueueClient(config, service_endpoint=ociMessageEndpoint)

produce_messages(queue_client, ociQueueOcid)


