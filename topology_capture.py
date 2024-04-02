import os
import json
import subprocess
from time import sleep
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
import urllib2

# Define custom topology
class CustomTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)

# Function to capture network topology from Ryu controller
def capture_topology():
    topology_url = 'http://localhost:8080/v1.0/topology/switches'
    response = urllib2.urlopen(topology_url)
    topology_data = json.load(response)
    return topology_data

# Function to push data to Git repository
def push_to_git(data):
    # Change directory to the repository
    os.chdir('/home/b-abdul9071/Desktop/SDN')

    # Add new topology file
    with open('topology.json', 'w') as f:
        f.write(json.dumps(data))

    # Add, commit, and push changes
    subprocess.call(['git', 'add', 'topology.json'])
    subprocess.call(['git', 'commit', '-m', 'Added new network topology'])
    subprocess.call(['git', 'push'])

if __name__ == '__main__':
    setLogLevel('info')

    # Start Mininet with Ryu controller
    topo = CustomTopology()
    controller_ip = '127.0.0.1'
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip=controller_ip))
    net.start()

    # Sleep to allow time for switches to connect to the controller
    sleep(5)

    # Capture network topology
    topology_data = capture_topology()

    # Push topology data to Git repository
    push_to_git(topology_data)
    
    # Success msg
    print("Uploaded to git succesfully!")
    
    # Stop Mininet
    net.stop()
