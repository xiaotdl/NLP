def Viterbi(N,T,a,b,observation, tags_without_start_period):
    '''
    viterbi--a array of path probability; viterbi[N+2,T], initialize to all 0s
    backpointer--as same as viterbi recording state path
    N--number of states; tags number; not including start and end
    T--number of observations; sentence length
    a--array of transitional probabilities; P(t1|t0), a[0][0]--the probability of transferring from state 0 to state 1
    b--array of state probabilities; P(w|t), b[s-1][observation[0]]--the probability of given tag s, the word is observation 1.
    '''
    viterbi = [[0 for n in range(N+2)] for n in range(T+1)]
    backpointer = [[0 for n in range(N+2)] for n in range(T+1)] 
    
    # initialization
    for s in range(1, N+1):
#         print b[7][observation[0]]
#         print b[tags_without_start_period[s-1]]
        if observation[0] in b[tags_without_start_period[s-1]]:
            viterbi[1][s] = a['S'][tags_without_start_period[s-1]] * b[tags_without_start_period[s-1]][observation[0]]
            backpointer[1][s] = 'S'
    print viterbi
    print backpointer
    
    #recursion
    for t in range(2, T+1):
        for s in range(1, N+1):
    #         viterbi[s][t] = max{viterbi[s-1][t-1]*a[s-1][s]*b[t][s]}
    #         backpointer[s][t] = argmax{viterbi[s-1][t-1]*a[s-1][s]}
            max_newV = [0, 0]
            for s_last in range(1, N+1):
                if observation[t-1] in b[tags_without_start_period[s-1]]:
                    if viterbi[t-1][s_last]*a[tags_without_start_period[s_last-1]][tags_without_start_period[s-1]]*b[tags_without_start_period[s-1]][observation[t-1]] > max_newV[0]:
                        max_newV[0] = viterbi[t-1][s_last]*a[tags_without_start_period[s_last-1]][tags_without_start_period[s-1]]*b[tags_without_start_period[s-1]][observation[t-1]]
                        max_newV[1] = tags_without_start_period[s_last-1]
            viterbi[t][s] = max_newV[0]            
            backpointer[t][s] = max_newV[1]
#             print 'a', tags_without_start_period[s_last-1], tags_without_start_period[s-1], 'b', tags_without_start_period[s-1], observation[t-1], 'pointer', tags_without_start_period[s_last-1]
#             
#                         print viterbi[t-1][s_last]*a[tags_without_start_period[s_last-1]][tags_without_start_period[s-1]]*b[tags_without_start_period[s-1]][observation[t-1]]
#                         backpointer[t][s] = tags_without_start_period[s_last-1]
    print viterbi
    print backpointer

    #termination
    # viterbi[N+1][T] = max{viterbi[s][T]*a[s][N+1]}
#     for s in range(1, N+1):
# #         print viterbi[s][T-1]
# #         print viterbi[s][T]
# #         print a[s-1][N-1]
# #         print viterbi[N+1][T]
#         if viterbi[s][T-1]*a[s][N] > viterbi[N+1][T-1]:
#             viterbi[N+1][T-1] = viterbi[s][T-1]*a[s][N]
#             backpointer[N+1][T-1] = s
# #     return output_tags
#     return backpointer