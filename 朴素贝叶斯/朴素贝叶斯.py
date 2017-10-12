def createVocabList(dataSet):
    """
    ��ȡ���е��ʵļ���
    :param dataSet: ���ݼ�
    :return: ���е��ʵļ���(�������ظ�Ԫ�صĵ����б�)
    """
    vocabSet = set([])  # create empty set
    for document in dataSet:
        # ������ | �������������ϵĲ���
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)
def setOfWords2Vec(vocabList, inputSet):
    """
    �����鿴�õ����Ƿ���֣����ָõ����򽫸õ�����1
    :param vocabList: ���е��ʼ����б�
    :param inputSet: �������ݼ�
    :return: ƥ���б�[0,1,0,1...]������ 1��0 ��ʾ�ʻ���еĵ����Ƿ��������������ݼ���
    """
    # ����һ���ʹʻ��ȳ���������������Ԫ�ض�����Ϊ0
    returnVec = [0] * len(vocabList)# [0,0......]
    # �����ĵ��е����е��ʣ���������˴ʻ���еĵ��ʣ���������ĵ������еĶ�Ӧֵ��Ϊ1
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec