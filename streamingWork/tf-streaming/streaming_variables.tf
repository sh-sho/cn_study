variable "stream_name" {
  type = string
}

variable "stream_partitions" {
  type = number
  default = 1
}

variable "compartment_id" {
    type = string
    default = "ocid1.compartment.oc1..aaaaaaaavu633dop4qlvss3ebdvrzo6hwnr4g5e7s42frmlfvlsjpnyss7xa"
  
}

variable "stream_pool_id" {
  type = string
  default = "ocid1.streampool.oc1.phx.amaaaaaassl65iqawfnqo2qxfifnzuzcvtbe2utg3miyrbdckdvtvtpxja6q"
}

