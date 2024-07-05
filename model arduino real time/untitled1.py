# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B9A1nVnJsJWuN1Mx47ZZnf1cbKyLVURL
"""

import shutil
import time
import keyboard

source_directory = "C:\\Users\\2maju\\OneDrive\\Documents\\BYB"
destination_directory = "path\\"
import serial
    # Open the serial port
ser = serial.Serial('COM3', baudrate=9600,timeout=1)

def send_signal_to_com_port(signal_data):

    # Convert the signal data to bytes
    signal_data_bytes = str(signal_data)
    # signal_data_bytes=signal_data_bytes.encode()
    # Send the signal data
    ser.write(bytes(signal_data_bytes,'utf-8'))
    print("done")
    # Close the serial port





while True:

    files = os.listdir(source_directory)

    if files:
        for file in files:
            source_file_path = os.path.join(source_directory, file)
            # destination_file_path = os.path.join(destination_directory, file)

            # Move the file
            shutil.copy(source_file_path, destination_directory)
            if os.path.exists(source_file_path):
                os.remove(source_file_path)


    # Add a delay to prevent continuous checking and reduce CPU usage
    time.sleep(1)
    file = os.listdir(destination_directory)
    if len(file)!=0:
        signal, sr = librosa.load(os.path.join(destination_directory, file[0]))
        signal = librosa.resample(signal, orig_sr = sr, target_sr=10000)
        signal = signal[:100000]
        stft = librosa.stft(signal, n_fft=2048, hop_length=512,center=False)
        log_stft = librosa.amplitude_to_db(np.abs(stft))
        normalized_spectrogram = (log_stft - np.min(log_stft)) / (np.max(log_stft) - np.min(log_stft))
        # Apply the log transformation
        log_spectrogram = np.log(normalized_spectrogram + 1e-10)
        # print(log_spectrogram)
        log_spectogram=np.reshape(log_spectrogram,(1,log_spectrogram.shape[0],log_spectrogram.shape[1],1))
        prediction=model.predict(log_spectogram)
        # ser1.write(prediction[0])
        print(prediction)
        if prediction > 0.5:
            value =1

        else:
            value=0
        #CODE FOR MOTOR CONTROL#
        print(value)
        send_signal_to_com_port(value)
        os.remove(os.path.join(destination_directory, file[0]))

        print("File deleted successfully.")
    if keyboard.is_pressed('q'):
            print("pressed")
            time.sleep(17)