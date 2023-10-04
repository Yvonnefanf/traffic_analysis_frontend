from glob import escape
from sqlite3 import Timestamp
import os
import re
import pyshark
import csv
import pandas as pd
# from scapy.all import *

import random
import ast
# from database.operations_db import *

from flask import request, Response, Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

# upload the pcap files
@app.route('/api/upload', methods=['POST', 'OPTIONS'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.pcap'):
        path = f'uploads/{file.filename}'
        file.save(f'uploads/{file.filename}')
        packets = pcap_to_list(f'uploads/{file.filename}')
        # check_request_method_and_status_code(f'uploads/{file.filename}', f'uploads/{file.filename}_http1.csv','./uploads/www.ctrip.com.log')
        # extract_http2_info(f'uploads/{file.filename}', f'uploads/{file.filename}_http2.csv','./uploads/www.ctrip.com.log')
        # response = app.make_response('success')
        response = jsonify({"data": packets, "path": path})
        response.status_code = 200  # 
    else:
        response = app.make_response('error', 400)
    
    # 设置 CORS 头部
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    return response

def pcap_to_list(filepath):
    # 使用 FileCapture 对象读取 PCAP 文件
    cap = pyshark.FileCapture(filepath)
    
    # 初始化一个空列表来存储数据包数据
    packets_list = []

    for packet in cap:
        # 为每个包创建一个字典
        packet_dict = {
            'Time': packet.sniff_time,
            'length': packet.length,
            'info': getattr(packet, 'info', None),  # 使用 getattr 提供默认值 None
            'protocol': getattr(packet, 'highest_layer', None)  # 使用 getattr 提供默认值 None
        }
        # If the packet is TCP, format the info
        if 'TCP' in packet:
            tcp_layer = packet['TCP']
            src_port = tcp_layer.srcport
            dst_port = tcp_layer.dstport
            flags = getattr(tcp_layer, 'flags', None)
            seq = getattr(tcp_layer, 'seq', None)
            ack = getattr(tcp_layer, 'ack', None)
            window = getattr(tcp_layer, 'window', None)  # Provide a default value of None
            length = getattr(tcp_layer, 'len', None)
            tsval = getattr(tcp_layer, 'time', '')
            tsecr = getattr(tcp_layer, 'tsecr', '')

            info = f"Src Port: {src_port}, Dst Port: {dst_port}, Seq: {seq}, Ack: {ack}, Flags: {flags}, Window: {window}, Len: {length}"
            if tsval and tsecr:
                info += f", TSval: {tsval}, TSecr: {tsecr}"
            packet_dict['info'] = info

        # 将包的数据添加到列表中
        packets_list.append(packet_dict)

    return packets_list


type_mapping = {
    '0': 'DATA (0)',
    '1': 'HEADERS (1)',
    '2': 'PRIORITY (2)',
    '3': 'RST_STREAM (3)',
    '4': 'SETTINGS (4)',
    '5': 'PUSH_PROMISE (5)',
    '6': 'PING (6)',
    '7': 'GOAWAY (7)',
    '8': 'WINDOW_UPDATE (8)',
    '9': 'CONTINUATION (9)'
}

def extract_http2_info(pcap_file, csv_file, ssl_keylog_file):
    print("ssl_keylog_file", ssl_keylog_file)
    capture = pyshark.FileCapture(
    pcap_file,
    tshark_path='/opt/homebrew/bin/tshark',
    override_prefs={'ssl.keylog_file': ssl_keylog_file},
    display_filter='http2.header')

    with open(csv_file, 'w', newline='') as file:
        fieldnames = [
            'HTTP Protocol',
            'Type',
            'Request Method',
            # 'Request URI',
            'Accept Type',
            'Request Packet Number',
            'Status Code',
            'Reason Phrase',
            'Content Type'
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for packet in capture:
            if hasattr(packet, 'http2'):
                http_layer = packet.http2
                # print(dir(http_layer))
                # sys.quit()
                # headers = http_layer.field_names
                # print(headers)

                layer_type = ''
                layer_type_desc = ''
                request_method = ''
                request_uri = ''
                accept_type = ''
                status_code = ''
                reason_phrase = ''
                content_type = ''

                if hasattr(http_layer, 'type'):
                    layer_type = http_layer.type
                    layer_type_desc = type_mapping.get(layer_type, '')
                
                if hasattr(http_layer, 'headers_accept'):
                    accept_type = http_layer.headers_accept
                   
                if hasattr(http_layer, 'headers_content_type'): 
                    content_type = http_layer.headers_content_type
                    
                if hasattr(http_layer, 'header'):
                    status_parts = http_layer.header.split(' ')
                    status_code = status_parts[2] if len(status_parts) > 2 else ''
                    reason_phrase = ' '.join(status_parts[3:]) if len(status_parts) > 3 else ''

                if reason_phrase == '':
                    request_method = status_code
                    status_code = ''
                row = {
                    'HTTP Protocol': 'HTTP/2',
                    'Type': layer_type_desc,
                    'Request Method': request_method,
                    # 'Request URI': request_uri,
                    'Accept Type': accept_type,
                    'Request Packet Number': packet.number,
                    'Status Code': status_code,
                    'Reason Phrase': reason_phrase,
                    'Content Type': content_type
                }
                writer.writerow(row)
    capture.close()

def check_request_method_and_status_code(pcap_file, output_file, ssl_keylog_file):
    # capture = pyshark.FileCapture(pcap_file, display_filter='http.request')
    capture = pyshark.FileCapture(
        
    pcap_file,
    tshark_path='/opt/homebrew/bin/tshark',
    override_prefs={'ssl.keylog_file': ssl_keylog_file},
    display_filter='http.request')
    
    fieldnames = [
        'HTTP Protocol',
        'Request Method',
        # 'Request URI',
        'Accept Type',
        'Request Packet Number',
        'Status Code',
        'Reason Phrase',
        'Content Type',
        'Response Packet Number',
        # 'Interim Packet Number'
    ]

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for packet in capture:
            if 'http' in packet:
                http = packet.http
                request_packet_number = packet.number
                print(f"Request_packet_number: {request_packet_number}")
                    
                row = {
                    'Request Packet Number': request_packet_number,
                    'HTTP Protocol': getattr(http, 'request_version', ''),
                    'Request Method': getattr(http, 'request_method', ''),
                    'Accept Type': getattr(http, 'http.accept', ''),
                    # 'Request URI': http.request_uri,
                }

                # 打印TCP流中的所有数据包编号
                print_packet_numbers_in_tcp_stream(pcap_file, request_packet_number, writer, row, ssl_keylog_file)

    capture.close()

def print_packet_numbers_in_tcp_stream(pcap_file, request_packet_number, writer, row, ssl_keylog_file):
    # capture = pyshark.FileCapture(pcap_file, display_filter='tcp.stream eq {}'.format(tcp_stream))
    capture = pyshark.FileCapture(
    pcap_file,
    override_prefs={'ssl.keylog_file': ssl_keylog_file},
    tshark_path='/opt/homebrew/bin/tshark',
    display_filter='http.response')
    
    for packet in capture:
        packet_number = packet.number
        if packet_number < request_packet_number:
            continue
        else:
            http = packet.http
            # packet_numbers.append(packet_number)
            if (hasattr(http, 'packet.http.request_in')) and (packet.http.request_in == request_packet_number):
                if hasattr(http, 'response_code'):
                    status_code = http.response_code
                    reason_phrase = getattr(http, 'reason_phrase', '')
                    content_type = getattr(http, 'content_type', '')
                    row['Status Code'] = status_code
                    row['Reason Phrase'] = reason_phrase
                    row['Content Type'] = content_type
                    row['Response Packet Number'] = packet_number
                    # merged_packet_numbers = merge_consecutive_numbers(packet_numbers[1:-1])
                    # row['Interim Packet Number'] = '; '.join(packet_numbers[1:-1])
                    writer.writerow(row)

                    break  # 结束循环，不再继续读取数据包

    capture.close()
    
@app.route('/api/getTraffic', methods=['GET'])
def getTraffic():
    ifFilter = request.args.get('ifFilter')  # 获取查询参数ifFilter
    print("ifFilter",ifFilter)
    df = pd.read_csv(f'analysis/consolidated.csv', parse_dates=['Time'])
    df.fillna("NaN", inplace=True)  # 使用字符串 "NaN" 替换 NaN 值
    # 将数据框转换为字典列表
    
    # 如果 ifFilter 参数存在且为'true'，则过滤数据
    if ifFilter and ifFilter.lower() == 'true':
        print('filter')
        df = df[df['Action'] != 'NaN']  # 过滤掉 Action 列为 "NaN" 的行

    # 添加 actionId 列
    df['actionId'] = (df['Action'] != df['Action'].shift()).cumsum()


    result = df.to_dict(orient='records')

    # 获取 actionId 和 Action，并删除重复的行
    actions = df[['actionId', 'Action']].drop_duplicates().sort_values(by='actionId')

    # 转换为所需的数组格式
    actions_array = [{'actionId': row['actionId'], 'label': row['Action']} for index, row in actions.iterrows()]

    response = jsonify({"actions_array": actions_array, "result": result})

    # # 如果你想将数据框转换为 numpy 数组
    # array = df.to_numpy()
    # array_list = array.tolist()
    # response = jsonify({actions_array:actions_array,result:result})

    return response


if __name__ == '__main__':
   app.run(host='localhost', port=5000)