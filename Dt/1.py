


def port_inspect (event):
	tcp_packet = tcp packets
	if not tcp_packet:
		return
	if tcp_packet.port == 445 or 139:
		block the stream
	else:
		return

def launch:
	addListenerByName(port_inspect, high priority)


def smb_handler(event):
	tcp_packet = tcp packets
	if not tcp_packet:
		return
	if tcp_packet.port == 445 or 139:
		if (check the string "1Mz7153HMuxXTur2R1t78mGSdzaAtNbBWX"):
			found Malicous SMB 
			block the flow
		else:
			normal processure
	else:
		return


def launch:
	addListenerByName(smb_handler, high priority)


def http_handler(event):
	tcp_packet = tcp packets
	if not tcp_packet:
		return
	elif http packet:
		if "PROPFIND /admin$" is found:
			block the http flow
		else:
			normal processure
	else:
		return

def launch:
	addListenerByName(http_handler, high priority)


def arp_handler(event):
	 packet = event.parsed
	 if packet == ARP packet:
	 	if source ip address is 0.0.0.0:
	 		return
	 	if packet == ARP request packet:
	 		counter + 1
	 		if counter > 10:
	 			block the infected host
	 		else:
	 			pass
	 	elif packet == ARP reply packet:
	 		counter - 1
	 	else:
	 		return
	 else:
	 	return

def launch:
	addListenerByName(arp_handler, high priority)
