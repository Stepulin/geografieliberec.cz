#!/bin/bash
# Created on 12. 5. 2018; version 1.0
# Created by Jan Stepanek, contributor Martin Hunek
#####################################
# Added on 20190928 | with Debian 10 (Buster)
PATH='/sbin'
#####################
# Delete all settings
#####################
echo "Deleting all settings"
iptables -F
iptables -X
iptables -Z

#############################################
# Starting firewall & settings default policy
#############################################
echo "..."
echo "Starting firewall"
echo "..."
echo "Setting default policy"

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

##########
# Chain(s)
##########
iptables -N ICMP_CHK

#############
# INPUT chain
#############

#######
# Local
#######
iptables -A INPUT -s 10.1.0.0/16 -j ACCEPT
iptables -A INPUT -s 192.168.1.1/24 -j ACCEPT

#######
iptables -A INPUT -p icmp -j ICMP_CHK
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -m state --state INVALID -j DROP
# Most common port, allow them later if necessary
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --dport 5000 -j ACCEPT #generator pyramid
iptables -A INPUT -p tcp --dport 5001 -j ACCEPT #bokeh ukazka
iptables -A INPUT -p tcp --dport 5002 -j ACCEPT #bokeh pocet ob muzi
iptables -A INPUT -p tcp --dport 5003 -j ACCEPT #bokeh pocet ob zeny
iptables -A INPUT -p tcp --dport 5010 -j ACCEPT #bokeh porodnost
iptables -A INPUT -p tcp --dport 5011 -j ACCEPT #bokeh umrtnost
iptables -A INPUT -p tcp --dport 5012 -j ACCEPT #bokeh prirozeny prirustek na 1000
iptables -A INPUT -p tcp --dport 5013 -j ACCEPT #bokeh procentualni narust
iptables -A INPUT -p tcp --dport 5014 -j ACCEPT #bokeh migracni saldo
iptables -A INPUT -p tcp --dport 5015 -j ACCEPT #bokeh migracni saldo na 1000
iptables -A INPUT -p tcp --dport 5016 -j ACCEPT #bokeh stredni delka zivota CLKM
iptables -A INPUT -p tcp --dport 5017 -j ACCEPT #bokeh stredni delka zivota M
iptables -A INPUT -p tcp --dport 5018 -j ACCEPT #bokeh stredni delka zivota Z




###############
# FORWARD chain
###############

##############
# OUTPUT chain
##############
iptables -A OUTPUT -o lo -j ACCEPT
# Added on 20200202 | with Ubuntu 18 (Bionic Beaver)
iptables -A INPUT -i lo -j ACCEPT


##################
# ICMP CHECK chain
##################
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 8 -m limit --limit 30/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 0 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 3/0 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 3/1 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 3/3 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 3/4 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -p icmp -m icmp --icmp-type 11 -m limit --limit 10/sec -j ACCEPT
iptables -A ICMP_CHK -j DROP

############
# Finalizing
############
echo "..."
echo "Done"
