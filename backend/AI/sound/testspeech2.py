import sys

def main(name):
    # [START speech_quickstart]
    import io
    import os
    from pydub import AudioSegment

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
    AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
    AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"        
    # [END migration_import]

    # Instantiates a client
    # [START migration_client]
    client = speech.SpeechClient()
    # [END migration_client]

    # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     '.',
    #     'file.wav')
    # print("++++++++++======")
    # print(file_name)
    # print("++++++++++======")
    file_name = name
    print(file_name)
    #file_name = argv
    str_name = str(file_name).split('.')[-1]
    filename1 = "C:/Users/multicampus/SSAFY/Final/backend/AI/captioning/test/images/" + str(file_name)

    if str_name == "wav":
        print("wav")    
        sound = AudioSegment.from_wav(filename1)

    sound = sound.set_channels(1)
    sound.export(filename1, format="wav")

    sound = AudioSegment.from_wav(filename1)

    frames_per_second = sound.frame_rate

    print(frames_per_second)
    
    # Loads the audio into memory
    with io.open(filename1, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frames_per_second,
        language_code='en')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        stt = result.alternatives[0].transcript
        return stt
    # [END speech_quickstart]

if __name__ == "__main__" :
    main(sys.argv[1])