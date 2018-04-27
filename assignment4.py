
import nmap

def port_scanner(ports):
    nm = nmap.PortScanner()
    print(nm.scan(ports, '21-1000'))
    nm.scan(ports, '21-1000')
    print(ports)
    print(nm.all_hosts())
    print(ports)
    for host_names in nm.all_hosts():
        print(ports)
        ports = nm[host_names].get('tcp')
        print(ports)
        write_to_file(ports)

    return ports

    """
    write a port scanner using nmap library
    for scanning 10 arbitrary hosts and and ports between
    21-1000 then write the result to a file using
    write_to_file function
    """

def write_to_file(contents):
    f = open('result_of_nmap', 'w')

    f.write(contents)
    """
    first remove the pass from function body
    then write your code
    :param contents: the result that should be written to file
    :return: true if the writing successfull and false if can't
    """

    pass

def get_host_names():
    f = open('host_names', 'r')
    hosts = f.read()
    hosts = hosts.rsplit('\n')
    return hosts




def main():
    hosts = get_host_names()
    for host_name in hosts:
        port_scanner(host_name)

main()
