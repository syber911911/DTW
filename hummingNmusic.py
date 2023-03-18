
#허밍데이터 리스트 만들기------------------------------------------------------------------------------------
humming_data_list = []

def humming_data_append():
    lines = humming_file.readlines()
    humming_data=[]
    for line in lines:
        humming_data.append(int(line.rstrip('/n')))
    humming_data_list.append(humming_data)

humming_file = open('test_F/humming_data/0362_humming4.txt','rt')
humming_data_append()

humming_file = open('test_F/humming_data/0714_humming3.txt','rt')
humming_data_append()

humming_file = open('test_F/humming_data/1197_humming2.txt','rt')
humming_data_append()

humming_file = open('test_F/humming_data/0362_humming4.txt','rt')
humming_data_append()

#허밍데이터 리스트 만들기------------------------------------------------------------------------------------

#뮤직데이터 리스트 만들기------------------------------------------------------------------------------------
music_data_list = []
def music_data_append():
    lines = music_file.readlines()
    music_data=[]
    for line in lines:
        music_data.append(int(line.rstrip('/n')))
    music_data_list.append(music_data)

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0006_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0008_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0011_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0012_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0015_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0016_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0023_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0025_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0053_midinote_VAD_padding_out.txt','rt')
music_data_append()

music_file = open('C:/Users/HEEJUN/Desktop/DTW/test_F/music_data/0061_midinote_VAD_padding_out.txt','rt')
music_data_append()

#뮤직데이터 리스트 만들기------------------------------------------------------------------------------------