import pyaudio
import wave

pa = pyaudio.PyAudio()

print("\nAll devices")
devices = [[],[]]
for id in range(pa.get_device_count()):
    if pa.get_device_info_by_index(id)["maxInputChannels"]>0:
        devices[0].append(pa.get_device_info_by_index(id)["name"])
        devices[1].append(pa.get_device_info_by_index(id)["index"])
for i in range(len(devices[0])):
     print(devices[0][i],devices[1][i])
     device_index = int(input("Entrer l'index: "))
     freq = 48000

     try:
         stream = pa.open(
             rate = freq,
             channels =2,
             format =pyaudio.paInt16,
             input = True,
             input_device_index = device_index,
             frames_per_buffer = 2048
         )
     except OSError as e :
         print(e)
     else:
         print("recording")
         audio = []
         for i in range(20):
             data = stream.read(freq)
             audio.append(data)
             print ("finished")
             stream.stop_stream()
             stream.close()
             pa.terminate()

             with wave.open("test.wav","wb") as fichier:
                 fichier.setnchannels(2)
                 fichier.setsampwidth(2)
                 fichier.setframerate(freq)

                 for byte in audio:
                     fichier.writeframes(byte)
                     print("okay")
                     