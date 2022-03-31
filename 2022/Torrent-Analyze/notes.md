# For

# Flag: picoCTF{ubuntu-19.10-desktop-amd64.iso}

1) Open pcap
2) Enable protocol BT-DHT
3) Google each info_hash as they contain the name of the file
4) Packet 51080
  Frame 51080: 139 bytes on wire (1112 bits), 139 bytes captured (1112 bits) on interface eth0, id 0
  Ethernet II, Src: VMware_2d:4b:5e (00:0c:29:2d:4b:5e), Dst: VMware_f5:e4:05 (00:50:56:f5:e4:05)
  Internet Protocol Version 4, Src: 192.168.73.132, Dst: 107.181.231.146
  User Datagram Protocol, Src Port: 51413, Dst Port: 2169
  BitTorrent DHT Protocol
      Request arguments: Dictionary...
          Key: a
          Value: Dictionary...
              id: 17c1ec414b95fc775d7dddcb686693b7863ac1aa
                  Key: id
                  Value: 17c1ec414b95fc775d7dddcb686693b7863ac1aa
              info_hash: e2467cbf021192c241367b892230dc1e05c0580e
                  Key: info_hash
                  Value: e2467cbf021192c241367b892230dc1e05c0580e
              Terminator: e
      Request type: get_peers
          Key: q
          Value: get_peers
      Transaction ID: 6770c723
          Key: t
          Value: 6770c723
      Message type: Request
          Key: y
          Value: q
      Terminator: e

5) Google: torrent e2467cbf021192c241367b892230dc1e05c0580e
  ubuntu-19.10-desktop-amd64.iso at Linuxtracker
  https://linuxtracker.org › id=e2467cbf021192c241367b...
  17 Oct 2019 — If you need a Bittorrent client, try TransmissionBT on MacOS or Linux ... Info Hash, e2467cbf021192c241367b892230dc1e05c0580e. Who thanks.