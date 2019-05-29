import numpy as np
def HMM(A,B,C,obser_seq):
    """
    :param A: 状态转移概率
    :param B: 观测概率
    :param C: 初始概率
    :param obser_seq: 观测序列
    :return: 状态序列
    """
    state=np.zeros((len(C),len(obser_seq)))##state
    prob=np.zeros((len(C),len(obser_seq)))
    ##利用循环计算每一种观测对应的几个状态的概率，找到每种最大概率对应的前一种的状态
    for i in range(len(obser_seq)):
        for j in range(len(C)):
            temp_state = obser_seq[i]
            if i==0:
                prob[j][0]=C[j]*B[j][temp_state]

            else :
                temp_arry=np.zeros((len(C),1))
                #print(temp_arry)
                for k in range(len(C)):
                    print(prob[k][i-1],A[k][j],B[k][temp_state],end="")
                    temp_arry[k]=prob[k][i-1]*A[k][j]*B[k][temp_state]
                    print(temp_arry[k])
                prob[j][i]=np.max(temp_arry)
                t = np.where(temp_arry == np.max(temp_arry))
                state[j][i]=int(t[0][0])
    #print(state,prob)
    predict_seq=[]
    t=len(obser_seq)
    next=0
    ## 循环回推概率序列
    for i in range(len(obser_seq)):
        if i == 0:
            #print(np.shape(prob))
            max=np.max(prob[:,t-1])
            sub=np.where(prob[:,t-1]==max)
            predict_seq.insert(0,sub[0][0])
            #print(predict_seq)
            temp=int(sub[0][0])
            #print(temp)
            next=int(state[temp,t-1])
        else :
            # print(next)
            predict_seq.insert(0, int(state[next,t-i]))
            next=int(state[next,t-i])
    return predict_seq



def test_SorR():
    A=[[0.8,0.2],[0.4,0.6]]#状态转移概率
    B=[[0.8,0.2],[0.4,0.6]]#观测概率
    C=[0.67,0.33]
    obser_seq=[0, 1, 0, 0, 1, 0, 1]
    preseq=HMM(A,B,C,obser_seq)
    print(preseq)
def test_RorW():
    A=[[0,1,0,0],[0.4,0,0.6,0],[0,0.4,0,0.6],[0,0,0.5,0.5]]#状态转移概率
    B=[[0.5,0.5],[0.3,0.7],[0.6,0.4],[0.8,0.2]]#观测概率
    C=[0.25,0.25,0.25,0.25]
    obser_seq=[0, 0, 1, 1, 0]
    preseq=HMM(A,B,C,obser_seq)
    print(preseq)

if __name__=="__main__":
    # C=[2,3,4,5,6,7,5,7,3]
    # print(np.max(C))
    # t=np.where(C ==np.max(C))
    # print(t)
    # print(t[0][0])
    test_SorR()
    test_RorW()