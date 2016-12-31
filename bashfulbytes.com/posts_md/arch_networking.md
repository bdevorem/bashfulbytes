---
title: Simple Networking in Arch Linux 
date: 2016 12 30
tag: linux
summary: i really suck at networking, and ive finally found a simple recipe for networking in arch
---

# Simple Networking in Arch Linux

Arch Linux is my favorite. I've been running Arch for a year now and though I've 
had many ups and downs, the ups always outweigh the downs. Nowadays, I can 
only imagine running Arch or an operating system with extremely similar design
philosophies. However, I've always had one major problem with Arch Linux: networking.  
  
I am not a networking guru. I enjoyed my Computer Networks course and I am slightly
fond of web development, but when it comes to connecting to the Internet in Arch 
Linux, it's always a struggle. A big struggle. But after a year of tinkering around,
I finally no longer boot into my dual partition of Ubuntu when networking gets hard.  
  
So, you go to an airport, or a Starbucks, or a friend's house and you need to connect
to a new network? Well, below is the recipe for simple networking in Arch Linux:  

## Before You Leave Home

1. Switch to [systemd-networkd](https://wiki.archlinux.org/index.php/systemd-networkd)  
	This is the major step, especially if you are using NetworkManager, and you 
	should do this when you set up your fresh install of Arch Linux, preferably. If
	you didn't, then stay home and make the switch before you brave the world of
	new networks. [Here is a simple guide.](http://xmodulo.com/switch-from-networkmanager-to-systemd-networkd.html)  

2. Set up [WPA Supplicant](https://wiki.archlinux.org/index.php/WPA_supplicant)  
	Install the `wpa_supplicant` package from the official Arch repositories. Then,
	you will need to set up the configuration files. The minimal config file
	should set your control interface. The advanced config file can set your
	networks and passwords. You should first find your wireless interface name with 
	`ip link`, and name your file `wpa_supplicant-interface.conf` in `etc/wpa_supplicant/`.
	A basic version of my config file is shown below.  

		# /etc/wpa_supplicant/wpa_supplicant-wlp3s0.conf  
		ctrl_interface=/var/run/wpa_supplicant  
		eapol_version=1		# this is the default  
		ap_scan=1			# also the default  
		fast_reauth=1		# also the default  
		p2p_disabled=1		# through many trials & errors, this has served me well  

		# an example network configuration, but not what this post is about  
		network={   
			ssid="Google Starbucks"  
			key_mgmt=NONE  
		}  

## When You're Ready to Network

1. Start the WPA commandline client  
	Type `sudo wpa_cli` from your terminal. Root privileges required. You should get
	a nice description of the version of `wpa_cli` you are using, as well as the
	selected interface, which should be the same interface as the one you created
	a configuration file for. 

2. Scan for available networks  
	Type `scan`, and wait until the client says something along the lines of
	`CTRL-EVENT-SCAN-RESULTS`. This means the scan has finished and you can 
	now see the available networks in your range.

3. List available networks  
	Type `scan_results`. You should get a list of the found networks in return. Take
	note of the SSID of the network you want to connect to (the last column's value).
	Let's assume your chosen network's SSID is `example network`.

4. Add a network  
	Type `add_network` from the commandline. You should recieve a number in response.
	Let's assume for the sake of this post that the number is `2`. Now you're ready
	to connect.

5. Set the network identification and passphrase  
	Assuming network `2` and SSID `example_network`, 
	type `set_network 2 ssid "example network"`. You should get an `OK` in return. Else,
	you can't connect to this network or you misspelled the name. Then, set the 
	passphrase in a similar manner: `set_network 2 psk "sup3r_s3cr3t_p4ssphr4s3"`.
	Once again, you should get an `OK` in return.

6. Enable the network!  
	The tricky step for me. I was unaware I had to select and enable the network I
	wanted. Well, it's easy. To be safe, first enable your network: `enable_network 2`.
	Then, select it: `select_network 2`. This last command should disable all other 
	networks, but I like to play it safe by enabling the new network first.

That's it. You should get `authenticating` and `key negotiation` messages, and then
you're set. Super simple, right? Why did it take me so long to figure this out?
Great question.  
