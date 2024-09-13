import argparse
from scapy.all import *
from datetime import timedelta

def find_matching_intervals(pcap1, pcap2, min_packet_count=3, show_first_only=True):
    sniff(offline=pcap1, prn=lambda x: packet_data[x.number].append(x.time()))
    packet_data = {}
    for pkt in PcapReader(pcap2):
        if not pkt.haslayer('IP'):
            continue
        num = int(pkt['IP'].src) % 1000000
        if num not in packet_data:
            packet_data[num] = []
        packet_data[num].append(pkt.time())
    
    intervals = []
    interval_start = None
    current_packet_count = 0
    
    for idx, ts in enumerate(packet_data[0], start=1):
        if len(packet_data[idx]) == 0 or abs((ts - packet_data[idx][0]).total_seconds() >= 60*10):
            if interval_start is not None and current_packet_count >= min_packet_count:
                intervals.append([interval_start, max(packet_data[0]), interval_start, max(packet_data[idx])])
            interval_start = None
            current_packet_count = 0
            
        elif packet_data[idx][0] <= ts + timedelta(minutes=10):
            current_packet_count += 1
            if interval_start is None:
                interval_start = packet_data[idx][0]
    
    return intervals

def main():
    parser = argparse.ArgumentParser(description='Search matching intervals between two pcap files')
    parser.add_argument('file1', type=str, help='Path to the first pcap file')
    parser.add_argument('file2', type=str, help='Path to the second pcap file')
    parser.add_argument('-m', '--min-packet-count', default=3, type=int, help='Minimum number of consecutive packets that must match in an interval')
    parser.add_argument('-f', '--first-only', action='store_true', help='Show information only about the first matching interval')
    args = parser.parse_args()
    
    intervals = find_matching_intervals(args.file1, args.file2, args.min_packet_count, args.first_only)
    
    if not intervals:
        print("No matching intervals found.")
        return
    
    if args.first_only:
        matched_interval = intervals[0]
        print(f"Number of matching intervals: {len(intervals)}")
        print(f"Matching interval: {matched_interval}")
        print(f"Number of packets within the matching interval: {len(packet_data[matched_interval[0]])} + {len(packet_data[matched_interval[3]])}")
        print(f"First packet time from file1: {matched_interval[0]}")
        print(f"Last packet time from file1: {matched_interval[1]}")
        print(f"First packet time from file2: {matched_interval[2]}")
        print(f"Last packet time from file2: {matched_interval[3]}")
    else:
        for i in range(len(intervals)):
            matched_interval = intervals[i]
            print(f"Interval #{i+1}:")
            print(f"Number of packets within the matching interval: {len(packet_data[matched_interval[0]])} + {len(packet_data[matched_interval[3]])}")
            print(f"First packet time from file1: {matched_interval[0]}")
            print(f"Last packet time from file1: {matched_interval[1]}")
            print(f"First packet time from file2: {matched_interval[2]}")
            print(f"Last packet time from file2: {matched_interval[3]}")

if __name__ == '__main__':
    main()
