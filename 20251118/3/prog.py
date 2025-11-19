import sys
import struct

data = sys.stdin.buffer.read()
data_len = len(data)

if data_len < 44:
    print('NO', end='')
    exit()

is_riff = data[:4]
is_wave = data[8:12]
is_fmt = data[12:16]
if is_riff != b'RIFF' or is_wave != b'WAVE' or is_fmt != b'fmt ' or struct.unpack('i', data[16:20])[0] != 16:
    print('NO', end='')
    exit()

file_size = struct.unpack('i', data[4:8])[0]
type_of_format = struct.unpack('h', data[20:22])[0]
channels = struct.unpack('h', data[22:24])[0]
sample_rate = struct.unpack('i', data[24:28])[0]
bits_per_sample = struct.unpack('h', data[34:36])[0]
data_size = struct.unpack('i', data[40:44])[0]

if sample_rate != 44100 and sample_rate != 48000 or bits_per_sample != 16:
    print('NO', end='')
    exit()

if struct.unpack('i', data[28:32])[0] != (sample_rate * bits_per_sample * channels) / 8:
    print('NO', end='')
    exit()

if struct.unpack('h', data[32:34])[0] != (bits_per_sample * channels) / 8 and (struct.unpack('h', data[32:34])[0] != 1 or struct.unpack('h', data[32:34])[0] != 2 or struct.unpack('h', data[32:34])[0] != 4):
    print('NO', end='')
    exit()

if data[36:40] != b'data':
    print('NO', end='')
    exit()

print(f'Size={file_size}, Type={type_of_format}, Channels={channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}', end='')