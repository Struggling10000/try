import numpy
import math
import random
import scipy.stats
def rand_icon(round,times,priors):
    '''
    rand_icon:生成随机的硬币排布
    :param round: 抛硬币的
    :param times:
    :param priors: 硬币的概率
    :return:
    '''
    p1=1-priors[0]
    p2=1-priors[1]
    round=int(round/2)
    observations = []
    for j in range(round):
        list1 = []
        list2 = []
        for i in range(times):
            if random.random()<p1:
                list1.append(0)
            else:
                list1.append(1)

            if random.random()<p2:
                list2.append(0)
            else:
                list2.append(1)
        observations.append(list1)
        observations.append(list2)

    return observations





#硬币投掷结果
observations = numpy.array([[1,0,0,0,1,1,0,1,0,1],
                        [1,1,1,1,0,1,1,1,0,1],
                        [1,0,1,1,1,1,1,0,1,1],
                        [1,0,1,0,0,0,1,1,0,0],
                        [0,1,1,1,0,1,1,1,0,1]])
def em_single(observations,priors):

    """
    EM算法的单次迭代
    Arguments
    ------------
    priors:[theta_A,theta_B]
    observation:[m X n matrix]

    Returns
    ---------------
    new_priors:[new_theta_A,new_theta_B]
    :param priors:
    :param observations:
    :return:
    """
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}
    theta_A = priors[0]
    theta_B = priors[1]
    #E step
    for observation in observations:
        len_observation = len(observation)
        num_heads = observation.sum()
        num_tails = len_observation-num_heads
        #二项分布求解公式
        contribution_A = scipy.stats.binom.pmf(num_heads,len_observation,theta_A)
        contribution_B = scipy.stats.binom.pmf(num_heads,len_observation,theta_B)

        weight_A = contribution_A / (contribution_A + contribution_B)
        weight_B = contribution_B / (contribution_A + contribution_B)
        #更新在当前参数下A，B硬币产生的正反面次数
        counts['A']['H'] += weight_A * num_heads
        counts['A']['T'] += weight_A * num_tails
        counts['B']['H'] += weight_B * num_heads
        counts['B']['T'] += weight_B * num_tails

    # M step
    new_theta_A = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    new_theta_B = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])
    return [new_theta_A,new_theta_B]

def em(observations,prior,tol = 1e-6,iterations=10000):
    """
    EM算法
    ：param observations :观测数据
    ：param prior：模型初值
    ：param tol：迭代结束阈值
    ：param iterations：最大迭代次数
    ：return：局部最优的模型参数
    """
    iteration = 0;
    while iteration < iterations:
        new_prior = em_single(observations,prior)
        delta_change = numpy.abs(prior[0]-new_prior[0])
        if delta_change < tol:
            break
        else:
            prior = new_prior
            iteration +=1
    return [new_prior,iteration]
def count_real_prob(observations,round,times):
    """
    count_real_prob:计算生成数据真实的概率
    :param observations: 生成的观测数据
    :param round:
    :param times:
    :return: 返回真实的概率
    """
    li=[]
    a=0
    b=0
    t=int(round/2)
    for observation in observations:
        li.append(sum(observation))
    for i in range(t):
        a=a+li[2*i]
        b=b+li[2*i+1]
    return a/(t*times) ,b/(t*times)


observations=rand_icon(10,10,[0.2,0.5])
observations=numpy.array(observations)
print('随机生成的硬币结果如下：')
print(observations)
print('生成数据的A，和B的真实概率为：')
print(count_real_prob(observations,10,10))
print("当迭代停止时的概率和次数")
print (em(observations,[0.6,0.5]))