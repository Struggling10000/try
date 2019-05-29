# -*- coding:utf-8 -*-
# Filename: test_weather.py
# Author：hankcs
# Date: 2016-08-06 PM6:04
import numpy as np

import HMM

def generate_index_map(lables):
    index_label = {}
    label_index = {}
    i = 0
    for l in lables:
        index_label[i] = l
        label_index[l] = i
        i += 1
    return label_index, index_label

def convert_observations_to_index(observations, label_index):
    list = []
    for o in observations:
        list.append(label_index[o])
    return list


def convert_map_to_vector(map, label_index):
    v = np.empty(len(map), dtype=float)
    for e in map:
        v[label_index[e]] = map[e]
    return v


def convert_map_to_matrix(map, label_index1, label_index2):
    m = np.empty((len(label_index1), len(label_index2)), dtype=float)
    for line in map:
        for col in map[line]:
            m[label_index1[line]][label_index2[col]] = map[line][col]
    return m



def test():

    states = ('Healthy', 'Fever')

    observations = ('normal', 'cold', 'dizzy')

    start_probability = {'Healthy': 0.6, 'Fever': 0.4}

    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6},
    }

    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }



    states_label_index, states_index_label = generate_index_map(states)

    observations_label_index, observations_index_label = generate_index_map(observations)


    A = convert_map_to_matrix(transition_probability, states_label_index, states_label_index)
    print (A)
    B = convert_map_to_matrix(emission_probability, states_label_index, observations_label_index)
    # print B
    observations_index = convert_observations_to_index(observations, observations_label_index)
    pi = convert_map_to_vector(start_probability, states_label_index)
    # print pi

    h = HMM.HMM(A, B, pi)
    V, p = h.viterbi(observations_index)
    print(" " * 7, " ".join(("%10s" % observations_index_label[i]) for i in observations_index))
    for s in range(0, 2):
        print ("%7s: " % states_index_label[s] + " ".join("%10s" % ("%f" % v) for v in V[s]))
    print('\nThe most possible states and probability are:')
    p, ss = h.state_path(observations_index)
    for s in ss:
        print( states_index_label[s],)
    print (p)

    # run a baum_welch_train
    observations_Cdata = ['H', 'G', 'H', 'H', 'G', 'H', 'G']
    observations_data = [0, 1, 0, 0, 1, 0, 1]
#
# # observations_data, states_data = h.simulate(100)
# # print (observations_data)
# # print (states_data)
# guess = HMM.HMM(np.array([[0.8, 0.2],
#                           [0.4, 0.6]]),
#                 np.array([[0.8, 0.2],
#                           [0.4, 0.6]]),
#                 np.array([0.67, 0.33])
#                 )
# guess.baum_welch_train(observations_data)
# states_out = guess.state_path(observations_data)[1]
# print(states_out)


# p = 0.0
# for s in states_data:
#     if next(states_out) == s: p += 1
# print(p / len(states_data))

def test_SorR():
    states = ('S', 'R')

    observations = ('H', 'G')

    start_probability = {'S': 0.67, 'R': 0.33}

    transition_probability = {
        'S': {'S': 0.8, 'R': 0.2},
        'R': {'S': 0.4, 'R': 0.6},
    }

    emission_probability = {
        'S': {'H': 0.8, 'G': 0.2},
        'R': {'H': 0.4, 'G': 0.6},
    }
    states_label_index, states_index_label = generate_index_map(states)
    print(states_label_index, states_index_label)
    observations_label_index, observations_index_label = generate_index_map(observations)
    print(observations_label_index, observations_index_label)
    A = convert_map_to_matrix(transition_probability, states_label_index, states_label_index)
    print("状态转移矩阵：A")
    print(A)
    B = convert_map_to_matrix(emission_probability, states_label_index, observations_label_index)
    print("观察矩阵：B")
    print (B)
    observations_index = convert_observations_to_index(observations, observations_label_index)
    pi = convert_map_to_vector(start_probability, states_label_index)
    print("最初的可能性矩阵：Pi")
    print(pi)

    h = HMM.HMM(A, B, pi)

    V, p = h.viterbi(observations_index)
    print(V, p)
    print(" " * 7, " ".join(("%10s" % observations_index_label[i]) for i in observations_index))
    for s in range(0, 2):
        print("%7s: " % states_index_label[s] + " ".join("%10s" % ("%f" % v) for v in V[s]))
    print('\nThe most possible states and probability are:')
    p, ss = h.state_path(observations_index)
    print(p,ss)
    for s in ss:
        print(states_index_label[s], )
    print(p)

    # run a baum_welch_train
    #observations_Cdata = ['H', 'G', 'H', 'H', 'G', 'H', 'G']
    observations_data = [0, 1, 0, 0, 1, 0, 1]

    # observations_data, states_data = h.simulate(100)
    # print (observations_data)
    # print (states_data)
    guess = HMM.HMM(np.array([[0.8, 0.2],
                              [0.4, 0.6]]),
                    np.array([[0.8, 0.2],
                              [0.4, 0.6]]),
                    np.array([0.67, 0.33])
                    )
    guess.baum_welch_train(observations_data)
    states_out = guess.state_path(observations_data)[1]
    print(states_out)
    # p = 0.0
    # for s in states_data:
    #     if next(states_out) == s: p += 1
    # print(p / len(states_data))


if __name__=="__main__":
    test_SorR()