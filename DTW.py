from math import *                                      #실행 전 주의사항 1. 이 프로그램은 16스레드 PC기준으로 제작되었으니 이용하는 PC의 스레드 수에 맞춰서
from hummingNmusic import*                              # '#이 부분' 이라고 적혀있는 main_1 함수의 반복문을 수정해주세요. 
from multiprocessing import Process                     # 2배수, 5배수, 10배수로 설정해주시기 바랍니다.
import numpy as np                                      # 예) 2스레드 시 : for numnum in range(0,100,2):
import sys                                              #                     for num in range(numnum,numnum+2):
import time, os                                         # 예) 5스레드 시 : for numnum in range(0,100,5):
import multiprocessing                                  #                       for num in range(numnum, numnum+5):
                                                        # 예) 10스레드 시 : for numnum in range(0,100,10):
                                                        #                       for num in range(numnum, numnum+10):
                                                        #실행 전 주의사항 2. 이 프로그램은 numpy라이브러리를 사용하므로 실행 전 설치해야합니다.
# DTW 함수 출처 :  https://gist.github.com/bistaumanga/6023705

def DTW(A, B, window=sys.maxsize, d=lambda x, y: abs(x - y)):
    # 비용 행렬 초기화
    A = np.array(A)
    B = np.array(B)  
    M, N = len(A), len(B)
    cost = sys.maxsize * np.ones((M, N))

    # 첫번째 로우,컬럼 채우기
    cost[0, 0] = d(A[0], B[0])
    for i in range(1, M):
        cost[i, 0] = cost[i - 1, 0] + d(A[i], B[0])

    for j in range(1, N):
        cost[0, j] = cost[0, j - 1] + d(A[0], B[j])
    # 나머지 행렬 채우기
    for i in range(1, M):
        for j in range(max(1, i - window), min(N, i + window)):
            choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
            cost[i, j] = min(choices) + d(A[i], B[j])

    # 최적 경로 구하기
    n, m = N - 1, M - 1
    path = []

    while (m, n) != (0, 0):
        path.append((m, n))
        m, n = min((m - 1, n), (m, n - 1), (m - 1, n - 1), key=lambda x: cost[x[0], x[1]])

    path.append((0, 0))
    return cost[-1, -1]

#hum_num = 선택할 허밍 번호 / final_cost = 허밍과 노래의 최종 비교값 리스트 / num = 한번에 실행할 수 있는 반복문 갯수
#cost = 허밍사이즈로 나눈 노래의 거리값 / cost_2 = 해당 노래의 거리값중 최소값 / cost_3 = cost_2중 최소값
#humming_size = 허밍사이즈 / humming_data_list = 허밍데이터 배열 / music_data_list = 노래데이터 배열
#y_value = 선택할 노래 번호 / hum_num = 실행중인 허밍 번호 / work_loop = 본체

def work_loop(y_value,final_cost,hum_num):
    A = np.array(humming_data_list[hum_num])
    humming_size = len(humming_data_list[hum_num])
    cost_2 = 9999999
    for j in range(0, (len(music_data_list[0]) - len(humming_data_list[hum_num])),10):
        B = np.array(music_data_list[y_value][j:humming_size + j])
        try:
            if(10 > abs(humming_data_list[hum_num][0] - music_data_list[y_value][j])):
                cost = DTW(A, B, window = 70)
                cost_2 = min(cost,cost_2)
        except IndexError:
            continue
    print(hum_num + 1,"번 허밍과 ",y_value+1,"번 노래의 가장 짧은 유사도거리는 ",cost_2,"입니다")
    final_cost[cost_2] = y_value

#dic_min = final_cost 딕셔너리의 최소값 / mins_dic = 최소값 5개를 반환하기 위한 딕셔너리
def main_1(hum_num):
    manager = multiprocessing.Manager()
    global final_cost
    final_cost = manager.dict()
    start = int(time.time())
    procs = []    
    for numnum in range(0,100,10):                                                      # 이 부분
        for num in range(numnum,numnum+10):                                             # 이 부분
            proc = Process(target=work_loop, args=(num,final_cost,hum_num))
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()
        print("ㅁㅁㅁ total run time :", int(time.time()) - start,"sec ㅁㅁㅁ")
    mins_dict = {}
    for i in range(0,5):
        dic_min = min(final_cost.keys())
        mins_dict[final_cost[dic_min]] = dic_min
        del final_cost[dic_min]
    print("가장 유사한 노래 리스트. (번호 : 값)")
    print(mins_dict)


if __name__ == "__main__": 
    #mainOFmain(0)
    main_1(3)