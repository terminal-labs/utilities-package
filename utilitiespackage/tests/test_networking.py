from utilitiespackage.networking import get_primary_address


def test_get_primary_address():
    mockdata_0 = b"""
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
        inet 172.28.128.1/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0
           valid_lft 60000sec preferred_lft 60000sec
        inet6 2605:2605:2605:2605::1024/128 scope global dynamic noprefixroute
           valid_lft 60000sec preferred_lft 60000sec
    """
    mockdata_1 = b"""
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
        inet 172.28.128.128/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0
           valid_lft 60000sec preferred_lft 60000sec
        inet6 2605:2605:2605:2605::1024/128 scope global dynamic noprefixroute
           valid_lft 60000sec preferred_lft 60000sec
    """
    mockdata_2 = b"""
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
        inet 172.28.128.112/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0
           valid_lft 60000sec preferred_lft 60000sec
        inet6 2605:2605:2605:2605::1024/128 scope global dynamic noprefixroute
           valid_lft 60000sec preferred_lft 60000sec
    """
    assert get_primary_address(mockdata=mockdata_0) == "172.28.128.1"
    assert get_primary_address(mockdata=mockdata_1) == "172.28.128.128"
    assert get_primary_address(mockdata=mockdata_2) == "172.28.128.112"
