function host(){
    host=$(hostname -I)
    echo $host
}
function config(){
    confi=$(curl ifconfig.me)
    echo $confi
}
function nmap(){
    nmap=$(nmap 192.168.100.1)
    echo $nmap
}
function pag(){
    pag=$(nmap scanme.nmap.org)
    echo $pag
}
host
config
nmap
pag