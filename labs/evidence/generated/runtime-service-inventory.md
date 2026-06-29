# Runtime Service Inventory

Generated At: 2026-06-29 10:39:22 KST +0900

Source: ansible ubuntu_nodes service and port collection

----- BEGIN RUNTIME INVENTORY -----
data-ops-node | CHANGED | rc=0 >>
## Host
data-ops-node

## Time
2026-06-29 10:39:25 KST +0900

## IP Address
192.168.8.135 192.168.1.40 172.17.0.1 

## Active Services
docker: active
node_exporter: active
promtail: active
prometheus: active
grafana-server: active
loki: active
blackbox_exporter: active
mariadb: active
mysqld_exporter: active
alertmanager: active
chrony: active

## Listening Ports
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                                        
LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=6387,fd=3),("sshd",pid=1561,fd=3),("systemd",pid=1,fd=226))
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=692,fd=15))                                     
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=692,fd=17))                                     
LISTEN 0      80         127.0.0.1:3306       0.0.0.0:*    users:(("mariadbd",pid=20880,fd=24))                                          
LISTEN 0      4096               *:9080             *:*    users:(("promtail",pid=41650,fd=8))                                           
LISTEN 0      4096               *:9100             *:*    users:(("node_exporter",pid=47970,fd=3))                                      
LISTEN 0      4096               *:9096             *:*    users:(("loki",pid=40696,fd=9))                                               
LISTEN 0      4096               *:9093             *:*    users:(("alertmanager",pid=45291,fd=8))                                       
LISTEN 0      4096               *:9094             *:*    users:(("alertmanager",pid=45291,fd=3))                                       
LISTEN 0      4096               *:9090             *:*    users:(("prometheus",pid=45331,fd=7))                                         
LISTEN 0      4096               *:9115             *:*    users:(("blackbox_export",pid=42215,fd=3))                                    
LISTEN 0      4096               *:9104             *:*    users:(("mysqld_exporter",pid=43357,fd=3))                                    
LISTEN 0      4096            [::]:22            [::]:*    users:(("sshd",pid=6387,fd=4),("sshd",pid=1561,fd=4),("systemd",pid=1,fd=227))
LISTEN 0      4096               *:3100             *:*    users:(("loki",pid=40696,fd=8))                                               
LISTEN 0      4096               *:3000             *:*    users:(("grafana",pid=41773,fd=27))                                           
LISTEN 0      4096               *:43501            *:*    users:(("promtail",pid=41650,fd=9))                                           
app-node-02 | CHANGED | rc=0 >>
## Host
app-node-02

## Time
2026-06-29 10:39:25 KST +0900

## IP Address
192.168.8.134 192.168.1.32 172.17.0.1 

## Active Services
docker: active
node_exporter: active
promtail: active
chrony: active

## Listening Ports
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                 
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=671,fd=17))              
LISTEN 0      4096         0.0.0.0:80         0.0.0.0:*    users:(("docker-proxy",pid=38976,fd=8))                
LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=2200,fd=3),("systemd",pid=1,fd=135))
LISTEN 0      128        127.0.0.1:35221      0.0.0.0:*    users:(("code-7e7950df89",pid=1580,fd=10))             
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=671,fd=15))              
LISTEN 0      4096         0.0.0.0:8080       0.0.0.0:*    users:(("docker-proxy",pid=39013,fd=8))                
LISTEN 0      4096               *:43009            *:*    users:(("promtail",pid=41833,fd=9))                    
LISTEN 0      4096            [::]:22            [::]:*    users:(("sshd",pid=2200,fd=4),("systemd",pid=1,fd=136))
LISTEN 0      4096               *:9080             *:*    users:(("promtail",pid=41833,fd=8))                    
LISTEN 0      4096               *:9100             *:*    users:(("node_exporter",pid=12672,fd=3))               
app-node-01 | CHANGED | rc=0 >>
## Host
app-node-01

## Time
2026-06-29 10:39:25 KST +0900

## IP Address
192.168.8.133 192.168.1.31 172.17.0.1 

## Active Services
docker: active
node_exporter: active
promtail: active
chrony: active

## Listening Ports
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                 
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=662,fd=17))              
LISTEN 0      128        127.0.0.1:42261      0.0.0.0:*    users:(("code-7e7950df89",pid=1591,fd=10))             
LISTEN 0      4096         0.0.0.0:8080       0.0.0.0:*    users:(("docker-proxy",pid=37195,fd=8))                
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=662,fd=15))              
LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=2401,fd=3),("systemd",pid=1,fd=160))
LISTEN 0      4096         0.0.0.0:80         0.0.0.0:*    users:(("docker-proxy",pid=37241,fd=8))                
LISTEN 0      4096               *:37361            *:*    users:(("promtail",pid=40072,fd=9))                    
LISTEN 0      4096            [::]:22            [::]:*    users:(("sshd",pid=2401,fd=4),("systemd",pid=1,fd=162))
LISTEN 0      4096               *:9080             *:*    users:(("promtail",pid=40072,fd=8))                    
LISTEN 0      4096               *:9100             *:*    users:(("node_exporter",pid=12459,fd=3))               
openstack-node | CHANGED | rc=0 >>
## Host
openstack-node

## Time
2026-06-29 10:39:25 KST +0900

## IP Address
192.168.8.131 192.168.1.10 172.17.0.1 

## Active Services
docker: active
node_exporter: active
promtail: active
chrony: active

## Listening Ports
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                 
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=712,fd=15))              
LISTEN 0      128        127.0.0.1:43851      0.0.0.0:*    users:(("code-7e7950df89",pid=1418,fd=10))             
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=712,fd=17))              
LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=9697,fd=3),("systemd",pid=1,fd=234))
LISTEN 0      4096               *:40461            *:*    users:(("promtail",pid=25977,fd=9))                    
LISTEN 0      4096            [::]:22            [::]:*    users:(("sshd",pid=9697,fd=4),("systemd",pid=1,fd=235))
LISTEN 0      4096               *:9080             *:*    users:(("promtail",pid=25977,fd=8))                    
LISTEN 0      4096               *:9100             *:*    users:(("node_exporter",pid=14721,fd=3))               
proxy-network-node | CHANGED | rc=0 >>
## Host
proxy-network-node

## Time
2026-06-29 10:39:25 KST +0900

## IP Address
192.168.8.132 192.168.1.20 172.17.0.1 

## Active Services
docker: active
node_exporter: active
promtail: active
haproxy: active
chrony: active

## Listening Ports
State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                                 
LISTEN 0      128        127.0.0.1:42497      0.0.0.0:*    users:(("code-7e7950df89",pid=1564,fd=10))             
LISTEN 0      2048         0.0.0.0:8404       0.0.0.0:*    users:(("haproxy",pid=26120,fd=10))                    
LISTEN 0      4096         0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=7908,fd=3),("systemd",pid=1,fd=208))
LISTEN 0      4096      127.0.0.54:53         0.0.0.0:*    users:(("systemd-resolve",pid=657,fd=17))              
LISTEN 0      2048         0.0.0.0:80         0.0.0.0:*    users:(("haproxy",pid=26120,fd=9))                     
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*    users:(("systemd-resolve",pid=657,fd=15))              
LISTEN 0      4096            [::]:22            [::]:*    users:(("sshd",pid=7908,fd=4),("systemd",pid=1,fd=209))
LISTEN 0      4096               *:9100             *:*    users:(("node_exporter",pid=12934,fd=3))               
LISTEN 0      4096               *:39883            *:*    users:(("promtail",pid=25594,fd=9))                    
LISTEN 0      4096               *:9080             *:*    users:(("promtail",pid=25594,fd=8))                    
----- END RUNTIME INVENTORY -----
