resource "oci_streaming_stream" "test_stream" {
    name = var.stream_name
    partitions = var.stream_partitions
    # compartment_id = var.compartment_id
    stream_pool_id = var.stream_pool_id
}