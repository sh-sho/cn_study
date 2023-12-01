import oci

from base64 import b64decode

ociMessageEndpoint = "https://cell-1.queue.messaging.us-phoenix-1.oci.oraclecloud.com"
ociQueueOcid = "ocid1.queue.oc1.phx.amaaaaaassl65iqau6t4rpjks5fjqudjy3v5r33fd4rp2wlptjr7qimp5dca"
ociConfigFilePath = "/home/opc/.oci/config"  
ociProfileName = "DEFAULT"  


def get_message_loop(client, queue_id):
    while True:
        get_response = client.get_messages(queue_id, limit=10, timeout_in_seconds=30)
        if not get_response.data:
            return
        
        print(" Read {} messages".format(get_response.data))
        
        if get_response.data is None:
            content = "Null"
        else:
            content = get_response.data
        print("{}".format(content))
        
        ## delete
        # del_message = oci.queue.models.DeleteMessagesDetailsEntry(receipt = )
        # delete_response = client.delete_messages(queue_id, oci.queue.models.DeleteMessagesDetails)
        # print(" Delete {} messages".format(delete_response.data))
        
            
        


config = oci.config.from_file(ociConfigFilePath, ociProfileName)
queue_client = oci.queue.QueueClient(config, service_endpoint=ociMessageEndpoint)

get_message_loop(queue_client, ociQueueOcid)



