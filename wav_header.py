import sys

sample_id = sys.argv[1]

# Open a .wav file as read binary
with open(sample_id, 'rb') as fp:
    raw_wav = fp.readlines()

print(f'Sample: {sample_id.split("/")[-1]}')


print('WAV RIFF Header Description (44 bytes)')
print("-" * 20)

# ChunkID: 4 bytes (big)
chunkID = raw_wav[0][0:4]
chunkID_hex = "/".join(hex(i) for i in chunkID)
chunkID_decode = chunkID.decode('ascii')

print(f'ChunkID 4 bytes (big): {chunkID_hex}')
print(f'ChunkID (RIFF): {chunkID_decode}')
print("-" * 20)

# ChunkSize: 4 bytes (little) This is the size of the entire file in bytes minus 8 bytes (not included in this count, ChunkID and ChunkSize)
chunkSize = raw_wav[0][4:8]
chunkSize_decode = int.from_bytes(chunkSize, 'little')

print(f'ChunkSize 4 bytes (little): {"/".join(hex(i) for i in chunkSize)}')
print(f'ChunkSize (bytes): {chunkSize_decode}')
print("-" * 20)

# Format: 4 bytes (big)
format = raw_wav[0][8:12]
format_decode = format.decode('ascii')

print(f'Format 4 bytes (big): {"/".join(hex(i) for i in format)}')
print(f'Format (WAVE): {format_decode}')
print("-" * 20)

# Subchunck1ID: 4 bytes
Subchunck1ID = raw_wav[0][12:16]
Subchunck1ID_decode = Subchunck1ID.decode('ascii')


print(f'Subchunck1ID 4 bytes: {"/".join(hex(i) for i in Subchunck1ID)}')
print(f'Subchunck1ID (fmt): {Subchunck1ID_decode}')
print("-" * 20)

# Subchunck1Size: 4 bytes (little)
Subchunck1Size = raw_wav[0][16:20]
Subchunck1Size_decode = int.from_bytes(Subchunck1Size, 'little') 

print(f'Subchunck1Size 4 bytes (little): {"/".join(hex(i) for i in Subchunck1Size)}')
print(f'Subchunck1Size (16 for PCM): {Subchunck1Size_decode}')
print("-" * 20)

# Audio format: 2 bytes (little)
audio_format = raw_wav[0][20:22]
audio_format_decode = int.from_bytes(audio_format, 'little')


print(f'Audio format 2 bytes (little) : {"/".join(hex(i) for i in audio_format)}')
print(f'Audio format (PCM=1): {audio_format_decode}')
print("-" * 20)

# Number of channels: 2 bytes (little)
numChannels = raw_wav[0][22:24]
numChannels_decode = int.from_bytes(numChannels, 'little')


print(f'Number of Channels 2 bytes (little): {"/".join(hex(i) for i in numChannels)}')
print(f'Number of Channels: {numChannels_decode}')
print("-" * 20)

# Sample Rate: 4 bytes (little)
SampleRate = raw_wav[0][24:28]
SampleRate_decode = int.from_bytes(SampleRate, 'little')


print(f'Sample Rate 4 bytes (little): {"/".join(hex(i) for i in SampleRate)}')
print(f'Sample Rate (Hz): {SampleRate_decode}')
print("-" * 20)

# Byte Rate: 4 bytes (little)
ByteRate = raw_wav[0][28:32]
ByteRate_decode = int.from_bytes(ByteRate, 'little')

print(f'Byte Rate 4 bytes (little): {"/".join(hex(i) for i in ByteRate)}')
print(f'Byte Rate (bytes): {ByteRate_decode}')
print("-" * 20)

# Block Align: 2 bytes (little The number of bytes for one sample )
BlockAlign = raw_wav[0][32:34]
BlockAlign_decode = int.from_bytes(BlockAlign, 'little')

print(f'BlockAlign 2 bytes (little): {"/".join(hex(i) for i in BlockAlign)}')
print(f'BlockAlign (bytes): {BlockAlign_decode}')
print("-" * 20)

# Bit Depth: 2 bytes (little)
BitsPerSample = raw_wav[0][34:36]
BitsPerSample_decode = int.from_bytes(BitsPerSample, 'little')

print(f'Bits Per Sample 2 bytes (little): {"/".join(hex(i) for i in BitsPerSample)}')
print(f'Bits Per Sample (bits): {BitsPerSample_decode}')
print("-" * 20)

# SubChunck2ID: 4 bytes (big)
SubChunck2ID = raw_wav[0][36:40]
SubChunck2ID_decode = SubChunck2ID.decode('ascii')


print(f'SubChunck2ID 4 bytes (big):  {"/".join(hex(i) for i in SubChunck2ID)}')
print(f'SubChunck2ID: {SubChunck2ID_decode}')
print("-" * 20)

# Subchunk2Size: 4 bytes (little)
Subchunk2Size = raw_wav[0][40:44]
Subchunk2Size_decode = int.from_bytes(Subchunk2Size, 'little')

print(f'Subchunk2Size 4 bytes (little): {"/".join(hex(i) for i in Subchunk2Size)}')
print(f'Subchunk2Size (bytes): {Subchunk2Size_decode}')
