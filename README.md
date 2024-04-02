# SDN Topology Capture and Git Integration
Capture SDN info (from mininet)and push it to Git.

This project aims to capture the network topology from SDN environment created using Mininet and Ryu Controller and we are pushing the data to a git repository.

# Requirements
- Mininet
- Ryu Controller
- Python 2.7 or later
- Git

# Ryu
ryu-manager ryu.app.rest_topology

# sudo -E
use 'sudo -E python script_name.py' to run the script, sudo for mininet and -E option to retain the user's environment so that the git config works and to stop the mininet use 'sudo mn -c'

#NOTE
# Set up your connection to git using ssh, clone repo: "git@github.com:lightz51/SDN.git" using ssh
# Change changedir path according to location of your cloned directory
